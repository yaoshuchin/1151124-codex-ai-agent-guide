import asyncio
import os
import json
import re
from playwright.async_api import async_playwright

async def main():
    os.makedirs("assets/slides", exist_ok=True)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            headless=True
        )
        context = await browser.new_context(viewport={"width": 1920, "height": 1080})
        page = await context.new_page()
        
        url = "https://www.canva.com/design/DAHWBVG4DgA/6QudLzXya3PKuMDNX-CWHQ/view?utm_content=DAHWBVG4DgA&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h85ffc483d8#1"
        print("Navigating to Canva presentation...")
        await page.goto(url, wait_until="networkidle", timeout=60000)
        await asyncio.sleep(4)
        
        # 1. First extract the bootstrap JSON directly from the page DOM
        bootstrap_data = await page.evaluate('''() => {
            const scripts = Array.from(document.querySelectorAll('script'));
            for (let s of scripts) {
                if (s.textContent && s.textContent.includes("window['bootstrap']")) {
                    const idx1 = s.textContent.indexOf("JSON.parse('");
                    if (idx1 !== -1) {
                        const start = idx1 + 12;
                        const end = s.textContent.lastIndexOf("');");
                        const raw = s.textContent.substring(start, end);
                        try {
                            const unescaped = raw.replace(/\\\\'/g, "'").replace(/\\\\\\\\/g, "\\\\");
                            return JSON.parse(unescaped);
                        } catch(e) {
                            return { error: e.toString() };
                        }
                    }
                }
            }
            return null;
        }''')
        
        if bootstrap_data and "error" not in bootstrap_data:
            with open("canva_bootstrap_parsed.json", "w", encoding="utf-8") as f:
                json.dump(bootstrap_data, f, ensure_ascii=False, indent=2)
            print("Successfully extracted bootstrap data directly from JS!")
        else:
            print("Could not parse bootstrap directly, will decode string.")

        # Let's hide any Canva UI toolbars or popups if needed for clean screenshots
        # Or let's inspect the slide container
        
        # Loop through all 50 slides
        slides = []
        print("Starting 50 slides capture...")
        for i in range(1, 51):
            slide_path = f"assets/slides/slide_{i:02d}.png"
            
            # Wait a moment for slide render
            await asyncio.sleep(1.2)
            
            # Take screenshot of the page
            await page.screenshot(path=slide_path)
            
            # Extract texts and links visible on current slide
            slide_data = await page.evaluate('''() => {
                const results = [];
                const ignored = [
                    '分享', '在 Canva 中創作', '上一頁', '下一頁', '放大和縮小', 
                    '顯示更多', '進入全螢幕', '工具列', '前往頁面', '淡化', 
                    'Canva', '(在新的索引標籤或視窗中開啟)', '深藍背景', 'A'
                ];
                
                // Get all text nodes
                const elements = Array.from(document.querySelectorAll('span, p, h1, h2, h3, h4, div'));
                for (let el of elements) {
                    if (el.children.length === 0 && el.innerText && el.innerText.trim()) {
                        const t = el.innerText.trim();
                        if (!ignored.includes(t) && !/^\\d+\\s*\\/\\s*50$/.test(t) && !/^第\\s*\\d+\\s*頁.*共\\s*50\\s*頁/.test(t)) {
                            results.push(t);
                        }
                    }
                }
                
                // Links
                const links = Array.from(document.querySelectorAll('a'))
                    .map(a => ({ text: a.innerText.trim(), href: a.href }))
                    .filter(l => l.href && !l.href.includes('canva.com'));
                    
                return {
                    texts: Array.from(new Set(results)),
                    links: links
                };
            }''')
            
            slide_entry = {
                "page": i,
                "screenshot": slide_path,
                "texts": slide_data["texts"],
                "links": slide_data["links"]
            }
            slides.append(slide_entry)
            print(f"[{i}/50] Captured: {len(slide_entry['texts'])} texts | sample: {slide_entry['texts'][:2]}")
            
            # Advance to next slide
            if i < 50:
                await page.keyboard.press("ArrowRight")
                
        with open("captured_slides.json", "w", encoding="utf-8") as f:
            json.dump(slides, f, ensure_ascii=False, indent=2)
        print("Completed all 50 slides! Saved to captured_slides.json")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

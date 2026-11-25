import asyncio
import os
import json
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
        print("Loading Canva presentation...")
        await page.goto(url, wait_until="networkidle", timeout=60000)
        await asyncio.sleep(4)
        
        # Test finding next button
        next_button = page.locator('button[aria-label="下一頁"]')
        print("Next button visible:", await next_button.is_visible())
        
        slides_info = []
        for i in range(1, 6):
            print(f"Processing slide {i}...")
            # Take screenshot of the slide container or full page
            await page.screenshot(path=f"assets/slides/slide_{i:02d}.png")
            
            # Extract texts
            texts = await page.evaluate('''() => {
                // Find all text elements inside main viewer area
                const elements = Array.from(document.querySelectorAll('span, p, h1, h2, h3, h4, a, div'));
                const results = [];
                for (let el of elements) {
                    if (el.children.length === 0 && el.innerText && el.innerText.trim()) {
                        const t = el.innerText.trim();
                        // Filter out Canva UI controls
                        if (!['分享', '在 Canva 中創作', '上一頁', '下一頁', '放大和縮小', '顯示更多', '進入全螢幕', '工具列', '前往頁面', '淡化', 'Canva', '(在新的索引標籤或視窗中開啟)'].includes(t) && !/\\d+\\s*\\/\\s*50/.test(t)) {
                            results.push(t);
                        }
                    }
                }
                // Also get all link hrefs
                const links = Array.from(document.querySelectorAll('a')).map(a => ({ text: a.innerText.trim(), href: a.href })).filter(l => l.href && !l.href.includes('canva.com'));
                return { texts: Array.from(new Set(results)), links: links };
            }''')
            print(f"Slide {i} texts:", texts["texts"])
            print(f"Slide {i} links:", texts["links"])
            slides_info.append({"page": i, **texts})
            
            # Press next
            await page.keyboard.press("ArrowRight")
            await asyncio.sleep(1.5)
            
        await browser.close()
        print("Done test.")

if __name__ == "__main__":
    asyncio.run(main())

import asyncio
import json
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            headless=True
        )
        page = await browser.new_page(viewport={"width": 1920, "height": 1080})
        url = "https://www.canva.com/design/DAHWBVG4DgA/6QudLzXya3PKuMDNX-CWHQ/view?utm_content=DAHWBVG4DgA&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h85ffc483d8#1"
        print("Navigating to Canva...")
        await page.goto(url, wait_until="networkidle", timeout=60000)
        await asyncio.sleep(5)
        
        title = await page.title()
        print("Page title:", title)
        
        # Take a screenshot to inspect
        await page.screenshot(path="canva_page_1.png")
        print("Saved canva_page_1.png")
        
        # Look for buttons or navigation
        buttons = await page.evaluate('''() => {
            return Array.from(document.querySelectorAll('button')).map(b => ({
                text: b.innerText,
                aria: b.getAttribute('aria-label')
            }));
        }''')
        print(f"Buttons found: {len(buttons)}")
        for b in buttons[:20]:
            print("Button:", b)
            
        # Get page counter or slide info
        counters = await page.evaluate('''() => {
            const res = [];
            document.querySelectorAll('*').forEach(el => {
                if (el.children.length === 0 && el.innerText && /\\d+\\s*\\/\\s*\\d+/.test(el.innerText)) {
                    res.push(el.innerText);
                }
            });
            return res;
        }''')
        print("Counters:", counters)
        
        # Extract text elements
        texts = await page.evaluate('''() => {
            const els = Array.from(document.querySelectorAll('p, h1, h2, h3, h4, span, div'));
            const list = [];
            for (let el of els) {
                if (el.children.length === 0 && el.innerText && el.innerText.trim().length > 0) {
                    list.push(el.innerText.trim());
                }
            }
            return Array.from(new Set(list));
        }''')
        print(f"Extracted {len(texts)} unique text nodes:")
        for t in texts[:30]:
            print(" - ", t)
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

from pathlib import Path
import asyncio
from playwright.async_api import async_playwright

URL = 'https://ticketing.almeida.co.uk/8745/8899'

async def main():
    out = Path('diagnostic')
    out.mkdir(exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1280, 'height': 900})
        try:
            response = await page.goto(URL, wait_until='domcontentloaded', timeout=60000)
            await page.wait_for_timeout(10000)
            text = await page.locator('body').inner_text()
            (out / 'page.txt').write_text(text, encoding='utf-8')
            await page.screenshot(path=str(out / 'page.png'), full_page=True)
            links = await page.locator('a').evaluate_all('(nodes) => nodes.map(a => ({text:a.innerText, url:a.href}))')
            import json
            (out / 'links.json').write_text(json.dumps(links, indent=2), encoding='utf-8')
            status = response.status if response else 'unknown'
            summary = f'HTTP status: {status}\nFinal URL: {page.url}\nTitle: {await page.title()}\nNo availability or price has been verified. No purchase attempted.\n'
            (out / 'summary.txt').write_text(summary, encoding='utf-8')
        finally:
            await browser.close()

asyncio.run(main())

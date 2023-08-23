""" Takes a list of urls from the urls.txt file and takes a screenshot of each.
"""
import asyncio
import time
from playwright.async_api import async_playwright
import helpers.file as f


async def main():
    """Main function
    """
    start = time.perf_counter()
    async with async_playwright() as play:
        browser = await play.chromium.launch()
        page = await browser.new_page()
        url_list = f.get_urls()
        for url in url_list:
            await page.goto(url)
            await page.screenshot(path=f.dir_path() + '/' + f.file_name(url), full_page=True)
        await browser.close()
    end = time.perf_counter()
    print(f'It took {round(end-start,0)} second(s) to complete.')
asyncio.run(main())

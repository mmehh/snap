""" Takes a list of urls from the urls.txt file and takes a screenshot of each.
"""
import asyncio
import time
from playwright.async_api import async_playwright
import helpers.file as f
import helpers.browser as b


async def main():
    """Main function using asyncio tasks and browser new context
    """
    start = time.perf_counter()
    async with async_playwright() as play:
        browser = await play.chromium.launch()

        url_list = f.get_urls()
        tasks = set()
        async with asyncio.TaskGroup() as task_group:
            for url in url_list:
                tasks.add(task_group.create_task(b.take_shot(
                    browser, url, f.dir_path() + '/' + f.file_name(url))))
        await browser.close()
    end = time.perf_counter()
    print(f'It took {round(end-start,0)} second(s) to complete.')

asyncio.run(main())

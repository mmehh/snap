"""Browser Helper
"""
import time


async def take_shot(browser, url, file_path):
    """ Performs a screenshot of the webpage for supplied url.

    Args:
        browser (Browser): _description_
        url (str): _description_
    """
    start = time.perf_counter()
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto(url)
    await page.screenshot(path=file_path, full_page=True)
    end = time.perf_counter()
    print(f'The task took {round(end-start,0)} second(s) to complete.')
    return

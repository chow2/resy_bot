from playwright.async_api import async_playwright
from dotenv import load_dotenv
from datetime import datetime
import pandas as pd
import asyncio
import os
import time



# load environment variables from .env file
load_dotenv()
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
RESTAURANT_NAME = os.getenv('RESTAURANT_NAME')
DATE = os.getenv('DATE')
TARGET_TIME = os.getenv('TARGET_TIME')
EARLIEST = os.getenv('EARLIEST')
LATEST = os.getenv('LATEST')
PARTY_SIZE = os.getenv('PARTY_SIZE')


async def run(start_url):
	"""_summary_
	"""
	# convert time strings to datetime time objects
	EARLIEST = datetime.strptime(EARLIEST, "%H:%M:%S").time()
	TARGET_TIME = datetime.strptime(TARGET_TIME, "%H:%M:%S").time()
	LATEST = datetime.strptime(LATEST, "%H:%M:%S").time()

	async with async_playwright() as p:
		try:
			# launch non-headless browser
			browser = await p.chromium.launch(headless=False)

			# open new page
			page = await browser.new_page()
			await page.goto(start_url)

			# click login button
			await page.click('button[data-test-id="menu_container-button-log_in"]')

			# click use email & password
			await page.get_by_text("Use Email and Password instead").click()

			# fill email & password
			await page.get_by_placeholder("Email Address").fill(EMAIL)
			await page.get_by_placeholder("Password").fill(PASSWORD)

			# click continue
			await page.get_by_text("Continue").click()
			
			# search for restaurant name
			await page.get_by_placeholder("Search restaurants, cuisines, etc.").fill(RESTAURANT_NAME)

			# click on first option
			await page.click('li[role="option"]')

			# now check what reservations are available
			#id="rgs://resy/51293/2591024/2/2024-12-18/2024-12-18/19:00:00/2/Dining Room"
			#id="rgs://resy/65463/2920970/2/2024-12-18/2024-12-18/19:00:00/2/Table Seating"

			

			
			time.sleep(5)





			time.sleep(5)
			




		except Exception as e: 
			print(f"An error occurred: {e}")
		finally:
			try: 
				await browser.close()
			except Exception as e:
				print(f"Failed to close browser: {e}")

async def main():
	URL = f"https://resy.com/?seats={PARTY_SIZE}&date={DATE}"
	print(f"URL: {URL}")
	await run(URL)


if __name__ == '__main__':
	asyncio.run(main())

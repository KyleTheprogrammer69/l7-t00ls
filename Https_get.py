import asyncio
import aiohttp
import logging
import subprocess

logging.basicConfig(level=logging.INFO)

async def simulate_protocol(session, url, headers, request_num):
    try:
        async with session.get(url, headers=headers) as response:
            text = await response.text()
            logging.info(f"Request {request_num} successful")
            return text
    except (aiohttp.ClientError, aiohttp.ServerDisconnectedError) as e:
        logging.error(f"Error fetching {url}: {e}")
        return None

async def send_protocol_requests(url, headers, total_requests):
    async with aiohttp.ClientSession() as session:
        for i in range(total_requests):
            response = await simulate_protocol(session, url, headers, i+1)

    logging.info("All requests sent")

while True:
    try:
        choice = input("1. Enter the website URL and number of requests\n0. Return to menu1v.py\nEnter your choice: ")

        if choice == '1':
            website_url = input("Enter the website URL: ")
            total_requests = int(input("Enter the total number of requests to send: "))
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/605.1.15 (KHTML, like Gecko) Opera/85.0.4183.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
            }
            asyncio.run(send_protocol_requests(website_url, headers, total_requests))
        elif choice == '0':
            subprocess.run(["python", "menu1v.py"])  # Assuming menu1v.py is in the same directory
            break
        else:
            print("Invalid choice. Please try again.")

    except Exception as e:
        logging.error(f"An error occurred: {e}. Restarting...")

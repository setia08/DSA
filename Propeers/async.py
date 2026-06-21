import asyncio
import aiohttp   # async version of requests

# USE CASE 1 — Fetching multiple URLs at the same time
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            fetch(session, "https://api.github.com"),
            fetch(session, "https://api.example.com"),
            fetch(session, "https://api.another.com"),
        )
    # all 3 fetched simultaneously!
# USE CASE 2 — Multiple tasks with delays
async def task(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)    # simulates waiting (API, DB, file)
    print(f"{name} done after {delay}s")

async def main():
    await asyncio.gather(
        task("Download", 3),
        task("Upload",   2),
        task("Process",  1),
    )

asyncio.run(main())

# Output:
# Download started
# Upload started
# Process started
# Process done after 1s
# Upload done after 2s
# Download done after 3s
# Total time: 3s (not 6s!)

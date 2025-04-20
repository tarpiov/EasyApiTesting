import asyncio, aiohttp, pathlib
from utils.screen import Screen, Colors

CONCURRENCY = 20 

async def make_request(session, url, sem):
    async with sem:                    
        try:
            async with session.get(url) as resp:
                if resp.headers.get("Content-Type", "").startswith("application/json"):
                    if resp.status == 200:
                        print(f"{Colors.green}[{resp.status}] {Colors.white}{url} {Colors.reset}")

                    if resp.status != 200:
                        pass

        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            print(Colors.red + f"{url} -> ERROR {e}" + Colors.reset)


async def main():
    Screen.clearScreen()
    Screen.printBanner()

    base_url = input(f"{Colors.magenta}Target (p.ej. https://api.ejemplo.com): {Colors.reset}").rstrip("/")
    option   = input(f"{Colors.magenta}1. Rápido (endpointsLite.txt)\n2. Lento  (endpointsLargue.txt)\n> {Colors.reset}").strip()

    wordlist_path = "./wordlists/endpointsLite.txt" if option == "1" else "./wordlists/endpointsLargue.txt"
    endpoints = [l.strip() for l in pathlib.Path(wordlist_path).read_text().splitlines() if l.strip()]

    sem = asyncio.Semaphore(CONCURRENCY)
    timeout = aiohttp.ClientTimeout(total=10)
    connector = aiohttp.TCPConnector(limit=CONCURRENCY)

    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        tasks = [
            make_request(
                session,
                ep if ep.startswith("http") else f"{base_url}/{ep.lstrip('/')}",
                sem
            )
            for ep in endpoints
        ]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())

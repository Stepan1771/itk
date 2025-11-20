import asyncio
import json
from typing import Dict, List

import aiohttp


async def fetch_urls(
    urls: List[str],
    file_path: str = "results.json",
) -> Dict[str, int]:

    sem = asyncio.Semaphore(5)
    timeout = aiohttp.ClientTimeout(total=10)
    results: Dict[str, int] = {}

    async with aiohttp.ClientSession(timeout=timeout) as session:

        async def _fetch(url: str):
            async with sem:
                try:
                    async with session.get(url) as resp:
                        results[url] = resp.status
                except (aiohttp.ClientError, asyncio.TimeoutError):
                    results[url] = 0
                except Exception:
                    results[url] = 0

        tasks = [asyncio.create_task(_fetch(url)) for url in urls]
        await asyncio.gather(*tasks)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    return results


if __name__ == "__main__":
    sample_urls = [
        "https://example.com",
        "https://httpbin.org/status/404",
        "https://nonexistent.url",
    ]

    results = asyncio.run(fetch_urls(sample_urls))
    print(results)

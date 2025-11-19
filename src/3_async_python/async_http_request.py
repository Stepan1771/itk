import asyncio
import json
from typing import Dict, List

import aiohttp


async def fetch_urls(
    urls: List[str], file_path: str = "results.jsonl"
) -> Dict[str, int]:
    """
    Выполняет асинхронные GET-запросы к списку urls, максимум 5 одновременно.
    Возвращает словарь {url: status_code}. При ошибке соединения или таймауте
    присваивает статус 0. Результат сохраняется в файл file_path в формате JSON.
    """
    sem = asyncio.Semaphore(5)
    timeout = aiohttp.ClientTimeout(total=10)  # можно настроить
    results: Dict[str, int] = {}

    async with aiohttp.ClientSession(timeout=timeout) as session:

        async def _fetch(url: str):
            async with sem:
                try:
                    async with session.get(url) as resp:
                        results[url] = resp.status
                except (aiohttp.ClientError, asyncio.TimeoutError):
                    # сетевые ошибки, таймауты и пр.
                    results[url] = 0
                except Exception:
                    # поймать прочие неожиданные ошибки
                    results[url] = 0

        tasks = [asyncio.create_task(_fetch(url)) for url in urls]
        await asyncio.gather(*tasks)

    # Сохранить все результаты в файл (перезаписываем)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    return results


# Пример использования:
if __name__ == "__main__":
    sample_urls = [
        "https://example.com",
        "https://httpbin.org/status/404",
        "https://nonexistent.domain.test",  # приведёт к статусу 0
    ]

    results = asyncio.run(fetch_urls(sample_urls, "results.jsonl"))
    print(results)

import asyncio
from loguru import logger
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

logger.add(
    "file.log",
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
    rotation="10 MB",
    retention="30 days"
)


async def main():
    try:
        logger.info("Запущено")
    except Exception as e:
        logger.error(f"Ошибка при запуске: {e}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Остановлено вручную")
    except Exception as e:
        logger.critical(f"Критическая ошибка: {e}")

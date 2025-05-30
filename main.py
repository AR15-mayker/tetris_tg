from loguru import logger
from input_handler import handle_input
from renderer import Renderer

logger.add(
    "file.log",
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
    rotation="10 MB",
    retention="30 days"
)


def main():
    try:
        Renderer()

        handle_input()
        logger.info("Запущено")
    except Exception as e:
        logger.error(f"Ошибка при запуске: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Остановлено вручную")
    except Exception as e:
        logger.critical(f"Критическая ошибка: {e}")

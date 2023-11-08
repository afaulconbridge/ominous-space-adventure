import logging

from textual.app import App
from textual.logging import TextualHandler

logging.basicConfig(
    level="INFO",
    handlers=[TextualHandler()],
)


class LogApp(App):
    def on_mount(self) -> None:
        logging.info("Logged via TextualHandler")


if __name__ == "__main__":
    LogApp().run()

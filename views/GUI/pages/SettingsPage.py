import toga
from toga.style.pack import Pack
from toga.constants import COLUMN
from views.GUI.utils.AbstractPage import AbstractPage


class SettingsPage(AbstractPage):
    def __init__(self, app) -> None:
        super().__init__(app)

    def build(self) -> toga.Widget:
        self.label_title = toga.Label(
            "Page de paramètre",
            style=Pack(padding=(10, 20, 10), font_style="italic"),
        )
        self.go_to_main_btn = toga.Button(
            "Aller à la page principale",
            on_press=self.go_to_main_page_callback, # type: ignore
            style=Pack(padding=(10, 20, 20)),
        )

        container = toga.Box(
            children=[
                self.label_title,
                self.go_to_main_btn,
            ],
            style=Pack(direction=COLUMN),
        )

        return container

    def go_to_main_page_callback(self, event=None):
        self._app.go_to_page("main")

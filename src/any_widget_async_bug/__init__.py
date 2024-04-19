import importlib.metadata
import pathlib
import time
from typing import Any

import anywidget
import traitlets
from traitlets import Int, observe

try:
    __version__ = importlib.metadata.version("any_widget_async_bug")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"


class BugWidget(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "static" / "widget.js"
    _css = pathlib.Path(__file__).parent / "static" / "widget.css"

    value = Int(0).tag(sync=True)

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.value_computing = False

    def compute_value(self):
        self.value_computing = True
        self.send({"event_name": "compute_value"})
        while self.value_computing:
            time.sleep(0.1)
        return self.value

    @observe("value")
    def _observe_value(self, change):
        self.value_computing = False

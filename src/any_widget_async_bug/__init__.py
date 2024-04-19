import importlib.metadata
import pathlib
import time

import anywidget
import traitlets
from traitlets import Int, Bool

try:
    __version__ = importlib.metadata.version("any_widget_async_bug")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"


class BugWidget(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "static" / "widget.js"
    _css = pathlib.Path(__file__).parent / "static" / "widget.css"

    value = Int(0).tag(sync=True)
    value_computing = Bool(False).tag(sync=True)

    def compute_value(self):
        self.value_computing = True
        self.send({"event_name": "compute_value"})
        while self.value_computing:
            time.sleep(0.1)
        return self.value

import importlib.metadata
import pathlib

import anywidget
import traitlets
from traitlets import Int

try:
    __version__ = importlib.metadata.version("any_widget_async_bug")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"


class BugWidget(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "static" / "widget.js"
    _css = pathlib.Path(__file__).parent / "static" / "widget.css"

    value = Int(0).tag(sync=True)

    def compute_value(self):
        self.send({"event_name": "compute_value"})

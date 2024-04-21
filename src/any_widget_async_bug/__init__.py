import importlib.metadata
import pathlib

import anywidget
from traitlets import Int
from IPython import get_ipython
from inspect import isawaitable

try:
    __version__ = importlib.metadata.version("any_widget_async_bug")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"


class BugWidget(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "static" / "widget.js"
    _css = pathlib.Path(__file__).parent / "static" / "widget.css"

    value = Int(0).tag(sync=True)

    async def compute_value(self):
        self.send({"event_name": "compute_value"})
        kernel = get_ipython().kernel
        try:
            end_of_cell = kernel.do_one_iteration()
            if isawaitable(end_of_cell):
                await end_of_cell
        except Exception:
            return
        finally:
            kernel.set_parent(kernel._parent_ident,
                              kernel.get_parent())

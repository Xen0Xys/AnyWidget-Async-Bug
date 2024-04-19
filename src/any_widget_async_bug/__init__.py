import asyncio
import importlib.metadata
import pathlib
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
    value_event = asyncio.Event()

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.on_msg(self._on_custom_message)

    async def compute_value(self):
        self.value_event.clear()
        self.send({"event_name": "compute_value"})
        await self.value_event.wait()
        return self.value

    @observe("value")
    def _value_changed(self, change):
        self.value_event.set()

    def _on_custom_message(self, model, message, list_of_buffers):
        event_type = message["event_type"]
        message_content = message["content"]
        if event_type == "value_computed":
            self.value_event.set()

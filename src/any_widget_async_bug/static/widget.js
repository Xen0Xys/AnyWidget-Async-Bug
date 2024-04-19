/** @typedef {{ value: number }} Model */

/** @type {import("npm:@anywidget/types").Render<Model>} */
function render({ model, el }) {
  model.on("msg:custom", (msg) => {
    switch (msg["event_name"]) {
      case "compute_value":
        model.set("value", model.get("value") + 1);
        model.save_changes();
    }
  })
}

export default { render };

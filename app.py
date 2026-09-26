from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
from navigation import CAMPUS_GRAPH, shortest_path
from visual_localizer import VisualLocalizer

app = Flask(__name__)
localizer = VisualLocalizer("reference_images")

@app.route("/")
def index():
    return render_template("index.html", nodes=list(CAMPUS_GRAPH.keys()))

@app.post("/localize")
def localize():
    if "image" not in request.files:
        return jsonify({"error": "No image supplied"}), 400
    data = np.frombuffer(request.files["image"].read(), np.uint8)
    image = cv2.imdecode(data, cv2.IMREAD_COLOR)
    if image is None:
        return jsonify({"error": "Could not decode image"}), 400
    return jsonify(localizer.localize(image))

@app.post("/route")
def route():
    body = request.get_json(silent=True) or {}
    start, destination = body.get("start"), body.get("destination")
    if start not in CAMPUS_GRAPH or destination not in CAMPUS_GRAPH:
        return jsonify({"error": "Unknown start or destination"}), 400
    return jsonify(shortest_path(CAMPUS_GRAPH, start, destination))

@app.get("/map")
def campus_map():
    return jsonify({
        "nodes": CAMPUS_GRAPH,
        "edges": [
            {"from": a, "to": b, "distance": w}
            for a, neighbours in CAMPUS_GRAPH.items()
            for b, w in neighbours.items() if a < b
        ]
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

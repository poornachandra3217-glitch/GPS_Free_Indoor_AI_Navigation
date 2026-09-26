# GPS-Free Indoor AI Navigation

A local, API-free prototype for indoor navigation using visual localization and graph-based routing.

## Features
- GPS-free indoor positioning from a camera/reference image
- OpenCV ORB feature matching
- Confidence scoring
- Dijkstra shortest-path navigation
- Browser interface with webcam capture or image upload
- No cloud API and no database required

## Install
Python 3.10+
```bash
pip install -r requirements.txt
```

## Run
```bash
python app.py
```
Open http://127.0.0.1:5000

## Real deployment
Put reference photos in `reference_images/`. Filename must match a navigation node:
`entrance.jpg`, `library.jpg`, `block_b.jpg`, etc.

Collect multiple images per location for better robustness. This prototype is for demonstration and research, not safety-critical navigation.

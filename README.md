# 🚀 GPS-Free Indoor AI Navigation

> A computer-vision and graph-based indoor navigation prototype designed to help users navigate complex indoor environments without depending on traditional GPS.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![AI/ML](https://img.shields.io/badge/AI%2FML-Computer%20Vision-purple)
![Algorithms](https://img.shields.io/badge/Algorithms-Dijkstra-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Prototype-informational)

---

## 📌 Overview

**GPS-Free Indoor AI Navigation** is a prototype that explores how **Computer Vision, Artificial Intelligence, and Graph Algorithms** can be combined to solve indoor navigation problems.

GPS-based navigation is highly effective in outdoor environments, but GPS signals can become weak, inaccurate, or unavailable inside large buildings. Places such as:

- 🏫 Colleges and universities
- 🏥 Hospitals
- ✈️ Airports
- 🛍️ Shopping malls
- 🏢 Office buildings
- 🏨 Hotels
- 🏛️ Museums and public buildings

often contain multiple floors, corridors, rooms, entrances, and intersections, making navigation difficult for first-time visitors.

This project explores a different approach: **identify or recognize indoor locations using visual information and use a graph representation of the building to calculate a route between locations.**

The project is intended as an educational and experimental prototype and provides a foundation for future real-time indoor navigation systems.

---

## 🎯 Problem Statement

Traditional GPS navigation depends on satellite signals and works best in open outdoor environments.

Inside buildings, several challenges can occur:

- GPS signals may be weak or unavailable.
- Indoor maps may not contain detailed room-level information.
- Large buildings can have many intersections and decision points.
- Users may not know which corridor, floor, or entrance to take.
- Static directions may become less useful when a user takes a wrong turn.
- Indoor navigation requires understanding the structure of the building rather than only geographic coordinates.

### 💡 Our Goal

To build a prototype that can:

1. Understand an indoor environment using visual information.
2. Identify relevant indoor locations or landmarks.
3. Represent the indoor environment as a graph.
4. Find a route between a source and destination.
5. Provide the calculated route through a simple application interface.
6. Create a foundation for future real-time navigation features.

---

# 🧠 Core Idea

The project combines three major concepts:

```text
                ┌─────────────────────┐
                │   User / Camera     │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   Computer Vision   │
                │      / AI Layer     │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Indoor Location /   │
                │ Landmark Detection  │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   Building Graph    │
                │ Nodes + Connections  │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Dijkstra Algorithm  │
                │ Route Calculation   │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   Flask Application  │
                │   / Navigation UI   │
                └─────────────────────┘
```

### 1. Computer Vision

Visual information can be processed using **OpenCV** to extract useful information from images or frames.

### 2. Location Recognition

The vision layer can be used to identify visual characteristics, landmarks, signs, rooms, or other useful indoor references.

### 3. Graph Representation

The building can be represented as a graph:

- **Nodes** → rooms, corridors, intersections, stairs, entrances, landmarks
- **Edges** → paths connecting two nodes
- **Weights** → distance, estimated travel cost, or another routing metric

### 4. Route Optimization

A shortest-path algorithm such as **Dijkstra's Algorithm** can calculate an efficient route between two nodes.

### 5. Flask Application

Flask provides a lightweight backend through which the navigation logic can be connected to a web interface.

---

# ✨ Key Features

## 🗺️ Indoor Route Planning

The system can model an indoor environment as a graph and calculate a route from a source location to a destination.

## 👁️ Computer Vision Integration

OpenCV provides the computer-vision layer required for processing indoor visual information.

## 🧭 GPS-Free Concept

The project focuses on indoor navigation without making traditional GPS the primary positioning mechanism.

## 🧮 Dijkstra's Shortest Path

Dijkstra's algorithm can be used to calculate the shortest/lowest-cost path across the indoor graph when edge weights are non-negative.

## 🌐 Flask Backend

A Flask-based application layer provides a simple way to connect the navigation logic with a web interface or API.

## 🧩 Modular Architecture

The project can be extended by adding:

- More computer-vision models
- More indoor locations
- Multiple floors
- Dynamic route updates
- User tracking
- Wrong-turn detection
- Real-time camera input

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Main programming language |
| 👁️ OpenCV | Computer vision and image processing |
| 🤖 AI/ML | Visual recognition and intelligent navigation concepts |
| 🧮 Dijkstra's Algorithm | Shortest-path calculation |
| 🌐 Flask | Backend/web application layer |
| 📊 Graph Algorithms | Indoor map representation and routing |
| 💻 HTML/CSS/JS | Optional web interface layer |

---

# 🏗️ Project Architecture

A high-level architecture can be represented as:

```text
                    ┌──────────────────┐
                    │      User        │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Camera / Image   │
                    │      Input       │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ OpenCV / Vision  │
                    │    Processing    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Location /       │
                    │ Landmark Info    │
                    └────────┬─────────┘
                             │
                             ▼
              ┌──────────────────────────────┐
              │      Indoor Graph            │
              │                              │
              │  Node ── Edge ── Node        │
              │    │              │          │
              │  Node ── Edge ── Node        │
              └────────────┬─────────────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Dijkstra / Route │
                  │    Calculation    │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Flask Backend     │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Navigation Result │
                  └──────────────────┘
```

---

# 🧮 Graph-Based Navigation

One of the important parts of this project is representing an indoor environment as a graph.

For example:

```text
Entrance
   |
   v
Lobby
 /   \
v     v
A     B
|     |
v     v
C --- D
     |
     v
Destination
```

Each location can be represented as a node.

Example:

```python
graph = {
    "Entrance": {"Lobby": 5},
    "Lobby": {"Entrance": 5, "Room A": 10, "Room B": 8},
    "Room A": {"Lobby": 10, "Room C": 6},
    "Room B": {"Lobby": 8, "Room D": 7},
    "Room C": {"Room A": 6, "Room D": 4},
    "Room D": {"Room B": 7, "Room C": 4, "Destination": 5},
    "Destination": {"Room D": 5}
}
```

The edge weights can represent:

- Distance
- Estimated walking time
- Number of steps
- Navigation cost
- Accessibility cost

---

# 🔎 Dijkstra's Algorithm

The project uses the concept of **Dijkstra's shortest-path algorithm** for route calculation.

Given a source and destination, Dijkstra's algorithm:

1. Starts from the source node.
2. Assigns a distance of `0` to the source.
3. Assigns infinity to other nodes.
4. Selects the unvisited node with the smallest known distance.
5. Updates neighboring nodes.
6. Repeats until the destination is reached or all reachable nodes are processed.
7. Reconstructs the route.

### Example

```text
Start
  |
  | 5
  v
Lobby
 /   \
3     8
v     v
A     B
 \     /
  4   2
   \ /
    v
   End
```

The algorithm evaluates the available paths and selects the lowest-cost route according to the graph weights.

---

# 👁️ Computer Vision Component

Computer vision is an important part of the project's future-ready architecture.

OpenCV can be used for tasks such as:

- Image loading
- Image preprocessing
- Frame processing
- Feature extraction
- Object/landmark detection
- Visual comparison
- Camera input processing

A future implementation can extend this layer using modern vision models for more robust indoor localization.

### Potential visual landmarks

Examples include:

- Room signs
- Building signs
- Door numbers
- Corridor markers
- Staircases
- Elevators
- Reception desks
- Distinctive architectural features

---

# 🌐 Flask Layer

Flask can act as the bridge between the user interface and the Python navigation system.

A possible request flow is:

```text
Browser
   │
   │ Request
   ▼
Flask Server
   │
   ├── Location Recognition
   │
   ├── Graph Processing
   │
   └── Route Calculation
   │
   ▼
Navigation Result
   │
   ▼
Browser
```

Example Flask structure:

```text
project/
│
├── app.py
├── navigation/
│   ├── graph.py
│   └── dijkstra.py
│
├── vision/
│   └── vision.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

The exact structure may vary depending on the implementation.

---

# 📁 Suggested Project Structure

```text
GPS_Free_Indoor_AI_Navigation/
│
├── app.py
│
├── requirements.txt
│
├── README.md
│
├── .gitignore
│
├── data/
│   ├── maps/
│   ├── images/
│   └── locations/
│
├── vision/
│   ├── __init__.py
│   └── vision.py
│
├── navigation/
│   ├── __init__.py
│   ├── graph.py
│   └── dijkstra.py
│
├── templates/
│   └── index.html
│
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

> The actual repository structure may differ. This layout is a recommended organization for extending the project.

---

# ⚙️ Installation

## Prerequisites

Before running the project, install:

- Python 3.x
- Git
- VS Code
- A modern web browser

Check Python:

```bash
python --version
```

Check Git:

```bash
git --version
```

---

# 📥 Clone the Repository

```bash
git clone https://github.com/poornachandra3217-glitch/GPS_Free_Indoor_AI_Navigation.git
```

Move into the project directory:

```bash
cd GPS_Free_Indoor_AI_Navigation
```

---

# 🧪 Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

# 📦 Install Dependencies

If the project contains a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Typical dependencies may include:

```text
opencv-python
flask
numpy
```

Only install packages actually required by the current implementation.

---

# ▶️ Run the Application

If the Flask entry point is `app.py`:

```bash
python app.py
```

Flask will normally display a local URL such as:

```text
http://127.0.0.1:5000/
```

Open that address in your browser.

---

# 🖥️ Example Workflow

A typical navigation workflow can look like this:

```text
1. User opens the application
          ↓
2. User selects / provides a destination
          ↓
3. System receives visual or location information
          ↓
4. Computer vision processes the input
          ↓
5. Current indoor location is determined
          ↓
6. Indoor graph is loaded
          ↓
7. Dijkstra calculates a route
          ↓
8. Route is returned
          ↓
9. User receives navigation instructions
```

---

# 🧪 Testing

The project should be tested using different indoor scenarios.

### Basic Tests

- Valid source and destination
- Source equals destination
- Destination exists
- Destination does not exist
- No available route
- Multiple possible routes
- Different edge weights

### Computer Vision Tests

- Different lighting conditions
- Different camera angles
- Partial visibility
- Similar-looking locations
- Different image resolutions

### Navigation Tests

- Short route
- Long route
- Multiple intersections
- Multiple floors
- Blocked paths
- Alternative routes

---

# 📊 Performance Considerations

The performance of the complete system depends on several components:

- Image resolution
- Computer-vision model complexity
- Number of graph nodes
- Number of graph edges
- Frequency of location updates
- Hardware capabilities
- Number of simultaneous users

For larger buildings, the graph can be optimized or divided into smaller sections such as:

```text
Building
├── Ground Floor
├── First Floor
├── Second Floor
└── Third Floor
```

Stairs and elevators can then be represented as connections between floors.

---

# 🏢 Multi-Floor Navigation

A future version can represent multiple floors in a single graph.

Example:

```text
             ┌───────────────┐
             │   Floor 2     │
             │ Room 201      │
             └───────┬───────┘
                     │
                 Elevator
                     │
             ┌───────▼───────┐
             │   Floor 1     │
             │ Room 101      │
             └───────┬───────┘
                     │
                  Stairs
                     │
             ┌───────▼───────┐
             │  Ground Floor │
             │    Entrance   │
             └───────────────┘
```

This would allow the system to calculate routes involving:

- Corridors
- Stairs
- Elevators
- Multiple floors
- Different entrances

---

# 🔐 Privacy Considerations

If camera-based navigation is extended into a real-world deployment, privacy should be treated as a core requirement.

Important considerations include:

- Avoid unnecessary storage of camera footage.
- Process data locally where practical.
- Clearly communicate when camera access is active.
- Avoid collecting personally identifiable information unnecessarily.
- Protect any stored location or navigation data.
- Obtain appropriate permissions before deploying cameras in real buildings.

This project is a prototype and should not be treated as a production security or surveillance system.

---

# ⚠️ Current Limitations

As a prototype, the project has several limitations.

### Indoor Localization

Accurate real-time indoor localization is significantly more difficult than simple GPS positioning.

### Visual Conditions

Computer-vision performance can be affected by:

- Lighting
- Camera quality
- Occlusion
- Motion blur
- Similar-looking areas
- Changes in the environment

### Static Maps

A graph created from a static building map may not automatically know about:

- Closed corridors
- Construction
- Temporary obstacles
- Crowded areas
- Locked rooms

### Real-Time Recalculation

A fully production-ready system would require continuous location updates and dynamic route recalculation.

---

# 🚀 Future Enhancements

The project can be extended significantly.

## 1. 📍 Real-Time Visual Localization

Use camera frames to continuously estimate the user's indoor location.

## 2. 🔄 Intelligent Route Recalculation

If the user deviates from the calculated route, automatically calculate a new route.

## 3. ⚠️ Wrong-Turn Detection

Detect when the user moves away from the expected path.

## 4. 🧠 Advanced AI Models

Integrate more advanced computer-vision and machine-learning models for improved localization.

## 5. 🏢 Multi-Floor Support

Support buildings with multiple floors, elevators, and staircases.

## 6. ♿ Accessibility-Aware Navigation

Allow users to select routes based on accessibility requirements, such as avoiding stairs.

## 7. 🚶 Walking-Time Estimation

Estimate travel time based on:

- Distance
- Walking speed
- Floor changes
- Route complexity

## 8. 🚧 Dynamic Obstacles

Allow the system to account for temporary blocked paths.

## 9. 📱 Mobile Application

Create Android/iOS interfaces for practical navigation.

## 10. 🗣️ Voice Navigation

Provide instructions such as:

```text
"Walk straight for 20 meters."
"Turn left at the corridor."
"Take the elevator to Floor 2."
"Your destination is on the right."
```

## 11. 🧭 AR Navigation

A future version could display directional arrows over the camera view using augmented reality.

---

# 🧪 Possible Future System

The long-term architecture could become:

```text
                 Smartphone Camera
                        │
                        ▼
              ┌──────────────────┐
              │ Computer Vision  │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ Visual Localizer │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ Indoor Map/Graph │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ Route Optimizer  │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ Wrong-Turn Check │
              └────────┬─────────┘
                       │
              ┌────────▼─────────┐
              │ Route Recalculate│
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ Voice / AR Guide │
              └──────────────────┘
```

---

# 🎓 Learning Outcomes

Building this project provided practical exposure to:

- Python programming
- Computer vision
- OpenCV
- Artificial intelligence concepts
- Graph data structures
- Shortest-path algorithms
- Dijkstra's algorithm
- Flask development
- Backend architecture
- Problem solving
- Debugging
- Testing
- System design
- Git and GitHub
- Team collaboration

The project also helped connect **algorithmic concepts with a real-world software problem**.

---

# 🤝 Team & Collaboration

This project was developed as a collaborative learning project.

### Contributors

- **Poorna Chandra Manupati** — [GitHub](https://github.com/poornachandra3217-glitch)
- **[Friend's Name]** — [GitHub/Profile Link]

### Contributions

Depending on the final implementation, team members can contribute across areas such as:

- Problem research
- System design
- Computer vision
- Graph implementation
- Backend development
- Testing
- Debugging
- Documentation
- UI development

> Update this section with the actual names, GitHub profiles, and contributions of all team members.

---

# 📸 Screenshots

Add project screenshots here:

```markdown
![Home Page](screenshots/home.png)

![Navigation](screenshots/navigation.png)

![Route Result](screenshots/route.png)
```

Recommended screenshots:

1. Application home page
2. Location selection
3. Indoor map
4. Route calculation
5. Computer-vision result
6. Final navigation screen

---

# 🎥 Demo

Add your project demonstration video here:

```markdown
[▶️ Watch the Project Demo](YOUR_VIDEO_LINK)
```

You can also add a GIF:

```markdown
![Project Demo](screenshots/demo.gif)
```

---

# 📚 Concepts Used

### Artificial Intelligence

Using intelligent methods to interpret visual/environmental information.

### Computer Vision

Processing images and camera data to extract useful information about an indoor environment.

### Graph Theory

Representing buildings as connected nodes and edges.

### Shortest Path

Finding an efficient route between two locations.

### Dijkstra's Algorithm

Computing shortest paths in a weighted graph with non-negative edge weights.

### Web Development

Connecting the Python navigation system to a web application using Flask.

---

# 🔗 Repository

GitHub:

https://github.com/poornachandra3217-glitch/GPS_Free_Indoor_AI_Navigation

---

# 📜 License

This project is released under the **MIT License**.

You may adapt the license depending on the actual requirements of the project and team.

---

# ⭐ Support

If you find this project useful or interesting:

⭐ Star the repository  
🍴 Fork the project  
🐛 Report issues  
💡 Suggest improvements  
🤝 Contribute to the project  

---

# 📌 Project Status

**Current Status:** 🚧 Prototype / Academic Project

The current implementation focuses on demonstrating the core concepts of GPS-free indoor navigation using computer vision, graph-based routing, and a Flask application.

Future versions may improve real-time localization, route recalculation, multi-floor support, accessibility, and AI-based navigation.

---

## 💭 Final Note

GPS-Free Indoor AI Navigation started with a simple question:

> **"How can we help people navigate complex indoor environments when traditional GPS is not reliable?"**

This project is our exploration of that problem using **Computer Vision + AI + Graph Algorithms + Web Technologies**.

It is not just about building a navigation system — it is about learning how to take a real-world problem, break it into smaller technical problems, design a solution, implement it, test it, and continuously improve it.

🚀 **Built to learn. Built to solve. Built to improve.**

---

### 🔥 Keywords

`Indoor Navigation` `GPS-Free Navigation` `Artificial Intelligence` `Computer Vision` `OpenCV` `Python` `Machine Learning` `Graph Algorithms` `Dijkstra` `Shortest Path` `Flask` `Indoor Localization` `AI Navigation` `Software Engineering` `Student Project` `CSE Project`

# ⚙️ ForgeAI Engine — Multimodal Industrial Operations Hub

A multimodal AI dashboard designed for industrial maintenance — integrating real-time computer vision with semantic document retrieval.
   
🔗 **Try it live** → *(Hosted on Streamlit Community Cloud)*

---

## What this is

Most industrial monitoring tools are fragmented: separate systems for machine logs, separate binders for manuals, and manual visual inspections prone to human error. ForgeAI isn't that.

This platform unifies two core capabilities into a single cohesive interface—**Vision Core** (YOLOv8-powered real-time component detection) and **Knowledge Core** (LangChain-powered RAG pipeline querying technical Fadal hardware documentation).

### Core Engine Pillars
| Pillar | What it means |
| :--- | :--- |
| 🟢 **Vision Core** | Real-time identification and snapshot verification of industrial components |
| 🟢 **Knowledge Core** | Semantic RAG pipeline querying technical Fadal CNC manuals instantly |
| 🔵 **Smart Context** | Automated system context triggers based on live visual detections |
| 💬 **Manual Override** | Built-in conversational chat interface for specific maintenance queries |

The interface renders your system status dynamically with a custom dark-mode radial gradient and glassmorphic panels, making system states and diagnostics visible at a glance.

---

## Table of contents

* Quickstart
* How it works
* Architecture
* Project structure
* Design decisions
* What's deliberately left out
* Extensibility
* License

---

## Quickstart

ForgeAI runs seamlessly on local environments or air-gapped Windows setups.

### Prerequisites
* Python 3.10+
* Git

### macOS / Linux / Windows (cmd.exe)
```bash
git clone [https://github.com/sa7028894-arch/forge-ai.git](https://github.com/sa7028894-arch/forge-ai.git)
cd forge-ai
pip install -r requirements.txt
python -m streamlit run app.py


How it works
Vision Inspection: Upload a component snapshot (JPG, PNG up to 200MB). The YOLOv8 vision pipeline evaluates the component against trained industrial datasets.

Contextual RAG: The system indexes local documentation (data/manual.pdf) via LangChain and ChromaDB to extract precise troubleshooting steps.

Unified Interface: The Streamlit frontend processes inputs, rendering diagnostic logs, confidence scores, and real-time chat responses inside a polished glassmorphism dashboard.

Architecture
[ User Input / Snapshot ] 
        │
        ▼
┌───────────────────────────────────────────────┐
│              Streamlit Frontend               │
│    (Custom CSS Glassmorphism Dark Theme)      │
└───────┬───────────────────────────────┬───────┘
        │                               │
        ▼                               ▼
┌───────────────┐               ┌───────────────┐
│  Vision Core  │               │Knowledge Core │
│   (YOLOv8)    │               │ (LangChain)   │
└───────────────┘               └───────────────┘


Project structure

Plaintext

forge-ai/
├── app.py                      # Main Streamlit dashboard & UI logic
├── requirements.txt            # Python dependencies (Streamlit, LangChain, YOLO, etc.)
├── data/
│   └── manual.pdf              # Fadal CNC hardware & operations manual
├── datasets/
│   └── fadal_parts/
│       └── train/              # Training images for component inspection
├── images/
│   ├── fadal_01.jpg            # Reference component snapshots
│   ├── fadal_02.jpg
│   ├── fadal_03.jpg
│   └── fadal_04.jpg
├── LICENSE
└── README.md


Design decisions


Why Streamlit? Allows rapid iteration of data-heavy Python applications into polished dashboards with minimal boilerplate code.

Why YOLOv8 + LangChain? Combining computer vision with generative retrieval provides a comprehensive end-to-end assistant for physical machinery maintenance.

Why Custom Glassmorphism CSS? Industrial dashboards require high-contrast dark modes to reduce eye strain in workshop or low-light control room environments.

What's deliberately left out
No cloud user authentication or multi-tenant database layers — scope is focused on local or air-gapped machine deployment.

No heavy external vector database servers (runs lightweight local embeddings for instant setup).

Extensibility


The modular structure of app.py allows swapping out target domains easily. Replacing the PDF in data/ and retraining the YOLO weights in datasets/ is enough to retarget the system to a completely different industrial machine or hardware model.

License

MIT — see LICENSE for details.
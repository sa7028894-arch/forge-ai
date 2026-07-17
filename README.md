# ForgeAI: Multimodal Industrial Operations Hub 
 
ForgeAI is a multimodal AI dashboard designed for industrial maintenance, integrating real-time computer vision with semantic document retrieval. 
 
## Features 
* **Vision Core:** Utilizes YOLOv8 for real-time identification of industrial components. 
* **Knowledge Core:** A RAG (Retrieval-Augmented Generation) pipeline using LangChain to query technical Fadal hardware manuals. 
* **Smart Interaction:** Automated system context triggers based on visual detection. 
* **Manual Override:** A built-in chat interface for specific technical queries. 
 
## Tech Stack 
* **Language:** Python 
* **Frontend:** Streamlit 
* **Vision:** YOLOv8 
* **AI/LLM:** LangChain, ChromaDB 
 
## How to Run 
1. Clone the repository: `git clone https://github.com/sa7028894-arch/forge-ai.git` 
2. Install requirements: `pip install -r requirements.txt` 
3. Launch the app: `python -m streamlit run app.py` 

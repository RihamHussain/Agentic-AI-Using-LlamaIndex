# 🚀 Agentic AI Using LlamaIndex, Gemini, and Tavily

*A lightweight agent with web search, memory, and streaming capabilities.*

---

## 📌 Overview

This project demonstrates how to build an **Agentic AI system** using:

* **Google Gemini 2.0 Flash** (via LlamaIndex)
* **Tavily Web Search** for real-time information
* **LlamaIndex AgentWorkflow** for tool use + memory
* **Short-term memory** inside the workflow context
* **Long-term memory** persisted to disk
* **Streaming responses** for interactive output

The agent can search the internet, remember user facts, reload that memory later, and respond intelligently using Gemini.

---

## 📦 Project Structure

```
AGENTIC-AI/
│── data/
│     └── memory.json            # Auto-generated long-term memory
│
│── src/
│     ├── .env                   # API keys (ignored by Git)
│     ├── check_models.py        # Lists available Gemini models
│     ├── long-term-memory.py    # Persistent memory (save & load)
│     ├── requirements.txt       # Project dependencies
│     ├── search-on-internet.py  # Web-enabled agent (Gemini + Tavily)
│     ├── short-term-memory.py   # Short-term memory using Context
│     ├── streaming.py           # Streaming token-by-token output
│     └── test-gemini.py         # Simple Gemini API test
│
│── .gitignore                   # Protects .env & memory.json
│── README.md                    # Project documentation
```

---

## 🔧 Features

### ✔️ Web Search (Tavily)

The agent can fetch live internet results using Tavily and then combine them with Gemini reasoning.
Implemented in:
`search-on-internet.py`

### ✔️ Short-Term Memory

The agent keeps memory inside the workflow context as long as the program is running.
Implemented in:
`short-term-memory.py`

### ✔️ Long-Term Memory

Context is exported → saved → reloaded later from `data/memory.json`.
Implemented in:
`long-term-memory.py`

### ✔️ Streaming Responses

Gemini responses are streamed token-by-token for a real assistant feel.
Implemented in:
`streaming.py`

### ✔️ Gemini Integration

Gemini 2.0 Flash is used for text generation and reasoning.
Tested via
`test-gemini.py` and `check_models.py`

---

## 🛠 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AGENTIC-AI.git
cd AGENTIC-AI
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r src/requirements.txt
```

---

## 🔑 Environment Variables

Inside `src/.env`, add:

```
GOOGLE_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Get keys from:

* Gemini API: [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)
* Tavily API: [https://app.tavily.com/](https://app.tavily.com/)

---

## ▶️ Running Each Module

### 1. Test Gemini

```bash
python src/test-gemini.py
```

### 2. List available Gemini models

```bash
python src/check_models.py
```

### 3. Agent with Web Search

```bash
python src/search-on-internet.py
```

### 4. Agent with Short-Term Memory

```bash
python src/short-term-memory.py
```

### 5. Agent with Long-Term Memory

```bash
python src/long-term-memory.py
```

### 6. Streamed Responses

```bash
python src/streaming.py
```

---

## 🧠 Memory System

### Short-Term

The workflow `Context` keeps conversation state per session.

### Long-Term

State is saved here:

```
data/memory.json
```

Which is then reloaded to restore the agent’s "personality" or memory.

---

## 🛡 Security

`.env` and `memory.json` are protected by `.gitignore`.
Never commit API keys or user data.
---

## 📬 Contact Me

If you'd like to connect, collaborate, or discuss AI, automation, and agentic systems, feel free to reach out:

🔗 **LinkedIn:** [Riham A. Hussain](https://www.linkedin.com/in/riham-a-hussain/)

---


# 🤖 Multi AI Agent

A powerful and customizable AI assistant platform built using **FastAPI**, **Streamlit**, **LangChain**, and **Groq**. This project allows users to create AI agents for specific domains such as **Finance**, **Healthcare**, **Education**, and more. It also fetches real-time information from the web using the **Tavily API**.

---

## 🚀 Features

- ✅ Create domain-specific AI agents with custom system prompts
- 🔍 Answer queries intelligently using Groq's language model
- 🌐 Real-time web data integration via Tavily API
- ⚙️ Backend powered by FastAPI and frontend built with Streamlit
- 🧠 Modular and scalable design with LangChain and LangGraph

---

## 🧰 Tech Stack

| Component     | Technology            |
|---------------|------------------------|
| Language Model | Groq API               |
| Real-Time Search | Tavily API           |
| Backend       | FastAPI                |
| Frontend      | Streamlit              |
| Frameworks    | LangChain, LangGraph   |
| Config        | python-dotenv          |

---

---

## 🔐 Setup Environment Variables

Create a `.env.local` file in the root directory and add your API keys:
```bash
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## 🛠️ Installation & Running

### 1. Clone the repository
```bash
git clone https://github.com/rahulbamnuya/Multi-AI-Agent-Project-.git
cd Multi-AI-Agent-Project-
```
### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate      # For Windows: venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
pip install -e .


```
### 4. Run Application
```bash
python ./app/main.py

```
## Example Use Case
💡 Example Use Case
Define your agent:
"You are a friendly financial advisor. Help users make safe investment decisions."

Ask:
"What are safe investment options for a beginner in 2025?"

✅ The agent will respond using Groq LLM and optionally retrieve real-time information from the web using Tavily.
---

## 🖼️ Screenshots

### 🎯 User Interface
<img src="Images/Screenshot 2025-08-03 232410.png" alt="Multi AI Agent UI" width="700"/>

### 📩 Sample Response
<img src="Images/Screenshot 2025-08-03 232522.png" alt="Multi AI Agent Output" width="700"/>

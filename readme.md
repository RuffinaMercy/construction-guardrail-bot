# 🏗️ Construction Assistant Chatbot

A **domain-restricted AI assistant for construction queries** that provides answers related to materials, cost estimation, building design, foundations, and safety practices.

The system integrates **LLMs, input validation pipelines, and AWS Guardrails** to ensure responses remain **relevant, safe, and domain-specific**.

🌐 **Live Demo:**
[https://construction-guardrail-bot.onrender.com](https://construction-guardrail-bot.onrender.com)

---

# 🚀 Features

* ✅ Domain-restricted chatbot (construction only)
* ✅ Input validation and filtering
* ✅ Query normalization (e.g., *RCC → Reinforced Cement Concrete*)
* ✅ AWS Bedrock Guardrails for safety
* ✅ LLM powered responses using **Groq + LLaMA 3**
* ✅ Interactive **Streamlit chat interface**
* ✅ Docker containerized application
* ✅ Cloud deployment

---

# 🧠 System Architecture

```
User Query
     │
     ▼
Input Validator
     │
     ▼
Query Normalizer
     │
     ▼
Domain Guard
     │
     ▼
AWS Bedrock Guardrail
     │
     ▼
LLM (Groq LLaMA 3)
     │
     ▼
Response Generator
     │
     ▼
Streamlit UI
```

---

# 📂 Project Structure

```
construction-guardrail-bot
│
├── src_2/
│   ├── chatbot.py
│   │
│   └── utils/
│       ├── validator.py
│       ├── normalizer.py
│       └── responder.py
│
├── ui_app.py
├── config.py
├── requirements.txt
├── Dockerfile
├── .env
├── .streamlit/
│   └── config.toml
│
└── README.md
```

---

# ⚙️ Local Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/RuffinaMercy/construction-guardrail-bot.git
cd construction-guardrail-bot
```

---

### 2️⃣ Create Virtual Environment

Windows

```
python -m venv venv
venv\Scripts\activate
```

Mac / Linux

```
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=llama-3.3-70b-versatile
MAX_ROWS_PER_FILE=20000
TOP_K=5
MIN_SIMILARITY=0.05
```

---

### 5️⃣ Run the Application

```
streamlit run ui_app.py
```

Open:

```
http://localhost:8501
```

---

# 🐳 Docker Setup

Build Docker Image

```
docker build -t construction-bot .
```

Run Container

```
docker run --env-file .env -p 8501:8501 construction-bot
```

Access application at:

```
http://localhost:8501
```

---

# ☁️ Cloud Deployment

This project is deployed using:

* **Docker containerization**
* **GitHub repository integration**
* **Render cloud hosting**

Live Application:

[https://construction-guardrail-bot.onrender.com](https://construction-guardrail-bot.onrender.com)

---

# 💬 Example Queries

You can ask questions like:

* What is RCC in construction?
* Estimate cement bags for a 10m × 8m slab.
* Which foundation is best for clay soil?
* Difference between hollow blocks and bricks.
* How to repair cracks in concrete walls?

---

# 🔒 Safety & Guardrails

The chatbot integrates **AWS Bedrock Guardrails** to ensure:

* Only construction-related queries are processed
* Unsafe or unrelated prompts are blocked
* Domain compliance is maintained

---

# 🛠 Tech Stack

* **Python**
* **Streamlit**
* **Groq API**
* **LLaMA 3**
* **AWS Bedrock Guardrails**
* **Docker**
* **Render Cloud**

---

# 📌 Learning Outcomes

This project demonstrates:

* Domain-restricted AI application design
* LLM integration with validation pipelines
* Guardrails for safe AI responses
* Docker containerization
* Cloud deployment of AI systems

---

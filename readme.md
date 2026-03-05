
# 🏗️ Construction Assistant Chatbot

A domain-restricted AI chatbot that answers **construction-related queries** using an LLM.  
Built with a modular architecture including **input validation, normalization, and response generation**.

---

## 🚀 Features

- ✅ Domain-specific chatbot (construction only)
- ✅ Query normalization (handles abbreviations like *rcc → reinforced concrete*)
- ✅ Input validation & filtering
- ✅ Clean Streamlit UI
- ✅ LLM-powered responses (Groq + LLaMA 3)

---

## 🧠 Architecture

User Input → Validator → Normalizer → Domain Check → LLM → Response

---

## 📁 Project Structure

```

project/
│
├── src_2/
│   ├── chatbot.py
│   ├── utils/
│   │   ├── normalizer.py
│   │   ├── validator.py
│   │   └── responder.py
│
├── ui_app.py
├── config.py
├── .env
├── requirements.txt
└── README.md

````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/construction-chatbot.git
cd construction-chatbot
````

---

### 2️⃣ Create Virtual Environment (venv)

#### 👉 Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### 👉 Mac / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create a `.env` file in the root folder:

```env
GROQ_API_KEY=your_api_key_here
```

---

### 5️⃣ Run the Application

```bash
streamlit run ui_app.py
```

---

## 💬 Example Queries

* "What is RCC?"
* "How to fix wall cracks?"
* "Estimate cost for building a house"
* "Best foundation for clay soil?"



---

## 🌟 Future Improvements

* Chat memory (context awareness)
* Cost estimation module




---

## 📌 Note

This project demonstrates:

* Domain-restricted AI system design
* Input validation pipelines
* Practical LLM integration



---

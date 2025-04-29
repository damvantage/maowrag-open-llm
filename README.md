# maowrag-open-llm
an open source LLM application using Ollama, Fastapi, langchain-ollama, streamlit to chat with local models.
## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/damvantage/maowrag-open-llm.git
cd maowrag-open-llm
```

### 2. (Optional) Create a virtual environment

- **On Unix/macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- **On Windows:**
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```

### 3. Install required dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

Create a `.env` file by copying the example file:

```bash
cp .env.example .env
```

Add your API keys:

```env
OLLAMA_BASE_URL=http://localhost:11434
BACKEND_API_URL=http://localhost:8000
```

---

## 🚀 Running the Application

### 1. Start the Ollama
#### Run Ollama with Docker

```bash
docker compose -f docker-compose.ollama.yaml up
```

- Ollama Host: [http://localhost:11434/](http://localhost:11434/)

Pull the open source LLM model

```bash
docker exec -i ollama ollama pull gemma3:1b-it-q4_K_M
```
#### Run Ollama from `https://ollama.com/`

after download ollama then pull model

```bash
ollama pull gemma3:1b-it-q4_K_M
```

### 2. Start the FastAPI Backend

```bash
uvicorn app_fastapi:app --host 0.0.0.0 --port 8000 --reload
```

- API Documentation: [http://localhost:8000/docs](http://localhost:8000/docs)

### 3. Start the Streamlit Frontend

```bash
streamlit run app_streamlit.py --server.port=8501 --server.address=0.0.0.0
```

- Access the UI: [http://localhost:8501](http://localhost:8501)

---

## 🐳 Run all service with Docker

### 1. Build Docker Images

```bash
docker-compose build
```

### 2. Start Docker Containers

```bash
docker-compose up
```

- FastAPI backend: [http://localhost:8000](http://localhost:8000)  
- Streamlit UI: [http://localhost:8501](http://localhost:8501)
- Ollama Host: [http://localhost:11434/](http://localhost:11434/)

### 3. Stop Containers

```bash
docker-compose down
```

---

## 🤝 Contributing

Have ideas or improvements?  
Feel free to fork the repo, create issues, or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.
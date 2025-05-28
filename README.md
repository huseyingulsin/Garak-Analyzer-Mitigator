# 🔬 Garak Analyzer & Mitigator

A lightweight web interface to upload, visualize, and mitigate adversarial prompt test results from [Garak](https://github.com/leondz/garak), a tool for red-teaming language models. This viewer allows you to inspect `.report.jsonl` output files, view statistics, analyze triggers, and generate system prompt mitigations using local or cloud LLMs (e.g., OpenAI, Gemini, Ollama).

---

## ✨ Features

- 📄 Upload `.report.jsonl` files from Garak
- 📊 View pass/fail attempts, probe statistics, and trigger matches
- 🛡️ Generate system prompt mitigations using LLMs
- 📥 Export annotated report to PDF
- 🔎 Live search & filtering
- 🖼️ Visual pipeline diagram

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/huseyingulsin/Garak-Analyzer-Mitigator.git
cd Garak-Analyzer-Mitigator
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python app.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

---

## 🛡️ Local Mitigation with Ollama

To use the **local mitigation option with Ollama**, follow these steps:

### 1. Install Ollama

Go to [https://ollama.com](https://ollama.com) and install Ollama for your OS.

### 2. Pull a Supported Model

Run one of the following in your terminal:

```bash
ollama pull llama3
# or
ollama pull mistral
```

> Make sure you have sufficient disk space and RAM available.

### 3. Run Ollama in the Background

```bash
ollama run llama3
```

This will start a local model server at `http://localhost:11434`.

### 4. Select "Ollama (Local)" in the Viewer UI

Use the dropdown in the web UI to select **“Ollama (Local)”** as your LLM provider. When you click "🛡️ Generate", it will query your local model.

---

## 📂 Project Structure

```
├── app.py                     # Flask app entrypoint
├── templates/
│   └── index.html             # Main UI template
├── static/
│   ├── style.css              # Optional styling
│   ├── script.js              # JS for modals and frontend logic
│   └── sample.report.jsonl    # Example file
├── requirements.txt           # Dependencies
├── README.md
└── .gitattributes             # GitHub language stats cleanup
```

---

## 🧪 Example File

A sample Garak report is included for demo purposes:

📄 `static/sample.report.jsonl`

Try uploading it via the web UI to see the viewer in action!

---

## 📜 License

MIT License © Hüseyin Gülsin

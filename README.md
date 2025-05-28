# 🧪 Garak Analyzer & Mitigator

Garak Analyzer & Mitigator is a web-based tool to analyze `.report.jsonl` output files from the [garak](https://github.com/leondz/garak) adversarial LLM probing framework. This viewer helps visualize probe results and generate prompt mitigations using local or cloud-based LLMs like Ollama, OpenAI, or Gemini.

---

## ✨ Features

- 📂 Upload `.report.jsonl` files directly from Garak
- 📊 View probe status, matched triggers, and outputs
- 🛡️ Generate mitigation prompts using LLMs (local/cloud)
- 📤 Export to PDF for easy sharing
- 🌐 Works locally via Flask, no external dependency required

---

## 📸 Demo Screenshots

### 🏠 Upload & Overview
![index view](static/index.png)

### 📋 Detailed Report Viewer
![report viewer](static/reportviewer.png)

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/huseyingulsin/Garak-Analyzer-Mitigator.git
cd Garak-Analyzer-Mitigator
```

### 2. (Optional) Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install requirements
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
python app.py
```

Then open `http://127.0.0.1:5000/` in your browser.

---

## 🧠 Local LLM Mitigation (Ollama)

If you choose "Ollama (Local)" as mitigation provider:

1. Install [Ollama](https://ollama.com/)
2. Pull a supported model (e.g., llama3):
   ```bash
   ollama pull llama3
   ```
3. Start Ollama in the background:
   ```bash
   ollama serve
   ```
4. The app will connect automatically when "Ollama" is selected.

---

## 📝 Sample Report

You can try the viewer with the example Garak report:

📄 [`sample.report.jsonl`](static/sample.report.jsonl)

---

## 🧾 License

MIT License

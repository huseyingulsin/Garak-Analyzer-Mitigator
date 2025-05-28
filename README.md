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

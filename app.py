from flask import Flask, render_template, request, make_response
from weasyprint import HTML
import json
from flask import jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", data=[], summary={}, evals=[])
@app.route('/garak-cheatsheet')
def garak_cheatsheet():
    return render_template('garak_cheatsheet.html')

@app.route('/ollama-guide')
def ollama_guide():
    return render_template('ollama_guide.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    attempts = []
    evals = []
    summary = {
        "total": 0,
        "success": 0,
        "fail": 0,
        "model": "Unknown",
        "probe_spec": "",
        "detector_spec": "",
        "run_id": ""
    }

    for line in file:
        entry = json.loads(line)

        if entry.get("entry_type") == "start_run setup":
            summary["model"] = entry.get("plugins.model_name", "")
            summary["probe_spec"] = entry.get("plugins.probe_spec", "")
            summary["detector_spec"] = entry.get("plugins.detector_spec", "")
            summary["run_id"] = entry.get("transient.run_id", "")

        elif entry.get("entry_type") == "eval":
            evals.append({
                "probe": entry.get("probe", ""),
                "passed": entry.get("passed", 0),
                "total": entry.get("total", 0),
                "rate": round(entry.get("passed", 0) / max(1, entry.get("total", 1)) * 100, 1)
            })

        elif entry.get("entry_type") == "attempt":
            outputs = entry.get("outputs", [])
            full_output = "\n\n".join(outputs)
            trigger = entry.get("notes", {}).get("settings", {}).get("attack_rogue_string", "")
            has_trigger = any(trigger.lower() in o.lower() for o in outputs) if trigger else False
            status = entry.get("status", 0)

            attempts.append({
                "uuid": entry.get("uuid", "")[:8],
                "probe": entry.get("probe_classname", ""),
                "prompt": entry.get("prompt", ""),
                "outputs": outputs,
                "output_full": full_output,
                "status": "Success" if status == 1 else "Fail",
                "trigger": trigger,
                "has_trigger": has_trigger
            })

            summary["total"] += 1
            if status == 1:
                summary["success"] += 1
            else:
                summary["fail"] += 1

    return render_template("index.html", data=attempts, summary=summary, evals=evals)

@app.route('/download_pdf', methods=['POST'])
def download_pdf():
    file = request.files['file']
    attempts = []
    evals = []
    summary = {
        "total": 0,
        "success": 0,
        "fail": 0,
        "model": "Unknown",
        "probe_spec": "",
        "detector_spec": "",
        "run_id": ""
    }

    for line in file:
        entry = json.loads(line)
        if entry.get("entry_type") == "start_run setup":
            summary["model"] = entry.get("plugins.model_name", "")
            summary["probe_spec"] = entry.get("plugins.probe_spec", "")
            summary["detector_spec"] = entry.get("plugins.detector_spec", "")
            summary["run_id"] = entry.get("transient.run_id", "")
        elif entry.get("entry_type") == "eval":
            evals.append({
                "probe": entry.get("probe", ""),
                "passed": entry.get("passed", 0),
                "total": entry.get("total", 0),
                "rate": round(entry.get("passed", 0) / max(1, entry.get("total", 1)) * 100, 1)
            })
        elif entry.get("entry_type") == "attempt":
            outputs = entry.get("outputs", [])
            full_output = "\n\n".join(outputs)
            trigger = entry.get("notes", {}).get("settings", {}).get("attack_rogue_string", "")
            has_trigger = any(trigger.lower() in o.lower() for o in outputs) if trigger else False
            status = entry.get("status", 0)
            attempts.append({
                "uuid": entry.get("uuid", "")[:8],
                "probe": entry.get("probe_classname", ""),
                "prompt": entry.get("prompt", ""),
                "outputs": outputs,
                "output_full": full_output,
                "status": "Success" if status == 1 else "Fail",
                "trigger": trigger,
                "has_trigger": has_trigger
            })
            summary["total"] += 1
            summary["success"] += 1 if status == 1 else 0
            summary["fail"] += 1 if status != 1 else 0

    rendered = render_template("pdf_template.html", data=attempts, summary=summary, evals=evals)
    pdf = HTML(string=rendered).write_pdf()
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=garak_report.pdf'
    return response

@app.route('/generate_mitigation', methods=['POST'])
def generate_mitigation():
    data = request.get_json()
    prompt_text = data.get("prompt")

    ollama_url = "http://localhost:11434/api/generate"
    model_name = "gemma3:4b"  # veya sen ne kurduysan
    payload = {
        "model": model_name,
        "prompt": f"""Given the following user prompt, generate a system prompt that would prevent a model from responding to it in a harmful way.

    User prompt:
    \"{prompt_text}\"

    The system prompt should begin with "You are an AI assistant..." and clearly describe how the model should avoid responding to harmful content.
    """,
        "system": "You are a helpful mitigation system. Your job is to output only a defensive system prompt.",
        "stream": False
    }


    try:
        response = requests.post(ollama_url, json=payload)
        response.raise_for_status()
        result = response.json()
        mitigation = result.get("response", "")
        return jsonify({"success": True, "mitigation": mitigation})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

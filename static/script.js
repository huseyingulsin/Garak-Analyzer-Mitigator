// Filter output table
function filterTable() {
    const input = document.getElementById("searchInput").value.toLowerCase();
    const rows = document.querySelectorAll("#attemptTable tbody tr");
    rows.forEach(row => {
        let matched = false;
        row.querySelectorAll("pre").forEach(pre => {
            if (pre.textContent.toLowerCase().includes(input)) matched = true;
        });
        row.style.display = matched ? "" : "none";
    });
}

// Modal open/close (works for both details & prevention)
window.openModal = function(id) {
    const modal = document.getElementById(id);
    if (modal) modal.style.display = 'block';
};

window.closeModal = function(id) {
    const modal = document.getElementById(id);
    if (modal) modal.style.display = 'none';
};

// Click outside to close
window.addEventListener('click', function (event) {
    document.querySelectorAll('.modal').forEach(modal => {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
});

// Dynamic form action (View vs PDF)
document.addEventListener("DOMContentLoaded", function () {
    let clickedButtonAction = null;

    document.querySelectorAll('#reportForm button[type="submit"]').forEach(btn => {
        btn.addEventListener('click', function () {
            clickedButtonAction = this.getAttribute("formaction");
        });
    });

    document.getElementById('reportForm').addEventListener('submit', function (e) {
        if (clickedButtonAction) {
            this.action = clickedButtonAction;
        } else {
            e.preventDefault();
            alert("Error: No valid action set. Try again.");
        }
    });
});

window.generatePrevention = function(index) {
    const provider = document.getElementById("providerSelect").value;
    const modalId = `prevent-modal-${index}`;
    const resultId = `generated-prevention-${index}`;
    const modal = document.getElementById(modalId);
    const resultBox = document.getElementById(resultId);

    modal.style.display = 'block';
    resultBox.innerHTML = `<strong>🔄 Asking <code>${provider}</code>...</strong>`;

    const prompt = document.querySelector(`#details-modal-${index} pre`).textContent;

    // Real request
    fetch('/generate_mitigation', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt: prompt })
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            resultBox.innerHTML = `
                <p><strong>Provider:</strong> ${provider}</p>
                <p><strong>Mitigation Prompt:</strong></p>
                <pre>${data.mitigation}</pre>
                <button onclick="retestPrompt(${index}, \`${prompt.replace(/`/g, "\\`")}\`, \`${data.mitigation.replace(/`/g, "\\`")}\`)">🔁 Retest</button>
            `;
        } else {
            resultBox.innerHTML = `<span style='color:red'>❌ Error: ${data.error}</span>`;
        }
    })
    .catch(err => {
        resultBox.innerHTML = `<span style='color:red'>❌ Fetch error: ${err.message}</span>`;
    });
};

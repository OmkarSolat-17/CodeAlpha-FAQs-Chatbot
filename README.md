# FAQ Chatbot (Task 2)

A lightweight, **AI‑powered FAQ chatbot** built for the **CodeAlpha AI internship**. The application demonstrates a pure‑Python information‑retrieval pipeline and a modern, responsive web UI.

---

## ✨ Features
- **Pure‑Python retrieval** – No external NLP libraries. Questions are tokenized, stop‑words are removed, and a TF‑IDF‑like vector is built on‑the‑fly.
- **Cosine‑similarity ranking** – Finds the most relevant FAQ entry from a JSON knowledge base.
- **Responsive UI** – Built with **Flask**, HTML, and a custom CSS theme that works on desktop and mobile.
- **Interactive chat** – Users can type questions, see bot replies, and use **Copy** and **Speak** actions on every answer.
- **New UI enhancements**:
  - Sidebar with brand, new‑chat button, and profile info.
  - Top‑bar tag indicating the chatbot is NLP‑powered.
  - Suggestion buttons for quick starter queries.
  - Typing indicator while the server processes the request.
- **Zero external dependencies** – Only Flask is required (listed in `requirements.txt`).

---

## 📖 Project Overview
The chatbot loads FAQs from `faqs.json`, builds TF‑IDF‑like vectors for each question, and answers incoming queries using cosine similarity. If the best match score is below a confidence threshold (0.2), the bot asks the user to re‑phrase.

---

## 📂 Repository Structure
```
├─ app.py               # Flask server + retrieval logic
├─ faqs.json            # FAQ data (question & answer pairs)
├─ requirements.txt     # Python dependencies (Flask)
├─ templates/
│   └─ index.html       # Main UI layout
├─ static/
│   └─ style.css        # Theme and responsive styles
└─ README.md            # This documentation
```

---

## 🚀 Getting Started
### Prerequisites
- Python 3.9+ (tested on Windows)
- Virtual environment (recommended)

### Installation
```bash
# Clone the repo (if you haven't already)
git clone https://github.com/OmkarSolat-17/CodeAlpha-FAQs-Chatbot.git
cd CodeAlpha-FAQs-Chatbot

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # Windows

# Install the only required package
python -m pip install -r requirements.txt
```

### Running the App
```bash
python app.py
```
The server starts in **debug mode** on `http://127.0.0.1:5000`. Open that URL in a browser to interact with the chatbot.

---

## 🛠️ Customisation
- **Add more FAQs** – Append new objects to `faqs.json` following the existing `{ "question": "...", "answer": "..." }` format.
- **Change the UI** – Edit `templates/index.html` or `static/style.css`. The stylesheet uses CSS variables for colours, making theme tweaks straightforward.
- **Adjust retrieval logic** – The tokenizer, stop‑word list, and similarity threshold are defined in `app.py`. Feel free to experiment with alternative weighting schemes.

---

## 🤝 Contributing
Contributions are welcome! Please fork the repo, make your changes, and open a pull request. Ensure that:
1. New code follows the existing pure‑Python approach (no heavy NLP libraries).
2. UI changes keep the responsive layout intact.
3. The README stays up‑to‑date with any new features.

---

## 📄 License
This project is licensed under the MIT License – see the `LICENSE` file for details.

# FAQ Chatbot (Task 2)

A lightweight FAQ chatbot built for the **CodeAlpha AI internship**. It:

- Loads a collection of frequently‑asked questions (FAQs) from a JSON file.
- Pre‑processes the questions with a tiny pure‑Python tokenizer and a small stop‑word list (no external NLP libraries).
- Represents each FAQ as a TF‑IDF‑like vector and finds the most similar FAQ using cosine similarity.
- Serves a minimal web UI built with **Flask**.
- **Enhancements:** each bot reply includes **Copy** and **Speak** buttons, and the UI is styled with a clean CSS file.

## How to run
```bash
# (Windows) Create a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate

# Install Flask (the only dependency)
python -m pip install -r requirements.txt

# Start the app
python app.py
```

Open a browser at `http://127.0.0.1:5000` and start asking questions.

## Project structure
- `app.py` – Flask server and FAQ matching logic (pure Python).
- `faqs.json` – List of FAQ entries (20+ items).
- `templates/index.html` – UI with copy/speak actions.
- `static/style.css` – Simple, modern styling.
- `README.md` – This document.

Feel free to extend `faqs.json` with more Q&A pairs or enhance the UI further.

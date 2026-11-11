import json
import os
import math
import re
from collections import Counter, defaultdict
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# ----------------------------------------------------------------------
# Load FAQs
# ----------------------------------------------------------------------
FAQ_PATH = os.path.join(os.path.dirname(__file__), "faqs.json")
with open(FAQ_PATH, "r", encoding="utf-8") as f:
    faqs = json.load(f)

questions = [item["question"] for item in faqs]
answers   = [item["answer"]   for item in faqs]

# ----------------------------------------------------------------------
# Simple tokenizer & stop‑word list (pure Python)
# ----------------------------------------------------------------------
_STOP_WORDS = {
    "the", "is", "at", "which", "on", "a", "an", "and", "or", "for", "to",
    "of", "in", "what", "how", "with", "i", "you", "we", "they", "my", "your"
}

def _tokenize(text: str):
    # keep only alphanumeric words, lower‑case, drop stop‑words
    words = re.findall(r"\b\w+\b", text.lower())
    return [w for w in words if w not in _STOP_WORDS]

# ----------------------------------------------------------------------
# Build TF‑IDF‑like vectors (no external libs)
# ----------------------------------------------------------------------
_doc_term_counts = []
_doc_lengths = []          # total token count per doc
_term_doc_freq = defaultdict(int)  # DF per term

for q in questions:
    tokens = _tokenize(q)
    cnt = Counter(tokens)
    _doc_term_counts.append(cnt)
    _doc_lengths.append(sum(cnt.values()))
    for term in cnt:
        _term_doc_freq[term] += 1

N = len(questions)  # number of documents


def _tf_idf_vector(term_counter):
    vec = {}
    doc_length = sum(term_counter.values())

    if doc_length == 0:
        return vec

    for term, tf in term_counter.items():
        df = _term_doc_freq[term]
        idf = math.log((N + 1) / (df + 1)) + 1
        vec[term] = (tf / doc_length) * idf

    return vec


question_vectors = [_tf_idf_vector(cnt) for cnt in _doc_term_counts]

def _cosine_similarity(vec1, vec2):
    intersect = set(vec1) & set(vec2)
    dot = sum(vec1[t] * vec2[t] for t in intersect)
    norm1 = math.sqrt(sum(v * v for v in vec1.values()))
    norm2 = math.sqrt(sum(v * v for v in vec2.values()))
    return dot / (norm1 * norm2) if norm1 and norm2 else 0.0

# ----------------------------------------------------------------------
# Routes
# ----------------------------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_q = data.get('question', '')
    if not user_q:
        return jsonify({'answer': 'Please provide a question.'})
    user_vec = _tf_idf_vector(Counter(_tokenize(user_q)))
    sims = [_cosine_similarity(user_vec, qv) for qv in question_vectors]
    best_idx = max(range(len(sims)), key=lambda i: sims[i])
    best_score = sims[best_idx]
    if best_score < 0.2:
        return jsonify({'answer': "I'm not sure about that. Please try rephrasing your question."})
    return jsonify({'answer': answers[best_idx]})

if __name__ == '__main__':
    app.run(debug=True)

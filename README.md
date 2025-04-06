```md
# 🛍️ Flipkart Review Sentiment Analysis

A web-based sentiment analysis app built using **Python**, **Flask**, and **NLTK's VADER** model. This tool allows users to input product reviews (like those on Flipkart) and instantly get feedback on the sentiment—**Positive**, **Negative**, or **Neutral**—along with a **visual representation** of the sentiment scores.


## 📌 Features

- ✅ Real-time sentiment classification using VADER (no training needed)
- 🖼️ Clean Bootstrap-based user interface
- 📊 Sentiment score bar chart powered by Chart.js
- 📝 Text pre-processing for accurate sentiment extraction
- 💡 Simple, lightweight, and works offline


## 🧠 How It Works

1. User enters a product review (text input).
2. The app uses **VADER (Valence Aware Dictionary for sEntiment Reasoning)** from NLTK to analyze the sentiment.
3. The result is displayed:
   - Dominant sentiment (😊 Positive, 😠 Negative, 🙂 Neutral)
   - Bar chart showing positive, negative, and neutral score values


## 📂 Project Structure


sentiment_app/
├── app.py                         # Flask app to handle routes and logic
├── vader_sentiment_analyzer.pkl  # Saved VADER model
├── templates/
│   └── index.html                 # UI with Bootstrap + Chart.js
├── static/                        # (Optional) For custom CSS/JS
└── README.md                      # Project overview



## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.7+
- pip (Python package manager)

### 📥 Installation

1. **Clone the repository**
```bash
git clone https://github.com/rajputpritesh1/flipkart-sentiment-analysis.git
cd flipkart-sentiment-analysis
```

2. **Create virtual environment (optional but recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the app**
```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## 💬 Sample Reviews

Use these in the app for testing:

```text
✅ "Absolutely loved the product! Great quality and quick delivery."
❌ "Worst product ever. It stopped working after two days."
😐 "The product is okay. Not bad, not amazing."
```


## 📦 Requirements

```
Flask
nltk
pickle
```

> You can generate this file using:
> ```bash
> pip freeze > requirements.txt
> ```

---


## 🙌 Acknowledgements

- [NLTK VADER Sentiment Analyzer](https://www.nltk.org/)
- [Chart.js](https://www.chartjs.org/)
- [Bootstrap](https://getbootstrap.com/)
- Flipkart dataset by [Aman Kharwal](https://github.com/amankharwal)

---

## 🔖 GitHub Topics

```
sentiment-analysis flask vader bootstrap chartjs nlp python text-classification review-analysis visualization webapp
```

---

## ⭐ Project Maintainer

**Pritesh Kumar** – [@rajputpritesh1](https://github.com/rajputpritesh1)
```

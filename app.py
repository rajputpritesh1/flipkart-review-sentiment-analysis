from flask import Flask, render_template, request
import pickle
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

with open("vader_sentiment_analyzer.pkl", "rb") as f:
    sentiments = pickle.load(f)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    scores = {"pos": 0, "neg": 0, "neu": 0}
    if request.method == 'POST':
        review = request.form['review']
        score = sentiments.polarity_scores(review)
        scores = {
            "pos": round(score['pos'], 3),
            "neg": round(score['neg'], 3),
            "neu": round(score['neu'], 3)
        }
        if (score['pos'] > score['neg']) and (score['pos'] > score['neu']):
            result = "Positive 😊"
        elif (score['neg'] > score['pos']) and (score['neg'] > score['neu']):
            result = "Negative 😠"
        else:
            result = "Neutral 🙂"

    return render_template("index.html", result=result, scores=scores)

if __name__ == '__main__':
    app.run(debug=True)

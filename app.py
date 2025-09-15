from flask import Flask, render_template
import datetime

app = Flask(__name__)

quotes = [
    "⚡ Time is running out, make today count!",
    "🚀 Small steps today become big achievements tomorrow.",
    "💪 Push yourself, because no one else will do it for you.",
    "🌱 Improve 1% every day—it adds up fast.",
    "🔥 Stop waiting. Start creating your future now.",
    "✨ Your goals won't wait—why should you?"
]

@app.route("/")
def home():
    today = datetime.datetime.now()
    index = today.timetuple().tm_yday % len(quotes)
    daily_quote = quotes[index]
    return render_template("index.html", daily_quote = daily_quote)

if __name__ == "__main__":
    app.run(debug=True)

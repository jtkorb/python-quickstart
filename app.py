from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    with open('data/products.json', encoding="utf-8") as f:
        data = json.load(f)

    return render_template('index.html', products=data)

if __name__ == "__main__":
    app.run(debug=True)
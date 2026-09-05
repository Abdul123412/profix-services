from flask import Flask, render_template
from collections import defaultdict

app = Flask(__name__)

workers = [
    {"name": "Redeemer Atsu", "job": "Plumber", "contact": "0544304526", "rating": "4.8"},
    {"name": "Abdul Mujib", "job": "Electrician", "contact": "0506351995", "rating": "5.0"},
    {"name": "Master Francis", "job": "Carpenter", "contact": "0240278488", "rating": "4.9"},   
    {"name": "Abdul Hamid", "job": "Painter", "contact": "0543333313", "rating": "4.6"},  
]

@app.route('/')
def home():
    grouped = defaultdict(list)
    for w in workers:
        grouped[w['job']].append(w)
    return render_template('index.html', jobs=grouped)

if __name__ == '__main__':
    app.run(debug=True)

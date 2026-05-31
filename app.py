from flask import Flask, render_template

app = Flask(__name__)

workers = [
    {"name": "Redeemer Atsu", "job": "Plumber", "contact": "0544304526", "rating": "4.8"},
    {"name": "Abdul Mujib", "job": "Electrician", "contact": "0506351995", "rating": "4.9"},
    {"name": "Master Francis", "job": "Carpenter", "contact": "0240278488", "rating": "4.7"},
    {"name": "Abdul Hamid", "job": "Painter", "contact": "0543333313", "rating": "4.6"}
]

@app.route('/')
def home():
    return render_template('index.html', workers=workers)

if __name__ == '__main__':
    app.run(debug=True)

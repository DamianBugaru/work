import os
import csv
from flask import Flask, request, render_template

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

def calculate_averages(filepath):
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        totals = {}
        counts = {}

        for row in reader:
            for key, value in row.items():
                try:
                    num = float(value)
                    totals[key] = totals.get(key, 0) + num
                    counts[key] = counts.get(key, 0) + 1
                except ValueError:
                    continue

        return {key: totals[key] / counts[key] for key in totals}

@app.route('/', methods=['GET', 'POST'])
def index():
    averages = None
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            averages = calculate_averages(filepath)
    return render_template('index.html', averages=averages)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)

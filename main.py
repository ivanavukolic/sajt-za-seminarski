from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('index.html')


@app.route('/input', methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('input.html')


@app.route('/output', methods=['GET', 'POST'])
def output():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('output.html')


if __name__ == "__main__":
    app.run(debug=True)

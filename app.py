from flask import Flask, send_from_directory, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('static', path)
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('dist', path)


if __name__ == '__main__':
    app.run()

from flask import Flask, render_template
import platform

app = Flask(__name__)


@app.route('/')
def index():
    url = "http://placekitten.com/200/300"
    hostname = platform.node()
    return render_template('index.html', url=url, hostname=hostname)


if __name__ == "__main__":
    app.run(host="0.0.0.0")

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

if __name__ == '__main__':
    app.run("0.0.0.0",debug=True)

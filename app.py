from flask import Flask

app = Flask(__name__)

VERSION = "1.0.0"

@app.route("/")
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Python Jenkins Project</title>
    </head>
    <body>
        <h1>MY NEW PYTHON OUTPUT</h1>

        <h2>Jenkins Build Successful</h2>
        <p>This website is running using Python Flask.</p>
        <p>GitHub → Jenkins → Python</p>
        <h3>Version: {VERSION}</h3>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

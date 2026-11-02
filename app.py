from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Python Jenkins Project</title>
    </head>
    <body>
        <h1>PYTHON FREESTYLE PROJECT</h1>
        <h2>Jenkins Build Successful</h2>
        <p>This website is running using Python Flask.</p>
        <p>GitHub → Jenkins → Python</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    

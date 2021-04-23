from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "O Gustavo é muito Feio. Patinho no FF, no Play, no snook, e tudo mais"

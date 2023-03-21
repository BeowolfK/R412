from flask import Flask
from time import strftime


app = Flask(__name__)

@app.route("/<name>")
def bonjour(name):
  return f"Bonjour {name.title()}! Il est {strftime('%H:%M:%S')}"

if __name__ == "__main__":
  app.run(debug = True)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def raiz():
  json = {"message": "Olá mundo"}

  return json

app.run()
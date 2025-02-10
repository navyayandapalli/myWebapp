from flask import Flask

app = Flask("MyFlaskapp")

@app.route('/')
def home():
    return "Hello, Flask is running!"
  app.run(host='0.0.0.0', port=5000)

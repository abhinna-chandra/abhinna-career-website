from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "Hello Abhinna!"

  print(__name__)
  if __name__ == "__main__":
    print("I am inside loop.")

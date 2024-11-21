from flask import Flask
from web_app import pages
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8000, debug=True)

print(pages.about)
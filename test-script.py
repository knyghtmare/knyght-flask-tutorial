from flask import Flask

app = Flask( __name__ )


@app.route("/home")
def home():
    return "<h1>Hello!</h1> This is the main page."


if __name__ == "__main__":
    app.run()

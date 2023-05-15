from flask import Flask, request

app = Flask(__name__)



@app.route("/")
def index():
    return "Ok"

@app.route("/hello/<name>")
def hello(name):
    return f"Hello {name}"

@app.route("/login", methods=["POST"])
def login():
    print(request.method)
    print(request.json)
    return "Ok"


if __name__ == '__main__':  # se asigura ca aplicatia ruleaza doar rutele scrise din acest fisier. daca este rulat din alt fisier nu va functiona
    app.run(debug=True)




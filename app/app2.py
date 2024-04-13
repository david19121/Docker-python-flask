from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World welcome to my world!</p>"

@app.get("/health")

def health():
    return {"status up"}
    
@app.route("/home")
def home():
    return "<p>lets go guys</p>"

if __name__=='__main__':
    app.run(host="127.0.0.1",debug=True)
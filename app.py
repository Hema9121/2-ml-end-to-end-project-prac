from flask import Flask

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def app1():
    return "<h2>my practice app</h2>"

if __name__=="__main__":
    app.run(debug=True)
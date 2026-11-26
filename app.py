from flask import Flask, render_template, request
import pickle as pkl
import re

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="POST":
        lpa=float(request.form["lpa"])
        with open("model.pkl","rb") as f:
            model=pkl.load(f)
        predection = model.predict([[lpa]])
        prediction=str(predection[0])
        p=prediction.strip('[')
        p2=p.strip(']')
        return render_template("index.html",a=str(p2[0:3])+" LPA")
    else:
        return render_template("index.html")
    
if __name__=="__main__":
    app.run(debug=True)
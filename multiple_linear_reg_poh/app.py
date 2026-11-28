from flask import Flask, render_template, request
import pickle as pkl

app=Flask(__name__)
# Area_sqft	Bedrooms	Bathrooms	House_Age	House_Price_Lakhs
# 0	928	3	2	49	98.03

@app.route('/',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        area=float(request.form['area'])
        bed=float(request.form['bed'])
        bath=float(request.form['bath'])
        age=float(request.form['age'])
        with open('mlr.pkl','rb') as f:
            model=pkl.load(f)
        prediction=model.predict([[area,bed,bath,age]])
        return render_template('index.html',result=str(prediction[0])[1:-6]+" Lakhs") 
    else:
        return render_template('index.html')
    
app.run(debug=True)
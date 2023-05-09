from flask import Flask,render_template,request
import numpy as np
import pickle

app=Flask(__name__)
model=pickle.load(open('CKD.pkl','rb'))


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/prediction',methods=['POST','GET'])

def prediction():
    return render_template('indexnew.html')
@app route('/Home',methods=['POST','GET'])
def my_home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():

    input_features=[float(x) for x in request.form.values()]
    features_value=[np.array(imput_features)]

    features_name=['blood_urea','blood glugose random','anemia',
                   'coronary_artery_disease','pus_cell','red_blood_cells',
                   'diabetesmellitus','pedal_edama']
    
    df=pd.DataFrame(feature_value,columns=features_name)

    output=model.predict(df)

    render_template('result.html',prediction_text=output)


    if __name__=='__main__':

        app.run(debug=True)
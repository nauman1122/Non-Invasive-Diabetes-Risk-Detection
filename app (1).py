import os
from flask import Flask, render_template,request
import pickle
import gzip

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# About Diabetes pages
@app.route('/about_diabetes')
def about_diabetes():
    return render_template('about-diabetes.html')

@app.route('/about_diabetes/types_of_diabetes')
def types_of_diabetes():
    return render_template('types-of-diabetes.html')

@app.route('/about_diabetes/diabetes_risks')
def diabetes_risks():
    return render_template('diabetes-risks.html')

@app.route('/about_diabetes/signs_and_symptoms')
def signs_and_symptoms():
    return render_template('signs-and-symptoms.html')

@app.route('/about_diabetes/treatment_and_medication')
def treatment_and_medication():
    return render_template('treatment-and-medication.html')

# Diabetes and You pages
@app.route('/diabetes_and_you')
def diabetes_and_you():
    return render_template('diabetes_and_you.html')

@app.route('/diabetes_and_you/type1_diabetes')
def type1_diabetes():
    return render_template('type1-diabetes.html')

@app.route('/diabetes_and_you/type2_diabetes')
def type2_diabetes():
    return render_template('type2-diabetes.html')

@app.route('/diabetes_and_you/gestational_diabetes')
def gestational_diabetes():
    return render_template('gestational-diabetes.html')

@app.route('/diabetes_and_you/prediabetes')
def prediabetes():
    return render_template('prediabetes.html')

@app.route('/diabetes_and_you/kids_teens_diabetes')
def kids_teens_diabetes():
    return render_template('kids-teens-diabetes.html')

@app.route('/diabetes_and_you/control_diabetes')
def control_diabetes():
    return render_template('control-diabetes.html')

# Other pages
@app.route('/test')
def test():
    return render_template('test.html')

def load_model(model_filename):
    model_path = os.path.join(os.path.dirname(__file__), model_filename)
    # Load the compressed model
    with gzip.open(os.path.abspath(model_path), 'rb') as f:
        model = pickle.load(f)
    return model

@app.route('/result', methods = ['POST'])
def result():
    age = int(request.form['age'])
    income = int(request.form['income'])
    education = int(request.form['education'])
    bmi = float(request.form['bmi'])
    phyact = int(request.form['phyact'])
    heartprob = int(request.form['heartprob'])
    highchl = int(request.form['highchl'])
    smoke = int(request.form['smoke'])
    alcohol = int(request.form['alcohol'])
    htstroke = int(request.form['heatstroke'])
    bloodpressure = int(request.form['bldpre'])
    diffWalk = int(request.form['diffwalk'])
    generalHealth = int(request.form['genlt'])
    DocCost = int(request.form['doc'])
    physicalHealth = int(request.form['phyhlt'])
    mentalHealth = int(request.form['menlt'])


    loaded_model = load_model('random_forest_model.pkl.gz')
    prediction = loaded_model.predict_proba([[bloodpressure, highchl, bmi, smoke, htstroke, heartprob, phyact, alcohol, DocCost, generalHealth, mentalHealth,physicalHealth,diffWalk, age, education, income]])
    return render_template('result.html', result = prediction[0][1]*100)

@app.route('/health_tools/bmi_calculator')
def bmi_calculator():
    return render_template('bmi-calculator.html')

@app.route('/health_tools/calorie_calculator')
def calorie_calculator():
    return render_template('calorie-calculator.html')

if __name__ == '__main__':
    app.run(debug=True)

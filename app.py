from flask import Flask, request, render_template
from flask_cors import cross_origin
import pandas as pd
import pickle

app = Flask(__name__)


@app.route('/', methods=['GET'])
@cross_origin()
def homePage():
    return render_template('index.html')

@app.route('/Prediction', methods=['POST', 'GET'])
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            age = int(request.form['age'])
            workclass = int(request.form['workclass'])
            fnlwgt = float(request.form['fnlwgt'])
            education = int(request.form['education'])
            education_num = int(request.form['education_num'])
            marital_status = request.form['marital_status']
            occupation = int(request.form['occupation'])
            relationship = request.form['relationship']
            race = request.form['race']
            sex = int(request.form['sex'])
            capital_gain = float(request.form['capital_gain'])
            capital_loss = float(request.form['capital_loss'])
            hours_per_week = float(request.form['hours_per_week'])
            native_country = request.form['native_country']
            occ_nan = 0

            data = [
                [age, workclass, fnlwgt, education, education_num, marital_status, occupation, occ_nan, relationship,
                 race, sex, capital_gain, capital_loss, hours_per_week, native_country]]
            data = pd.DataFrame(data,
                                columns=['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status',
                                         'occupation', 'occ_nan', 'relationship', 'race', 'sex', 'capital_gain',
                                         'capital_loss', 'hours_per_week', 'native_country'])

            relationship_map = {'Husband': 19716, 'Not-in-family': 12583, 'Own-child': 7581, 'Unmarried': 5125,
                                'Wife': 2331, 'Other-relative': 1506}
            data.relationship = data.relationship.map(relationship_map)

            race_map = {'White': 41762, 'Black': 4685, 'Asian-Pac-Islander': 1519, 'Amer-Indian-Eskimo': 470,
                        'Other': 406}
            data.race = data.race.map(race_map)

            continent_map = {'North_America': 44799, 'South_America': 1372, 'Central_America': 963, 'Asian': 918,
                             'EU': 790}
            data.native_country = data.native_country.map(continent_map)

            marital_map = {'Married-civ-spouse': 22379, 'Never-married': 16117, 'Divorced': 6633, 'Separated': 1530,
                           'Widowed': 1518, 'Married-spouse-absent': 628, 'Married-AF-spouse': 37}
            data.marital_status = data.marital_status.map(marital_map)

            model = pickle.load(open('xgb.pickle', 'rb'))
            prediction = model.predict(data)

            if prediction == 1:
                pred = 'greater than'
            else:
                pred = 'less than or equal to'

            return render_template('results.html', prediction=pred)
        except Exception as e:
            return print(e)
    else:
        return render_template('results.html')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8001)

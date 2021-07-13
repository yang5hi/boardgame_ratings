import requests
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import math
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from flask import Flask, render_template, request, redirect


app = Flask(__name__, static_url_path='/static')

df = pd.read_csv('static/data/boardgames_07022021.csv')

predict_list = []

df_cleaned = df[df['usersrated'] > 0]
df_cleaned = df_cleaned[df_cleaned['yearpublished'] > 2010]
df_cleaned = df_cleaned[df_cleaned['maxplaytime'] < 300]
print(df_cleaned.shape)

X = df_cleaned.loc[:, ['minplayers', 'maxplayers',
                       'minplaytime', 'maxplaytime', 'minage']]
y = df_cleaned.loc[:, ['average']]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, random_state=42)

LinModel = LinearRegression()

LinModel.fit(X_train, y_train)

RF_model = RandomForestRegressor(
    n_estimators=100, min_samples_leaf=10, random_state=1)

RF_model.fit(X_train, y_train)


@app.route("/")
def home():
    print(f"home")

    return render_template("ml.html", predict_list =predict_list)


@app.route("/prediction", methods=['POST'])
def prediction():
    # print(f"prediction")

    minplayers = request.form['minplayers']
    maxplayers = request.form['maxplayers']
    minplaytime = request.form['minplaytime']
    maxplaytime = request.form['maxplaytime']
    minage = request.form['minage']

    predict_list.append(minplayers)
    predict_list.append(maxplayers)
    predict_list.append(minplaytime)
    predict_list.append(maxplaytime)
    predict_list.append(minage)

    print(f"=======================")
    print(f"{predict_list}")
    print(f"=======================")

    X_pred = np.array(
        [[minplayers, maxplayers, minplaytime, maxplaytime, minage]])

    y_pred = LinModel.predict(X_pred)

    LinModel_pred = round(y_pred[0][0], 2)
    print(f'LinModel prediction= {LinModel_pred}')

    y_pred = RF_model.predict(X_pred)

    RF_pred = round(y_pred[0], 2)
    print(f'RF prediction= {RF_pred}')

    predict_list.append(LinModel_pred)
    predict_list.append(RF_pred)

    return render_template("ml.html", predict_list=predict_list)


if __name__ == "__main__":
    app.run(debug=True)

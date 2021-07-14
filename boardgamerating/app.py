# Dependencies
from types import new_class
import numpy as np
import pandas as pd
from flask import Flask, render_template, request

# =========================================================================================================
# read in csv file
game_info_df=pd.read_csv("../data/boardgames_07022021.csv")
# remove duplicate games
game_info_df.drop_duplicates(subset=['objectid'], inplace=True)
# choose the features based on correlations
game_info_df=game_info_df[['average', 'numwanting', 'siteviews', 'blogs', 'minage', 'news',
                           'podcast', 'totalvotes', 'numcomments', 'numgeeklists', 'weblink']].copy()
# remove the rows which have invalid values
game_info_df.drop(game_info_df[game_info_df['average'] ==0].index, inplace = True)
game_info_df.drop(game_info_df[game_info_df['totalvotes'] ==0].index, inplace = True)
# drop the null rows
game_info_df.dropna(inplace=True)
# =========================================================================================================
# Set features (X) and target (y)
y=game_info_df['average']
X=game_info_df.drop(['average'],axis=1)
# Scale the data
from sklearn.preprocessing import MinMaxScaler
X_scaler = MinMaxScaler().fit(X)
X_scaled = X_scaler.transform(X)
# =========================================================================================================
from sklearn.ensemble import RandomForestRegressor
 # Create a random forest regressor,  n_estimators=100, criterion="mse", max_depth="None"
rf = RandomForestRegressor()
rf.fit(X_scaled, y)
# =========================================================================================================

app = Flask(__name__, static_url_path='/static')

RF_pred="  "
X_pred=[]

@app.route("/")
def home():
    print(f"home")
    return render_template("index.html", RF_pred=RF_pred[0],X_pred=X_pred)

@app.route("/prediction", methods=['POST','GET'])
def prediction():
    print(f"prediction")
    
    numwanting = request.form['numwanting']
    siteviews = request.form['siteviews']
    blogs = request.form['blogs']
    minage = request.form['minage']
    news = request.form['news']
    podcast = request.form['podcast']
    totalvotes = request.form['totalvotes']
    numcomments = request.form['numcomments']
    numgeeklists = request.form['numgeeklists']
    weblink = request.form['weblink']

    X_pred = np.array([[numwanting,siteviews, blogs, minage, news,
                podcast, totalvotes, numcomments, numgeeklists, weblink]])

    y_pred = rf.predict(X_pred)

    RF_pred = [round(y_pred[0], 2)]
    print(f'RF prediction= {RF_pred[0]}')
    print(X_pred[0])

    return render_template("index.html", RF_pred=RF_pred[0], X_pred=X_pred[0])


if __name__ == "__main__":
    app.run(debug=True)
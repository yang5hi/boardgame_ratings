# boardgame_ratings

we will to explore the BoardGameGeek dataset. Using machine learning, we intend to predict what rating a board game should have on the BGG website (on a scale of 1-10) based on factors such as type, name, playtime, categories, total_comments, total_wants, etc. To achieve this we will also be using Pandas, sklearn, and HTML/CSS/Bootstrap.



Exploratory data analysis (EDA)



- svm
- [sklearn.ensemble.AdaBoostRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html?highlight=regressor#sklearn.ensemble.AdaBoostRegressor) 
- [sklearn.ensemble.RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html?highlight=regressor#sklearn.ensemble.RandomForestRegressor) **0.65**
- [sklearn.neighbors.KNeighborsRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html?highlight=regressor#sklearn.neighbors.KNeighborsRegressor) **less than 0.5 data score**
- [sklearn.neighbors.RadiusNeighborsRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsRegressor.html?highlight=regressor#sklearn.neighbors.RadiusNeighborsRegressor)
- [sklearn.neural_network.MLPRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html?highlight=regressor#sklearn.neural_network.MLPRegressor) 
- [sklearn.tree.DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html?highlight=regressor#sklearn.tree.DecisionTreeRegressor) **<0.5**
- 

| **Regression**       | metrics link                                                 |
| -------------------- | ------------------------------------------------------------ |
| ‘explained_variance’ | [`metrics.explained_variance_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.explained_variance_score.html#sklearn.metrics.explained_variance_score) |
| ‘r2’                 | [`metrics.r2_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score) |
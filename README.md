# CricketCast
**CricketCast** is a real-time cricket score prediction system that leverages advanced analytics and machine learning. It processes live match data alongside historical trends to forecast the final score at any moment during an ongoing cricket match, offering dynamic insights for fans and strategists alike.

## Project Objective
This project aims to predict the final score of a cricket innings using ball-by-ball data. It employs a regression-based approach using machine learning models including Decision Tree, Random Forest, and XGBoost Regressor. This prediction can help analysts, commentators, or even fantasy game platforms understand and forecast the outcome of a match as it unfolds.

## Dataset Description
The dataset contains ball-by-ball details of cricket matches, including:

```markdown
| Column               | Description                                                 |
|----------------------|-------------------------------------------------------------|
| `inning`             | Inning number (1 or 2)                                      |
| `over`               | Over number (0-20)                                          |
| `ball`               | Ball number within the over (1-6)                           |
| `score`              | Runs scored upto that ball                                  |
| `is_home_team`       | Boolean indicating if the batting team is the home team     |
| `final_innings_score`| Target variable: total runs scored in the innings           |
| `batter_code`        | Encoded unique ID for the batter                            |
| `bowler_code`        | Encoded unique ID for the bowler                            |
| `non_striker_code`   | Encoded unique ID for the non-striker                       |
| `batting_team_code`  | Encoded team ID for the batting team                        |
| `bowling_team_code`  | Encoded team ID for the bowling team                        |
```

## Project Structure
```bash
.
├── Preprocessing.ipynb          # Data loading and encoding
├── Feature_Engineering.ipynb    # New features creation
├── Model.ipynb                  # Model training, evaluation, saving
└── README.md
```
## Preprocessing
- Removed redundencies like change of team names causing same teams with different name
- For venues, assigned home venues to each team and removed the repetiton of names
- Analysed factors like dependency of match result on toss and removed those columns
- Added whether the home team wins or away team wins along with tracking whether it is a neutral venue or not
- Plotted various graphs to figure out relations between teams and different columns
   
## Feature Engineering
- Encoded following categorical features:
  - batter_code
  - bowler_code
  - non_striker_code
  - batting_team_code
  - bowling_team_code
- Made a player_stats.csv to store the stats of every player

## Model
Regression Models have been used after extracting the information on which model is supposed to be trained. Then, a 80-20 train test split is used on the dataset for testing accuracy of the model. Following Regression Models have been used to predict the final score of the innings:
- Linear Regression
- Decision Tree Regression
- Random Forest Regression
- Extra Tree Regression
- XGB Regression
The results as quoted below shows that the Extra Tree Regression is the best model for the prediction task

## Results
```markdown
| Model                  | MAE       | RMSE      | R² Score   |
|------------------------|-----------|-----------|------------|
| Linear Regression      | 17.22     | 23.26     | 0.448      |
| Decision Tree Regressor| 5.22      | 14.03     | 0.799      |
| Random Forest Regressor| 6.29      | 9.85      | 0.901      |
| Extra Tree Regressor   | 4.46      | 7.84      | 0.937      |
| XGB Regressor          | 13.84     | 18.65     | 0.645      |
```
This clearly shows how extra tree regressor is best model among all the used models

## Installation
Make sure Python 3.8+ is installed. Then install dependencies:
```bash
pip install pandas scikit-learn xgboost
```
You can then run the notebooks in order:
- Preprocessing.ipynb -> Clean data and Observe trends
- Feature_Engineering.ipynb -> Encode and Create new features
- Model.ipynb -> Train models to analyse and get the best out of them

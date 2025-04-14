# CricketCast
**CricketCast** is a real-time cricket score prediction system that leverages advanced analytics and machine learning. It processes live match data alongside historical trends to forecast the final score at any moment during an ongoing cricket match, offering dynamic insights for fans and strategists alike.

## Project Objective
This project aims to predict the final score of a cricket innings using ball-by-ball data. It employs a regression-based approach using machine learning models including Decision Tree, Random Forest, and XGBoost Regressor. This prediction can help analysts, commentators, or even fantasy game platforms understand and forecast the outcome of a match as it unfolds.

## Dataset Description
The dataset contains ball-by-ball details of cricket matches, including:

| Column | Description |
| inning | Inning number (1 or 2) |
| over | Over number (0-20) |
| ball | Ball number within the over (0-5)
total_runs	Runs scored on the ball (including extras)
is_home_team	Boolean indicating if the batting team is the home team
final_innings_score	Target variable: total runs scored in the innings
batter_code	Encoded unique ID for batter
bowler_code	Encoded unique ID for bowler
non_striker_code	Encoded unique ID for non-striker
batting_team_code	Encoded team ID for batting team
bowling_team_code	Encoded team ID for bowling team

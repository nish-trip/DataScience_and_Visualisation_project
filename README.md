# Analysing the football transfer market 

This project helps us analyse the football transfer market to determine the relation between _Age_, _Transfer Fee_ and  _Market Value_ of players . We also take a close look into which of the top 5 football league in Europe has the highest market value. The top 250 transfers are considered from each year between the 2005/06 season and 2018/19 season. Player's _name, position, age, previous team, new team, previous league, current league, season, market value, transfer fee_ is taken into consideration.
We make use of the following libraries for the purpose of data cleaning, scientific calculations and data visualisation _pandas ,numpy, matplotlib.pyplot, scipy and seaborn_.
A PowerPoint presentation is available in the repository which shows the Visualisation , Data Cleaning process, etc . 

## Documentation

[pandas](https://pandas.pydata.org/) library

[numpy](https://numpy.org/doc/) library

[matplotlib](https://matplotlib.org/3.2.1/contents.html) library

[scipy](https://www.scipy.org/) library

[seaborn](https://seaborn.pydata.org/) library

## Library Installation 

* pip install pandas
* pip install numpy
* pip install matplotlib
* pip install scip
* pip install seaborn

## Dataset and Inference

The dataset used for this project was found on kaggle :
https://www.kaggle.com/vardan95ghazaryan/top-250-football-transfers-from-2000-to-2018

We observe that the average Market Value and Transfer Fee is gradually increasing with each year. This may be due to a variety of reasons like inflation and increasing commercialization of the sport also from the boxplot, we infer that out the 5 major leagues in the world , the Bundesliga (German League)  and the English Premier League seem to have the most valuable players, as its median value is slightly higher than that of the other leagues. The correlational analysis tell us that there is a strong linear relationship between the Market Value and Transfer Fee of the player. 
The relationship between Age of the player and Market Value, and Age of the player and Transfer fee, is non-linear as player's performance usually peaks between the age of 25-30 and there might be a steady decline following that. 

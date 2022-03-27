import pandas as pd
import numpy as np

# refer to pandas-dataframe2py and csv for help on this
# column names: year,Team,Wins,Losses,Runs Scored,Runs Allowed
df = pd.read_csv('standings.csv')

# Calcuated additonal columns for Scoring Ratio,Predicted Winnings, Acutal winnings
# and absolute error for the difference inbetween
df['ScoringRatio']= df['Runs Scored']/df['Runs Allowed']
df['PredictedWinningPercentage']= df['ScoringRatio']**2/(1.0 + df['ScoringRatio']**2)
df['ActualWinningPercentage'] = df['Wins']/(df['Wins']+df['Losses'])
df['AbsoluteError']= (df['ActualWinningPercentage']-df['PredictedWinningPercentage']).abs()


# printing out new columns with original dataframe
print('the initial dataframe:\n', df.head())

# calculating the Mean Absolute Devations of the Absolute Errors column
avergaeAB = df['AbsoluteError'].mean()
calcMAD = ((df['AbsoluteError']-avergaeAB).abs()).mean()

# Misc. Test
# calcMAD = 0.0200001
# meanAbsDeviation = df['AbsoluteError'].mad()

# printing out the MAD & whether or it is less then 2%
print('\nThe calulated MAD: '+ str(calcMAD))
YorN = 'Yes'
if calcMAD >= 0.02:
    YorN ='no'
else:
    YorN = 'yes'
print('Is it less than 2%? '+ YorN)

# print('numpy calculated MAD: '+str(meanAbsDeviation))

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


df = pd.read_csv('./data/posty_greeno.csv', index_col=6)
final_df  = df.iloc[:, [16,25,26,27,28,29]]
final_df.columns = ['views', 'recipient', 'activity', 'share', 'likes', 'comments']
final_df.index.name = 'time'
final_df.to_csv('./data/after_greeno.csv')
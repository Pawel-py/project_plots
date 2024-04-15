import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


df = pd.read_csv('./data/after_greeno.csv', index_col=0)
plt.rcParams['figure.dpi'] = 1000

new_index= []

for a in df.index:
    new = a.split(' ')
    new_index.append(new[0])
    
idx_2 = new_index[2:]    
idx_2.append(new_index[0])
idx_2.append(new_index[1])
idx_2 = idx_2[::-1]
df.index = idx_2
df.index.name = 'time'
#%%
ax = df['likes'].plot(color='red', marker='.', alpha=0.7)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
plt.title('Likes', fontsize=20)
plt.show()

#%%
ax = df['views'].plot(color='orange', marker='.', alpha=0.7)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
plt.title('Views', fontsize=20)
plt.show()

#%%
ax = df['recipient'].plot(color='brown', marker='.', alpha=0.7)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
plt.title('Recipient', fontsize=20)
plt.show()

#%%
ax = df['activity'].plot(color='#8B4513', marker='.', alpha=0.7)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
plt.title('Activity', fontsize=20)
plt.show()

#%%
ax = df.plot(cmap='viridis', marker='.')
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
plt.title('Our FaceBook in numbers', fontsize=20, fontweight='bold')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.show()

#%%

ax = df.max().plot(kind='bar', cmap='viridis', alpha=0.6)
plt.title('Top Post Results in Specific Areas', fontsize=20, fontweight='bold')
plt.show()

#%%
ax = df.mean().plot(kind='bar', cmap='viridis', alpha=0.6)
plt.title('Average Post Results', fontsize=20, fontweight='bold')
plt.show()

#%%

sns.heatmap(df.iloc[:,[0,1,2]].corr(), cmap='coolwarm', annot = True, 
            annot_kws={'color':'black'})
plt.title('Heatmap of the correlation matrix for selected columns', fontsize=20,
          fontweight='bold')
plt.show()

#%%
df['engagement_rate'] = round(df['activity']/df['recipient'], 2)
ax = df['engagement_rate'].plot(color='black', marker='.', alpha=0.8)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
plt.title('Percentage Degree of Engagement', fontsize=20)
plt.show()
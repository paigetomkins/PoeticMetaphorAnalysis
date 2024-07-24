import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('ggplot')
pd.options.display.max_columns = 6

df = pd.read_csv('/home/paige-tomkins/ICR-linguistics/fulldataset.csv')

#Distributions
"""
ax = df['age'].value_counts().plot(kind='bar', title='Age Distribution')

ax.set_xlabel('Age')
ax.set_ylabel('Number of Poems Included')
plt.show()
"""

#Correlation
correlation = df[['author', 'age']].corr()
print(correlation)


import pandas as pd
data = [10, 20, 30, 40]
series = pd.Series(data)
print(series)
series[1]=45
#print(series)
print(series.index)
print(series.values)




data = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])


print(data.iloc[0])  


print(data['b'])  


print(data[::2]) 


import pandas as pd

# Creating a Pandas Series
data = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

# Inserting a new value at a specific index
data['d'] = 40  # Adds a new element with index 'd'
print(data)
# Output:
# a    10
# b    20
# c    30
# d    40
# dtype: int64


# Inserting at the beginning
data['z'] = 50  # Adds a new element with index 'z'
data = data.sort_index(ascending=True)  # Sort to maintain order
print(data)
# Output:
# a    10
# b    20
# c    30
# d    40
# z    50
# dtype: int64

# Deleting an element by index
data = data.drop('c')
print(data)
# Output:
# a    10
# b    20
# d    40
# z    50
# dtype: int64


# Using apply with a condition to label values
data_labels = data.apply(lambda x: 'High' if x > 50 else 'Low')
print(data_labels)
# Output:
# 0     Low
# 1     Low
# 2     Low
# 3    High
# 4     Low
# dtype: object


# Creating two Series
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([4, 5, 6], index=['b', 'c', 'd'])

# Combining into a DataFrame based on index
appended = s1._append(s2)
print(appended)
# Output:
#       0    1
# a   1.0  NaN
# b   2.0  4.0
# c   3.0  5.0
# d   NaN  6.0

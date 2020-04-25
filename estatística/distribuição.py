import pandas as pd

df = pd.DataFrame({'Height':[184,180,181,184,182,181,182,182,
183,182,181,182,182,180,183,181,184,183,182,182,183,182,183,
181,180,181,183]})

print ('Min: ' + str(df['Height'].min()))
print ('Mode: ' + str(df['Height'].mode()[0]))
print ('Median: ' + str(df['Height'].median()))
print ('Mean: ' + str(df['Height'].mean()))
print ('Max: ' + str(df['Height'].max()))
print ('Std Deviation: ' + str(df['Height'].std()))
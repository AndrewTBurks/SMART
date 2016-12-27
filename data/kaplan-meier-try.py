import pandas as pd

# your argument in the function call below will be different
df = pd.read_csv('kaplanMeier.csv', header=0, usecols = ['Ethnicity','Site','Tcategory','OS', 'Censor'] )

df = df[df['Site'] == "glottic"]
df = df[df['Ethnicity'] == "white"]

from lifelines.utils import survival_table_from_events

df1 = df[df['Tcategory'] == 'T3']
df1['Censor'][df['Censor'] == 0] = 1
df1['Censor'][df['Censor'] == 1] = 0

df2 = df[df['Tcategory'] == 'T4']
df2['Censor'][df['Censor'] == 0] = 1
df2['Censor'][df['Censor'] == 1] = 0



T = df1['OS']
E= df1['Censor']
table = survival_table_from_events(df1['OS'], df1['Censor'])
table2 = survival_table_from_events(df2['OS'], df2['Censor'])
print table.head()

from lifelines import KaplanMeierFitter
kmf = KaplanMeierFitter()
kmf.fit(T, event_observed=E, label ="T3") # more succiently, kmf.fit(T,E)
print kmf.survival_function_

ax = kmf.plot()

T = df2['OS']
E= df2['Censor']
kmf.fit(T, event_observed=E , label= "T4") # more succiently, kmf.fit(T,E)
kmf.plot(ax=ax)

kmf.show()
import pandas as pd
df=pd.read_csv("digital_behaviour.csv")
print(df.head())
print(df.tail())
print(df.shape)
print(list(df.columns))
#print(df.describe())
print(df[['Instagram_Minutes','Study_Minutes']].describe())
#column_name=['Instagram_Minutes','Study_Minutes']
#print(df[column_names].describe())
print(df['Instagram_Minutes'])
print(df[['Instagram_Minutes','Date']])
print(df['Instagram_Minutes'].sum())
print(round(df['Study_Minutes'].mean(),2))
print(df['YouTube_Minutes'].max())
print(df[df['Instagram_Minutes']>100])
print(df[df['Study_Minutes']>180])
print(df[df['Study_Minutes']<df['Instagram_Minutes']])
#print(df[(df['Instagram_Minutes']>100) & (df[Study_Minutes']<100)])
#print(df['Instagram_Minutes'].head(5).sort_values(ascending=False))            ["Here, we pick first five values and then sorted them"]
sorting_insta=df.sort_values(by='Instagram_Minutes',ascending=False).head(5)        #  ["Here, we sorted all the values and then pick first five values"]
print(sorting_insta)
sorting_study=df.sort_values(by='Study_Minutes',ascending=False).head(5)        #  ["Here, we sorted all the values and then pick first five values"]
print(sorting_study)
df['Total_Screen_Time']=df['Instagram_Minutes']+df['YouTube_Minutes']+df['WhatsApp_Minutes']+df['LinkedIn_Minutes']
df['Screen_Hours']=(df['Total_Screen_Time']/60).round(2)
df['Digital_Balance']=(df['Study_Minutes']/df['Total_Screen_Time']).round(2)
df['Day_Type']='Normal'
df.loc[df['Total_Screen_Time']>300,'Day_Type']='Heavy'     ##"IN PLACE OPERATION"
#df[df['Total_Screen_Time']>300]['Day_Type']='Heavy'       ""wrong"" ##"STANDARD OPERATION"  ("MASK CONCEPT")
print(df.head(5))                       ##Line 29 and 30 are similar but different due to their operations
print(df['Day_Type'].value_counts())   #gives no. of heavy and normal day type 


print(f"Instagram:{df['Instagram_Minutes'].sum()}, Youtube:{df['YouTube_Minutes'].sum()}, Whatsapp:{df['WhatsApp_Minutes'].sum()}, LinkedIn:{df['LinkedIn_Minutes'].sum()}")

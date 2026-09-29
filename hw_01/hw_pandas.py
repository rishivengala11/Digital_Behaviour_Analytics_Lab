import pandas as pd
df=pd.read_csv("./hw_01/placement_readiness.csv")
print(f"performing head():\n{df.head(3)}")
print(f"Shape of df {df.shape}")
print(f"columns of the df:\n{list(df.columns)}")
print(f"performing describe():\n{df.describe()}")

print(f"Students above 75 in python:\n{df[df['Python_Score']>75]}")
sorting_apt=df.sort_values("Aptitude_Score",ascending=False)
print(f"descending order of df by aptitude:\n{sorting_apt}")
sorting_py=df.sort_values("Python_Score",ascending=False)
print(f"Top 10 students in python:\n{sorting_py.head(10)}")
print(f"Students strong in python but weak in communication:\n{df[df['Python_Score']>df['Communication_Score']]}")

#New Knowledge
df["Total_Score"]=df["Communication_Score"]+df["Python_Score"]+df['SQL_Score']+df["Aptitude_Score"]
df["Average_Score"]=df["Total_Score"]/4
_columns_=["Python_Score","Communication_Score","Aptitude_Score","SQL_Score"]
df["Weakest_Skill_Score"]=df[_columns_].min(axis=1)
df["Readiness_Score"]=df["Average_Score"]+(df["Projects_Completed"]*2)+df["Mock_Interviews_Attended"]
df["Readiness_Score"]=df["Readiness_Score"].clip(upper=100)   
# df.loc[df["Readiness_Score"]>100,"Readiness_Score"]=100    we can also use this in the place of clip method


#Classification
df["Readiness_Band"]="Ready"
df.loc[df["Readiness_Score"]<60,"Readiness_Band"]="Needs Work"
df.loc[(df["Readiness_Score"]>=60) & (df["Readiness_Score"]<=74),"Readiness_Band"]="Almost Ready"
band_counts = df["Readiness_Band"].value_counts()
print(band_counts)
print("Largest band:", band_counts.idxmax())
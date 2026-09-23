import numpy as np
import csv

insta_min=[]
study_min=[]

with open("./digital_behaviour.csv","r",encoding="utf-8") as f:
    reader=csv.DictReader(f)
    for row in reader:
        insta_min.append(int(row["Instagram_Minutes"]))
        study_min.append(int(row["Study_Minutes"]))

insta_min=insta_min[:7]
study_min=study_min[:7]

instagram=np.array(insta_min)
study=np.array(study_min)
print(instagram,study)

insta_total=instagram.sum()
insta_average=instagram.mean()
insta_minimum=instagram.min()
insta_maximum=instagram.max()
insta_days=len(instagram)

print(f"total:{insta_total}, average:{insta_average}, minimum:{insta_minimum}, maximum:{insta_maximum}, days:{insta_days}")

print(instagram[0],instagram[-1],instagram[2])

print(instagram[0::2])
print(instagram[:3],instagram[-2:],instagram[1:4])

insta_hours=instagram/60
insta_hours=insta_hours.round(2)
print(insta_hours)

study_total=study.sum()
study_average=study.mean()
study_minimum=study.min()
study_maximum=study.max()
study_days=len(study)

print(f"total:{study_total}, average:{study_average}, minimum:{study_minimum}, maximum:{study_maximum}, days:{study_days}")

print(study[0],study[-1],study[2])

print(study[::2])
print(study[:3],study[-2:],study[1:4])

study_hours=study/60
study_hours=study_hours.round(2)
print(study_hours)

difference=study-instagram
# greater=[val for val in difference if val>100]  #list comprehension
i_boolean=instagram>100 #len(instagram) and len(greater) are equal that greater stores the boolean values.
#i_greater=[bool_ for bool_ in i_boolean if bool_]
# i_greater=filter(lambda bool_:bool_, i_boolean)
i_greater=instagram[instagram>100]

s_boolean=study>100
s_greater=study[study>100] #s_greater and i_greater stores only values where the condition >100 is met

i_count=i_boolean.sum()
print(i_count)
s_count=s_boolean.sum()
print(s_count)
##above average comparison
i_abv_average=instagram[instagram>insta_average]
s_abv_average=study[study>study_average] 

 
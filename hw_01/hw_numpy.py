import numpy as np
import csv

py_score=[]
apt_score=[]
sql_score=[]
comuni_score=[]

with open("./hw_01/placement_readiness.csv","r",encoding="utf-8") as f:
    reader=csv.DictReader(f)
    for row in reader:
        py_score.append(int(row["Python_Score"]))
        apt_score.append(int(row["Aptitude_Score"]))
        comuni_score.append(int(row["Communication_Score"]))
        sql_score.append(int(row["SQL_Score"]))

py_score=np.array(py_score)
apt_score=np.array(apt_score)
comuni_score=np.array(comuni_score)

py_score_avg=py_score.mean()
print(f"Python average score across the batch is {py_score_avg}")

low_apt_score_=apt_score.min()
high_apt_score=apt_score.max()
print(f"Highest aptitude score is {high_apt_score}, Lowest aptitude score is {low_apt_score_}")

comuni_count=(comuni_score>70).sum()
print(f"The no. of students who scored above 70 in communication is {comuni_count}")

scores=np.column_stack((
    py_score,
    sql_score,
    apt_score,
    comuni_score
))
best_scores=np.max(scores,axis=1)
worst_scores=np.min(scores,axis=1)
gap=best_scores-worst_scores
print(gap)
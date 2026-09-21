import csv
APP="Instagram"
minutes = []
with open("digital_behaviour.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        minutes.append(int(row["Instagram_Minutes"]))
minutes = minutes[:7]
# s="A single piece of text"    slicing with step
# print(s[1::2]+"\t"+s[0::2])
total=sum(minutes)
# print(total)
average=total/len(minutes)
# print(average)
highest=max(minutes)
# print(highest)
lowest=min(minutes)
# print(lowest)
counter=0
for i in range(len(minutes)):
    if minutes[i]>average:
        counter+=1
# print(counter)
print(f"The app we are working on is {APP} the total time spent on the app for a week is {total} with an average of {average}.The highest time spent is {highest} and the lowest time spent is   {lowest}.There are {counter} days which are higher than average in the following week.")

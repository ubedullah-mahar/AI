#  task 02 
import numpy as np 
sr=np.array([60,90,101,-30,80])
print(sr)

sum=0
avg=0
count=0
count2=0
for i in sr:
    if i >=0 and i<=100:
        sum+=i
        count+=1

avg=sum/count
print("average of valid readings ",avg )

count_invalid=0
for i in range(len(sr)):
    if sr[i]<0 or sr[i]>100 :
        count_invalid+=1
        sr[i]=avg
print(" total invalid readings ", count_invalid)
print(sr)
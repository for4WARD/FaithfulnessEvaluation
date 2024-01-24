import json
import os
    
with open ("./wt_questions.json") as f:
    wt=json.load(f)

x_list=[]
y_list=[]
for i in range(len(wt)):
    score=0
    for j in range(len(wt[i])):
        if(wt[i]["pic_ans"][j]==1 or wt[i]["text_ans"][j]=="1"):
            score+=1
    x_list.append(score/len(wt[i]))
    y_list.append(wt[i]["human_score"])
    
import numpy as np
array1=np.array(x_list)
array2=np.array(y_list)
print(array1)
print(array2)
correlation=np.corrcoef(array1,array2)

print(correlation)
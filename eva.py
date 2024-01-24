import json
import os
with open ("./human_eva.json") as f:
    all=json.load(f)
x_list=[]
y_list=[]
min_num=10086
max_num=0
for i in range(50):
   #  print(all[i]['candidate_inter'])
   #  print(all[i]['content'])
    tp=0
    tn=0
    fp=0
    fn=0
    without_groundtruth_true=0
    without_groundtruth_false=0
    min_num=min(min_num,len(all[i]['question']))
    max_num=max(max_num,len(all[i]['question']))
    for j in range(len(all[i]['question'])):
        if (all[i]['true_summary_ans'][j]==1) and all[i]['candidate_inter_ans'][j]==1:
           tp+=1
        elif all[i]['true_summary_ans'][j]==0 and all[i]['candidate_inter_ans'][j]==0:
           tn+=1
        elif all[i]['true_summary_ans'][j]==0 and all[i]['candidate_inter_ans'][j]==1:
           fp+=1
        else:
           fn+=1
        if all[i]['candidate_inter_ans'][j]==1 and ( all[i]["pic_ans"][j]==1 ):
           without_groundtruth_true+=1
        elif all[i]['candidate_inter_ans'][j]==1 and (all[i]["pic_ans"][j]==0):
            without_groundtruth_false+=1
    x=(tp+tn)
    y=(tp+tn+fp+fn)
    
    score=0
    if x==y:
         score=5
    elif (y-x)<=1 and (y-x)<=y/4:
         score=4
    elif min(2,y/4)<=(y-x)<=y/3:
         score=3
    elif y/2>(y-x)>y/3:
         score=2
    else:
         score=1

         
    x_list.append(score)
    y_list.append(all[i]["human_score"])

import numpy as np

array1=np.array(x_list)
array2=np.array(y_list)

correlation=np.corrcoef(array1,array2)

print(correlation)

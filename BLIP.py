# get vqa answers
import json
import os
import requests
from PIL import Image
import torch
from transformers import Blip2Processor, Blip2ForConditionalGeneration
import time

time_begin=time.time()
with open ("./wt.json") as f:
    all=json.load(f) 
processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b")
model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b" , device_map="auto")

output=[]
for i in range(len(all)):
    now=all[i]
    now['pic_ans']=[]
    now['pic_ans_context']=[]
    raw_image = Image.open(f'./images_test/{all[i]["order"]}.jpg').convert('RGB')
    for j in range(len(all[i]["questions"])):
        qtext=f'Question: {all[i]["questions"][j]}  Answer:'
        print("i:",i,"j:",j)
        inputs = processor(raw_image, qtext, return_tensors="pt").to("cuda")
        out = model.generate(**inputs)
        ans_text=processor.decode(out[0], skip_special_tokens=True).strip()
        now['pic_ans_context'].append(ans_text)
        print(ans_text)
        if "yes" in ans_text.lower():
            now['pic_ans'].append(1)
        else:
            now['pic_ans'].append(0)
    output.append(now)
    
with open('vqa_done.json', 'w') as outfile:
    json.dump(output, outfile)
        
# nohup python ./BLIP_QA.py > ./BLIP_QA.log 2>&1 &



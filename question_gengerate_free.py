import openai 
import os
import json
with open ("./test_text.txt") as f:
    lines= f.readlines()
    lines1 = [line.strip() for line in lines]
with open ("./test_summary.txt") as f:
    lines= f.readlines()
    lines2 = [line.strip() for line in lines]
with open ("./test_human_score.txt") as f:
    lines= f.readlines()
    lines3 = [line.strip() for line in lines]
openai.api_key=os.getenv("OPENAI_API_KEY")

json_ans=[]
for i in range(len(lines1)):
    if i%10==0:
        print(i)
    
    ans={}

    ans['order']=i+1
    ans['content']=lines1[i]
    ans['summary']=lines2[i]
    ans['human_score']=lines3[i]
    content='I will now provide you with a sentence. Please generate three yes/no questions regarding the entities and relationships within this sentence. The answers to these three questions should all be true. Please present the questions in the format of ["question1", "question2", "question3"].The summary is:'
    content+=lines2[i]
    content+='Please give your response.'
    completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": content}
    ]
    )
    ans_str=completion.choices[0].message['content']
    ans_list = json.loads(ans_str)
    questions=[]
    for item in ans_list:
        questions.append(item)
    ans["text_ans"]=[]
    for j in range(len(questions)):
        content=f'
        I will provide you with a news segment and a question; please provide the answers to the questions in the form of 0 or 1, where 0 represents no and 1 represents yes. news:{lines1[i]},question:{questions[j]}'
        content+='Please give your response.'
    
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": content}
        ]
        )
        ans["text_ans"].append(completion.choices[0].message['content'])
with open('target_free.json', 'w') as outfile:
    json.dump(json_ans, outfile)


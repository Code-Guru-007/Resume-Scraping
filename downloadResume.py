import requests
import json
import os


M_H = 119
M_M = 520
M_L = 271
F_H = 174
F_M = 989
F_L = 587
total = 2361

base_link = '''
https://98mmn8mjed.us-east-1.awsapprunner.com/api/v1/file/download/
'''

file_data = open("result.json", "r", encoding='utf8').read()
all_data = file_data.split(',\n')

for data in all_data:
    json_data = json.loads(data)
    if (json_data["resume_id"] != ""):
        download_link = base_link + json_data["resume_id"]
        print(download_link)
        response = requests.get(download_link)
        if (json_data["gender"] == "male"):
            if not os.path.isdir('Male'):
                os.mkdir("Male")
            if (json_data["expected_salary"] < 5):
                if not os.path.isdir('Male\\Low'):
                    os.mkdir('Male\\Low')
                open(f"Male/Low/{M_L}_{json_data['name']}.pdf", "wb").write(response.content)
                M_L += 1
            if (5 <= json_data["expected_salary"] < 10):
                if not os.path.isdir('Male\\Medium'):
                    os.mkdir('Male\\Medium')
                open(f"Male/Medium/{M_M}_{json_data['name']}.pdf", "wb").write(response.content)
                M_M += 1
            if (json_data["expected_salary"] >= 10):
                if not os.path.isdir('Male\\High'):
                    os.mkdir('Male\\High')
                open(f"Male/High/{M_H}_{json_data['name']}.pdf", "wb").write(response.content)
                M_H += 1
        if (json_data["gender"] == "female"):
            if not os.path.isdir('Female'):
                os.mkdir("Female")
            if (json_data["expected_salary"] < 5):
                if not os.path.isdir('Female\\Low'):
                    os.mkdir('Female\\Low')
                open(f"Female/Low/{F_L}_{json_data['name']}.pdf", "wb").write(response.content)
                F_L += 1
            if (5 <= json_data["expected_salary"] < 10):
                if not os.path.isdir('Female\\Medium'):
                    os.mkdir('Female\\Medium')
                open(f"Female/Medium/{F_M}_{json_data['name']}.pdf", "wb").write(response.content)
                F_M += 1
            if (json_data["expected_salary"] >= 10):
                if not os.path.isdir('Female\\High'):
                    os.mkdir('Female\\High')
                open(f"Female/High/{F_H}_{json_data['name']}.pdf", "wb").write(response.content)
                F_H += 1

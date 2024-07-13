import requests
import json

url = 'https://employerapi.virtualstaff.ph/api/v1/employer/job-seekers-search'
headers = {
            'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmdWxsX25hbWUiOiJDYXJzb24gTGVlIiwidXNlcl9lbWFpbCI6InB5Lmd1cnUuMDA3QGdtYWlsLmNvbSIsInVzZXJfaWQiOiI2NTY3ZWEwNzlmNTQzZDAwODhlMGM0ZjYiLCJ1c2VyX3R5cGUiOiJlbXBsb3llciIsInVzZXJfdmVyaWZpY2F0aW9uX3N0YXR1cyI6ZmFsc2UsInRyYWNrZXJfaW5zdGFsbGVkIjpmYWxzZSwiaWF0IjoxNzA4MDIwODk5LCJleHAiOjE3MDgwNDk2OTl9.8oYOULDK2mfuU1ncyDjoL6obca9905AZSo3_fUEaaIk'
        }
skip = 116960


for x in range(231, 2310):
    print(f'>>>   {x}')
    myobj = {
        "limit": 100,
        "search_text": "",
        "skip": skip
        }
    response = requests.post(url, headers=headers, data=myobj)

    sep_result = json.loads(response.text)["result"]["data"]["data"]

    for data in sep_result:
        try:
            buf = {
                "id": data["_id"],
                "name": data["user_full_nam"],
                "gender": data["gender"],
                "resume_id": data["resume_id"],
                "expected_salary": data["expected_salary"]
            }
            with open('result.txt', 'a', encoding='utf-8') as file:
                # Write the data to the text file
                file.write(str(buf) + ',\n')
        except Exception:
            print('Error Occured')
    skip += 100

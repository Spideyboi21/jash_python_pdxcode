import requests
headers={"X-Mashape-Key": "RQgs6lmhYEmshika4gU0Rg7OEvzKp1q72lQjsnjWLhR8qOIUj2",
    "Accept": "text/plain"}

r = requests.get("https://yoda.p.mashape.com/yoda",
{"sentence":"You will learn how to speak like me someday"},
headers=headers)
print(r.text)

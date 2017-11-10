import requests

print("Hello! Please Enter The PR Number From Github")
prnum = input()

prshaobj = requests.get('https://api.github.com/repos/Electromaster232/FireSurvival-Docs/pulls/' + prnum)


url = prshaobj.text [18961:-250]



print("Your SHA1 is " + url)
status = input("Enter the Status you would like to apply to the PR ")
comment = input("Enter a comment (optional) ")


payload = {"state": status, "target_url": "https://github.com/Electromaster232/FireSurvival-Docs", "description": comment, "context": "pullrequest"}

headers = {"Authorization": "token <removed>”, "Host": "api.github.com", "Content-Type": "application/json"}

res = requests.post(url, json=payload, headers=headers)
print(res)

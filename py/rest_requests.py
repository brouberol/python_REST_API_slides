import requests, json

github_url = "https://api.github.com/user/repos"
data = json.dumps({'name':'test', 'description':'some test repo'}) 
r = requests.post(github_url, data, auth=('BaltoRouberol', '*****'))

print r.json

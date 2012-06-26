import pycurl, json

github_url = "https://api.github.com/user/repos"
user_pwd = "BaltoRouberol:*****"
data = json.dumps({"name": "test_repo", "description": "Some test repo"})

c = pycurl.Curl()
c.setopt(pycurl.URL, github_url)
c.setopt(pycurl.USERPWD, user_pwd)
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, data)
c.perform()
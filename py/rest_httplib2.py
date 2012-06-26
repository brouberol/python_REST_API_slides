import urllib, httplib2

github_url = "https://api.github.com/user/repos"

h = httplib2.Http(".cache")
h.add_credentials("BaltoRouberol", "******", "https://api.github.com")
data = urllib.urlencode({"name":"test"})
resp, content = h.request(github_url, "POST", data)

print content
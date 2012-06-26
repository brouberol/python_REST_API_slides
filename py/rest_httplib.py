import httplib

github_url = "api.github.com"
conn = httplib.HTTPConnection(github_url)

conn.request("GET", "/users/BaltoRouberol")
r = conn.getresponse()
print r.status, r.read()

# Does not work. httplib is a client side http module, not intended for direct use
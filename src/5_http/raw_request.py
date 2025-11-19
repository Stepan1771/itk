import http.client

conn = http.client.HTTPSConnection("www.google.com")
conn.request("GET", "/")
response = conn.getresponse()
print(response.read())
conn.close()

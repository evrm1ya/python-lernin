import urllib
response = urllib.urlopen('http://python.org/')
print response.headers
print response.headers['Content-Type']
print response.read()


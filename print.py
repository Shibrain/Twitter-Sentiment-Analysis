import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=shibrain")
pyresponse  = json.load(response)

#print pyresponse["results"]


result = pyresponse["results"]

print result[0]["text"]

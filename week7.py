In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse 
and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
Data Format
The data consists of a number of names and comment counts in JSON as follows:

{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}
The closest sample code that shows how to parse JSON and extract a list is json2.py. 
You might also want to look at geoxml.py to see how to prompt for a URL and retrieve data from a URL.


import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('enter --')
#entering the url for parsing
fhand=urllib.request.urlopen(url,context=ctx).read()
stuff=json.loads(fhand)
sum=0
comment=stuff['comments']
for i in comment:
    sum+=int(i['count'])
print(sum)

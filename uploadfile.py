import requests
files = {'file': open('result.txt', 'rb')}
r = requests.post("http://httpbin.org/post", files=files)
print(r.text)
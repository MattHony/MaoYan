import requests
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/12345679')
r = s.get('http://httpbin.org/cookies')
print(r.text)

import requests

url = "http://localhost:5002/pessoa"

x = requests.post(url, data="XXX")
if x.status_code != 200:
    print(f"[{x.status_code}] {x.text}")
else:
    print(x.text)

h = {"Content-Type": "application/json"}
y = requests.get(url, data="XXX", headers=h)
if y.status_code != 200:
    print(f"[{y.status_code}] {y.text}")
else:
    print(y.text)

z = requests.get(url, json={"foo": "bar"})
if z.status_code != 200:
    print(f"[{z.status_code}] {z.text}")
else:
    print(z.text)

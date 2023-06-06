import requests

a = input("Digite o valor de a: ")
b = input("Digite o valor de b: ")
url = f"http://localhost:5002/{a}/divide/{b}"

x = requests.get(url)

if x.status_code != 200:
    print(f"[{x.status_code}] {x.text}")
else:
    print(f"{a} dividido por {b} é igual a {x.text}.")

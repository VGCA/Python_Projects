import requests

# Create a session object
session = requests.Session()

# Log in and maintain the session automatically
login_url = "http://10.10.245.146/labs/lab4/login.php"
credentials = {"username": "admin", "password": "password123"}

response = session.post(login_url, data=credentials)

if "Welcome" in response.text:
    print("[+] Login successful. Session cookies are stored automatically!")
else:
    print("[-] Login failed.")
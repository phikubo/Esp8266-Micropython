import requests

url = "https://api2.apidaze.io/cfc79092/sms/send"

querystring = {"api_secret":"a1326351629f15b121b3e349f1908546","number":"573165258043","subject":"testing","body":"Message%20senttt%20from%20%mi%20pc"}

payload = ""
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)
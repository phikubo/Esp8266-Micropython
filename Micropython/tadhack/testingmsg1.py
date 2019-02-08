import requests

colombia=str(57)
orig_phone=colombia+str(15086829)
dest_phone=colombia+str(3165258043)

def msg(msg):
    pass



api_key ="cfc79092"
api_secret="a1326351629f15b121b3e349f1908546"
url = "https://api.apidaze.io/{}/sms/send".format(api_key)
print(url)
'''
querystring = {"api_secret":"{{api_secret}}"}

payload = "from=15558675309&to=15551234567&body=Have%20a%20great%20day."
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)
'''
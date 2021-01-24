import requests

# In the URL, change mstdn.social to the server on which your Mastodon account is hosted
url = 'https://mstdn.social/api/v1/accounts/verify_credentials'
auth = {'Authorization': 'Bearer <YOUR BEARER TOKEN/API AUTH KEY GOES HERE>'}

r = requests.get(url, headers=auth)

json = r.json()
myid = json['id']
print("My ID is: ")
print(myid)

import requests

url = 'https://mstdn.social/api/v1/accounts/verify_credentials'
auth = {'Authorization': 'Bearer <YOUR BEARER TOKEN/API AUTH KEY GOES HERE>'}
#params = {'status': 'Mastodon API request from Pythong!'}

r = requests.get(url, headers=auth)

json = r.json()
myid = json['id']
print("My ID is: ")
print(myid)
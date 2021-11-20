from requests.models import Request


class request:
    def __init__(self, url: str):

        self.url = url

    
    def requette(self):
        import requests
        response = requests.get(self.url)
        rresponse = f"Your country is {response.json()['country']} and your public IP is {response.json()['ip']} "
        return rresponse


request1 = request("https://ipinfo.io/json")

print(request1.requette())




import requests
import json

def get(_id=""):
    post_req = requests.get("https://api.dhariri.com/articles/{}".format(_id))

    return json.loads(post_req.text)

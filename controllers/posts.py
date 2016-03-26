import requests
import json


def get(_id=""):
    post_req = requests.get("https://api.dhariri.com/articles/{}".format(_id))

    if post_req.status_code is 200:
        return json.loads(post_req.text)
    else:
        return False

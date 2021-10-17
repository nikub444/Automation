import requests

url = "https://find-andrew-api.herokuapp.com/"
r = requests.get('https://find-andrew-api.herokuapp.com/',
                 headers={"apikey": "05da0dc747msh09150755268e421p148c8djsna768d3fd2802"})
print(r.json())

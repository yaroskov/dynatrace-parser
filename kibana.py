# from bs4 import BeautifulSoup
import requests


# Target web page
url = "http://p00pguelastic01.00.egov.local:5601/app/kibana#/discover?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:'2021-12-05T21:00:00.000Z',to:'2021-12-09T20:30:00.000Z'))&_a=(columns:!(msg_json.message,msg_json.traceId,msg_json.log.level),filters:!(),index:'85571840-df99-11eb-9e46-972219762301',interval:auto,query:(language:kuery,query:'msg_json.message%20:%221676310933%22'),sort:!())"

# Connection to web page
response = requests.get(url)
print(response.status_code)
print(response.text)

# Convert the response HTLM string into a python string
# html = response.text

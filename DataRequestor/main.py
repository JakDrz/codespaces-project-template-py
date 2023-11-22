from time import sleep
#from snap7.server import mainloop
import requests

res = requests.get("https://api.openaq.org/v2/locations/2178", , headers={"X-API-Key": "c07e50cfebdade8eb5e2dc0a5e29ea2e8a601d7ad9f5eb0ddfc8255f7609c88a"})

#https://docs.openaq.org/docs/getting-started

while (True):
    print('Test')
    sleep(2)




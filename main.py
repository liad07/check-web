import requests
import webbrowser
import time

url=input('enter url\n')
time1=input('Every once in a while you want to check the integrity of the site (Enter number of minutes)\n')
time1=int(time1)
r=requests.get(url)
x="liad"
y=1
z=0
counter=0



while y==1:
    if r.status_code == 200:
        print("web is online")
    else:
     x=str(r)
     print(r.status_code)
     webbrowser.open("whats mean"+x)
    time.sleep(time1 * 60)
    z=z+1
    print(f"The site has been checked {z} times")
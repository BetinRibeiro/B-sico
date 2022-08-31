import webbrowser
from time import sleep


url ="https://www.google.com"
for i in (range(int(10))):
    webbrowser.open(url)
    print(i)
    sleep(0)

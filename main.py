import pyqrcode # here pyqrcode is the module for to generate qrcode in python
from pyqrcode import QRCode
s = "https://www.youtube.com/watch?v=R4AbzwYOmNE"   #url link
url = pyqrcode.create(s)     #creating qrcode from url link
url.svg("myyoutube.svg",scale=8)


#scale = dimensions for code
#SVG stands for scalable vector graphics, and it is a file format
# this allows you to display vector images on your website


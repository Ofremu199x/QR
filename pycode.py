import pyqrcode 
import png

from pyqrcode import QRCode

QRstring = "https://www.tdmu.edu.ua/en/"
url = pyqrcode.create(QRstring)
url.png('tdmu\\qr.png', scale = 8)

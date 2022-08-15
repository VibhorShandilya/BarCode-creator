import pyqrcode
import png
from pyqrcode import QRCode
vini = "https://forms.gle/2hYVeCLxsiw4hMuf7"
url=pyqrcode.create(vini)
url.png("taru2.png",scale=6)
#You should have python installed in your desktop/laptop
# module to be install
# 1)pyqrcode :- pip install pyqrcode 2)png :- pip install pypng
import pyqrcode
import png
from pyqrcode import QRCode
vini = "https://www.linkedin.com/in/vibhor-shandilya-032801164/"
url=pyqrcode.create(vini)
url.png("anyname.png",scale=6)

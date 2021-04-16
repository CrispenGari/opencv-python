from pyqrcode import QRCode
import random
class QRCodeGenerator(object):
    def __init__(self, name=str(random.randint(10, 1000))):
        self.name = name
    def generate(self):
        qr = QRCode(self.name)
        qr.png('./images/'+self.name+'.png', scale=10)
        return
qr = QRCodeGenerator()
qr.generate()
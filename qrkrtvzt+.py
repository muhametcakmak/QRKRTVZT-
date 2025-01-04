import qrcode
from pystyle import *
from console.utils import set_title
import cv2
import os

class yazilim:
    def giris():

        os.system("cls" if os.name == "nt" else "clear")

        menu_rsm="""
      /$$$$$$  /$$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$$  /$$$$$$$$ /$$    /$$ /$$$$$$$$/$$$$$$$$       
     /$$__  $$| $$__  $$| $$  /$$/ /$$__  $$| $$__  $$|__  $$__/| $$   | $$|_____ $$|__  $$__/ /$$   
    | $$  | $$| $$$$$$$/| $$$$$/  | $$$$$$$$| $$$$$$$/   | $$   |  $$ / $$/    /$$/    | $$ /$$$$$$$$
    | $$  | $$| $$__  $$| $$  $$  | $$__  $$| $$__  $$   | $$    \  $$ $$/    /$$/     | $$|__  $$__/ 
    |  $$$$$$/| $$  | $$| $$ \  $$| $$  | $$| $$  | $$   | $$      \  $/    /$$$$$$$$  | $$   |__/   
     \____ $$$|__/  |__/|__/  \__/|__/  |__/|__/  |__/   |__/       \_/    |________/  |__/          
          \__/ """                   
        set_title("QRKARTVİZİT+")
        Write.Print(Center.XCenter(menu_rsm), Colors.purple_to_red, interval=0.000000001)
        Write.Print(Center.XCenter("Lütfen bilgilerinizi eksiksiz ve doğru giriniz!\n\n"), Colors.purple_to_red, interval=0.00001)

    def sgiriş():
        os.system("cls" if os.name == "nt" else "clear")

        menu_rsm="""
      /$$$$$$  /$$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$$  /$$$$$$$$ /$$    /$$ /$$$$$$$$/$$$$$$$$       
     /$$__  $$| $$__  $$| $$  /$$/ /$$__  $$| $$__  $$|__  $$__/| $$   | $$|_____ $$|__  $$__/ /$$   
    | $$  | $$| $$$$$$$/| $$$$$/  | $$$$$$$$| $$$$$$$/   | $$   |  $$ / $$/    /$$/    | $$ /$$$$$$$$
    | $$  | $$| $$__  $$| $$  $$  | $$__  $$| $$__  $$   | $$    \  $$ $$/    /$$/     | $$|__  $$__/ 
    |  $$$$$$/| $$  | $$| $$ \  $$| $$  | $$| $$  | $$   | $$      \  $/    /$$$$$$$$  | $$   |__/   
     \____ $$$|__/  |__/|__/  \__/|__/  |__/|__/  |__/   |__/       \_/    |________/  |__/          
          \__/ """                 
        Write.Print(Center.XCenter(menu_rsm), Colors.purple_to_red, interval=0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
        Write.Print(Center.XCenter("Lütfen bilgilerinizi eksiksiz ve doğru giriniz!\n\n"), Colors.purple_to_red, interval=0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)     

    def bilgi_alma():
        global ad
        global sad
        global tel
        global isyeri
        global isi
        global bc
        global fc
        
        ad = str(Write.Input("\n\n                   Adı: ", Colors.purple_to_red, interval=0.0001))
        sad = str(Write.Input("\n                   Soyadı: ", Colors.purple_to_red, interval=0.0001))
        tel = str(Write.Input("\n                   Telefon Num: ", Colors.purple_to_red, interval=0.0001))
        isyeri = str(Write.Input("\n                   Çalıştığı Yer: ", Colors.purple_to_red, interval=0.0001))
        isi = str(Write.Input("\n                   İşi: ", Colors.purple_to_red, interval=0.0001))
        bc = str(Write.Input("\n                   Arkaplan Renk: ", Colors.purple_to_red, interval=0.0001))
        fc = str(Write.Input("\n                   Çizgi Renk: ", Colors.purple_to_red, interval=0.0001))
    def qrqode():
        code = qrcode.QRCode(
        version=1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1
        )
        txt = """BEGIN:VCARD
VERSION:2.1
N:{};{};;;
FN:{} {}
TEL;CELL:+90{}
ORG:{}
TITLE:{}
END:VCARD""".format(sad,ad,ad,sad,tel,isyeri,isi)
        code.add_data(txt)
        code.make(fit=True)

        image = code.make_image(fill_color= fc, back_color=bc)

        image.save("{}_{}.png".format(sad,ad))
        resim = cv2.imread("{}_{}.png".format(sad,ad))
        cv2.imshow("QRCODE", resim)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    giris()
    bilgi_alma()         
    qrqode()
    while True:
        sgiriş()
        bilgi_alma()         
        qrqode()
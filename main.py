import cv2
import qrcode


print("***QR Code Generate & Read***")
print("---Place your file in directory!---\n")


def qr_generator():
    try:
        url = input("\nEnter Link: ")
        image = qrcode.make(url)
        image.save("QRcode.png")
    except:
        print("Try Again!")


def qr_reader():
    try:
        filename = cv2.imread(input("\nEnter File name: "))
        detector = cv2.QRCodeDetector()
        val, p, s, = detector.detectAndDecode(filename)
        print(val)
    except:
        print("File name is check and try again...")
        
        
while True:
    c = input("\nGenerator or Reader? (G\R\exit): ")
    c.lower()
    
    if c == "g":
        qr_generator()
    elif c == "r":
        qr_reader()
    else:
        print("Check and try again...")
        break


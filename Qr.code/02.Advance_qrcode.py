import qrcode 
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.ERROR_CORRECT_H,
                 box_size=10, border=4,)#QRcode is a function of qrcode we give vwesion-1 in this there are most chancess of overlaping error for that i am write error_correction in this we remove QRcode error we alwase set high level error correction 

qr.add_data("https://www.instagram.com/ankitpandey_8/")

# now we make google wing make functio

qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="blue")# give the color 
# saving the image
img.save("Ankit pandey.png")
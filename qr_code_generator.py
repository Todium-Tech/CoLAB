import qrcode
qrcode_obj = qrcode.QRCode(version=1,box_size=10,border=5)
qrcode_obj.add_data("Hi I am Belgin Android")
qrcode_obj.make(fit=True)
imag_ob = qrcode_obj.make_image(fill="black",back_color="white")
imag_ob.save("qrcode.png")
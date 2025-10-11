import qrcode
data=input('Enter the text or the URL: ').strip()
filename=input('Enter the filename: ').strip()
qr=qrcode.QRCode(box_size=10,border=4)
qr.add_data(data)
image=qr.make_image(fill_color='black',back_color='white')
image.save(f'{filename}.jpg',format="JPEG")
print(f'QR saved as {filename}.jpg')
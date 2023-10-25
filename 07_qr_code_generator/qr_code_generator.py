import qrcode


def generate_qrcode(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    image = qr.make_image(fill_color='red', back_color='blue')
    image.save('qrimage.png')


url = input("Enter a url for the QR Code:")

generate_qrcode('exampl.com') # add your URL here

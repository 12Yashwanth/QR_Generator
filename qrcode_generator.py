import qrcode
def generate(URL,file):
    qr=qrcode.QRCode(
        version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,border=4)
    qr.add_data(URL)
    qr.make(fit=True)
    img=qr.make_image(fill_color="black",back_color="white")
    img.save(file)

if __name__=="__main__":
    URL=input("Enter the text to be encoded in QR code: ")
    file=input("Enter the name of the file to save the QR code (with .png extension): ")
    generate(URL,file)
    print(f"QR code generated and saved as {file}")
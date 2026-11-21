import qrcode

import os


def generate_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit= True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as {filename}")



print("What do you want the qrcode for?  ")
print("1. Text or Website link")
print("2. Image")
print("3. Video")

choice = input("Enter 1 , 2 or 3:  ")

if choice == '1':
    data = input("Enter Text or Url: ")
elif choice == '2':
    print("\nMake sure the image is on the internet")
    print("\nIf not upload it on google Drive or Imgur first then try again")
    data = input("Paste image link: ")
    if not data.startswith("http"):
        print("Make sure it begins with http! ")
        data = input("Paste link: ")
elif choice == '3':
    print("\nMake sure the Video is on the internet")
    print("\nIf not upload it on Youtube or Google Drive first then try again")
    data = input("Paste Video link: ")
    if not data.startswith("http"):
        print("Make sure it begins with http! ")
        data = input("Paste link: ")
else:
    print("Invalid Choice run again")
    exit()

filename  =  input("Enter the filename you want to save it as:  ")
if not filename.endswith(".jpg") and not filename.endswith(".png"):
    filename = filename + ".png"

generate_code(data,filename)
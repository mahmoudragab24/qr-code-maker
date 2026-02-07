import qrcode
URL = input("Enter the URL: ")
img = qrcode.make(URL)
file_name = input("Enter the file name (without extension): ")

img.save(file_name + ".png")
print("QR code saved as " + file_name + ".png")
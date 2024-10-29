import qrcode
import qrcode.constants

data = input("Enter the text or URL: ").strip()
file_name = input("Enter the file name: ").strip()

qr = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4
)

qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill_color="black", back_color="white")
image.save(f"{file_name}.jpg")
print(f"QR Code is saved as {file_name}.jpg")


"""
# First solution:

qr = qrcode.make(data)
type(qr)
qr.save(f"{file_name}.png")
"""

"""https://email.seznam.cz/?i&q=label-id%3A258"""
"""https://members.codewithmosh.com/courses/python-projects-for-beginners-1/lectures/56763073"""

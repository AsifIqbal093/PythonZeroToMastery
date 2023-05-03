from PIL import Image, ImageFilter

img = Image.open('./CartoonImages/astro.jpg')
img.thumbnail((400,400))

img.save("./edited/thumbnail.jpg")

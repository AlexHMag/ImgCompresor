from PIL import Image

im = Image.open("imagen.jpg")
im.save("imagen2.jpg", format="JPEG", quality=70)
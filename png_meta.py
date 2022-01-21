from PIL.PngImagePlugin import PngImageFile, PngInfo

targetImage = PngImageFile("princess.png")

metadata = PngInfo()

# print(metadata)
metadata.add_text("Creation Time", "2022:11:21 18:18:18")


targetImage.save("princess4.png", pnginfo=metadata)
targetImage = PngImageFile("princess4.png")
print(targetImage.text)
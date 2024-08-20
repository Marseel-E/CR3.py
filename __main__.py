from CR3 import CR3


RAW: str = "IMG_0738.CR3"
JPEG: str = RAW[:-3] + "JPG"


with open(RAW, "rb") as file:
	file = CR3(file.read())

	file.parse()
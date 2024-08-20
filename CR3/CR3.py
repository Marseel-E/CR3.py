__all__ = ['CR3']


from Utils import mb

from .FTYP import *
from .MOOV import *
from .XPacket import *
from .Preview import *
from .MDAT import *

from pathlib import Path


class CR3:
	def __init__(
		self, 
		data: bytearray
	) -> None:
		"""
			Parses a CR3 file into a python Objects.

			Parameters:
			-----------
				data <bytearray>

			Attributes:
			-----------
				data <bytearray>
				ftyp <CR3.FTYP>
				moov <CR3.MOOV>
				xpacket <CR3.XPacket>
				preview <CR3.Preview>
				mdat <CR3.MDAT>
		"""

		self.data: bytearray = data

		self.ftyp = FTYP(data)
		self.moov = MOOV(data[self.ftyp.size:])
		self.xpacket = XPacket(data[self.moov.size:])
		self.preview = Preview(data[self.xpacket.size:])
		self.mdat = MDAT(data[self.preview.size:])


	@property
	def size(self) -> int:
		"""
			Returns the size of the image file in Mega Bytes (mb).
			
			[!Note]: Returns 0 if the file size is less than 1 mb!
		"""
		
		if len(self.data) < 1048576: # Minimum MB value
			return 0

		return round(mb(len(self.data)))


	def parse(self, text_file: bool = False) -> None:
		"""
			Parses the file binary into readable text.

			Parameters:
			-----------
				[optional] text_file <bool> = False
				-|	Outputs the text into a txt file when True.
		"""

		fields: tuple = (
			self.ftyp,
			self.moov,
			self.xpacket,
			self.preview,
			self.mdat
		)

		if not text_file:
			print(*fields, sep="\n")

			return

		text: str = ""
		for field in fields:
			text += str(field) + "\n"

		with open("CR3_dump.txt", '+w') as file:
			file.write(text)

		print(Path.cwd(), "/CR3_dump.txt", sep="")

		


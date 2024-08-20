__all__ = ['XPacket']


from .ABC import ABC

from Utils import mlen


class XPacket(ABC):
	def __init__(self, data: bytearray) -> None:
		"""
			XPacket data.

			Attributes:
			-----------
				uuid <str>
		"""
		super().__init__(data)

		self.uuid: str = data.hex()

	
	def __str__(self) -> str:
		return self.uuid[:32] + mlen(self.uuid)
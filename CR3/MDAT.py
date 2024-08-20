__all__ = ['MDAT']


from .ABC import ABC


class MDAT(ABC):
	def __init__(self, data: bytearray) -> None:
		"""
			Main data.
		"""
		super().__init__(data)

	
	...
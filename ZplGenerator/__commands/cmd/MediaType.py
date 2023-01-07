from typing import Any, Optional


class MediaType:
	def __init__(self, mediaTypeUsed) -> None:
		"""
		The ^MT command selects the type of media being used in the printer.
		"""
		self.__mediaTypeUsed = mediaTypeUsed

	def __str__(self) -> str:
		format = f"^MT{self.__mediaTypeUsed}"
		return format

from typing import Any, Optional


class UploadGraphics:
	def __init__(self, deviceToStoreGraphic, name, extension) -> None:
		"""
		The ^HY command is an extension of the ^HG command. ^HY is used to upload graphic objects from the printer in any supported format.
		"""
		self.__deviceToStoreGraphic = deviceToStoreGraphic
		self.__name = name
		self.__extension = extension

	def __str__(self) -> str:
		format = f"^HY{self.__deviceToStoreGraphic}:{self.__name}.{self.__extension}"
		return format

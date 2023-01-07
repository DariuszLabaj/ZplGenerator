from typing import Any, Optional


class MediaTracking:
	def __init__(self, mediaBeingUsed, blackMarkOffset) -> None:
		"""
		This command specifies the media type being used and the black mark offset in dots
		"""
		self.__mediaBeingUsed = mediaBeingUsed
		self.__blackMarkOffset = blackMarkOffset

	def __str__(self) -> str:
		format = f"^MN{self.__mediaBeingUsed},{self.__blackMarkOffset}"
		return format

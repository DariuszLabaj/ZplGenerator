from typing import Any, Optional


class LabelLength:
	def __init__(self, length, isLabelWithGap) -> None:
		"""
		The ^LL command defines the length of the label. This command is necessary when using continuous media (media not divided into separate labels by gaps, spaces, notches, slots, or holes). This command is not persistent across a power cycle unless a ^JUS is received.
		"""
		self.__length = length
		self.__isLabelWithGap = isLabelWithGap

	def __str__(self) -> str:
		format = f"^LL{self.__length}.{self.__isLabelWithGap}"
		return format

from typing import Any, Optional


class PresentLengthAddition:
	def __init__(self, additionalEjectLength) -> None:
		"""
		The ~PL command adds an additional amount to how far the paper is ejected during a present cycle. A standard amount of 50 mm is always added to clear the kiosk wall. This amount is added to that 50mm. The total amount of media ejected when a ^PN is executed, then, is 50 mm + ~PL value + ^PN value.
		"""
		self.__additionalEjectLength = additionalEjectLength

	def __str__(self) -> str:
		format = f"~PL{self.__additionalEjectLength}"
		return format

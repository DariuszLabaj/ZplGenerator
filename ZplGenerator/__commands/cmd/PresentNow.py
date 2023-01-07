from typing import Any, Optional


class PresentNow:
	def __init__(self, mediaEjectLength) -> None:
		"""
		The ^PN command causes the printer to run a Presenter cycle. The parameter defines the amount of media ejected. The total amount of media ejected when a ^PN is executed, then, is 50 mm + ~PL value + ^PN value.
		"""
		self.__mediaEjectLength = mediaEjectLength

	def __str__(self) -> str:
		format = f"^PN{self.__mediaEjectLength}"
		return format

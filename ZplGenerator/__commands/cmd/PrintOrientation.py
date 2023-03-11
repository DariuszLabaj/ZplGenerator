from typing import Any, Optional


class PrintOrientation:
	def __init__(self, invertLabel) -> None:
		"""
		The ^PO command inverts the label format 180 degrees. The label appears to be printed upside down. If the original label contains commands such as ^LL, ^LS, ^LT and ^PF, the inverted label output is affected differently.
		"""
		self.__invertLabel = invertLabel

	def __str__(self) -> str:
		format = f"^PO{self.__invertLabel}"
		return format

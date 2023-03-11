from typing import Any, Optional


class SlewGivenNumberOfDotRows:
	def __init__(self, noOfDotsRowsToSlew) -> None:
		"""
		The ^PF command causes the printer to slew labels (move labels at a high speed without printing) a specified number of dot rows from the bottom of the label. This allows faster printing when the bottom portion of a label is blank
		"""
		self.__noOfDotsRowsToSlew = noOfDotsRowsToSlew

	def __str__(self) -> str:
		format = f"^PF{self.__noOfDotsRowsToSlew}"
		return format

from typing import Any, Optional


class PrintingMirrorImageOfLabel:
	def __init__(self, printMirrorImageOfEntireLabel) -> None:
		"""
		The ^PM command prints the entire printable area of the label as a mirror image. This command flips the image from left to right.
		"""
		self.__printMirrorImageOfEntireLabel = printMirrorImageOfEntireLabel

	def __str__(self) -> str:
		format = f"^PM{self.__printMirrorImageOfEntireLabel}"
		return format

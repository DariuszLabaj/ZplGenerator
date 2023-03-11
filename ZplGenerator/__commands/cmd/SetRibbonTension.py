from typing import Any, Optional


class SetRibbonTension:
	def __init__(self, tension) -> None:
		"""
		^JW sets the ribbon tension for the printer it is sent to.
		"""
		self.__tension = tension

	def __str__(self) -> str:
		format = f"^JW{self.__tension}"
		return format

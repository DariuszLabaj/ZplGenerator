from typing import Any, Optional


class DecommissioningMode:
	def __init__(self, printerSerialNumber, noOfTimesForFlashWipe) -> None:
		"""
		This command places the printer into the Decommissioning Mode.
		"""
		self.__printerSerialNumber = printerSerialNumber
		self.__noOfTimesForFlashWipe = noOfTimesForFlashWipe

	def __str__(self) -> str:
		format = f"~PM{self.__printerSerialNumber},{self.__noOfTimesForFlashWipe}"
		return format

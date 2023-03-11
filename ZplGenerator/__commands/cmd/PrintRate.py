from typing import Any, Optional


class PrintRate:
	def __init__(self, printSpeed, slewSpeed, backfeedSpeed) -> None:
		"""
		The ^PR command determines the media and slew speed (feeding a blank label) during printing.
		"""
		self.__printSpeed = printSpeed
		self.__slewSpeed = slewSpeed
		self.__backfeedSpeed = backfeedSpeed

	def __str__(self) -> str:
		format = f"^PR{self.__printSpeed},{self.__slewSpeed},{self.__backfeedSpeed}"
		return format

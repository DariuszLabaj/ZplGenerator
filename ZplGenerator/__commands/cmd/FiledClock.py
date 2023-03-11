from typing import Any, Optional


class FiledClock:
	def __init__(self, primaryClockIndicatorChar, secondaryClockIndicatorChar, thirdClockIndicatorChar) -> None:
		"""
		The ^FC command is used to set the clock-indicators (delimiters) and the clock mode for use with the RealTime Clock hardware. This command must be included within each label field command string each time the Real-Time Clock values are required within the field
		"""
		self.__primaryClockIndicatorChar = primaryClockIndicatorChar
		self.__secondaryClockIndicatorChar = secondaryClockIndicatorChar
		self.__thirdClockIndicatorChar = thirdClockIndicatorChar

	def __str__(self) -> str:
		format = f"^FC{self.__primaryClockIndicatorChar},{self.__secondaryClockIndicatorChar},{self.__thirdClockIndicatorChar}"
		return format

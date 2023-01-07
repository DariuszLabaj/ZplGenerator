from typing import Any, Optional


class SelectDateAndTimeFormat:
	def __init__(self, valueOfDateAndTimeFormat) -> None:
		"""
		The ^KD command selects the format that the Real-Time Clock’s date and time information presents as on a configuration label. This is also displayed on the Printer Idle LCD control panel display, and displayed while setting the date and time
		"""
		self.__valueOfDateAndTimeFormat = valueOfDateAndTimeFormat

	def __str__(self) -> str:
		format = f"^KD{self.__valueOfDateAndTimeFormat}"
		return format

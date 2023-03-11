from typing import Any, Optional


class SetOffset:
	def __init__(self, clockSet, monthOffset, daysOffset, yearsOffset, hoursOffset, minutesOffset, secondsOffset) -> None:
		"""
		The ^SO command is used to set the secondary and the tertiary offset from the primary Real-Time Clock.
		"""
		self.__clockSet = clockSet
		self.__monthOffset = monthOffset
		self.__daysOffset = daysOffset
		self.__yearsOffset = yearsOffset
		self.__hoursOffset = hoursOffset
		self.__minutesOffset = minutesOffset
		self.__secondsOffset = secondsOffset

	def __str__(self) -> str:
		format = f"^SO{self.__clockSet},{self.__monthOffset},{self.__daysOffset},{self.__yearsOffset},{self.__hoursOffset},{self.__minutesOffset},{self.__secondsOffset}"
		return format

from typing import Any, Optional


class SetDateAndTime:
	def __init__(self, month, day, year, hour, minute, second, format) -> None:
		"""
		The ^ST command sets the date and time of the Real-Time Clock.
		"""
		self.__month = month
		self.__day = day
		self.__year = year
		self.__hour = hour
		self.__minute = minute
		self.__second = second
		self.__format = format

	def __str__(self) -> str:
		format = f"^ST{self.__month},{self.__day},{self.__year},{self.__hour},{self.__minute},{self.__second},{self.__format}"
		return format

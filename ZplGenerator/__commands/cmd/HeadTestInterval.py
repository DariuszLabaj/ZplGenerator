from typing import Any, Optional


class HeadTestInterval:
	def __init__(self, value, manualRangeSelect, firstElementToCheck, lastElementToCheck) -> None:
		"""
		The ^JT command allows you to change the printhead test interval from every 100 labels to any desired interval. With the ^JT command, the printer is allowed to run the test after printing a label. When a parameter is defined, the printer runs the test after printing a set amount of labels.
		"""
		self.__value = value
		self.__manualRangeSelect = manualRangeSelect
		self.__firstElementToCheck = firstElementToCheck
		self.__lastElementToCheck = lastElementToCheck

	def __str__(self) -> str:
		format = f"^JT{self.__value},{self.__manualRangeSelect},{self.__firstElementToCheck},{self.__lastElementToCheck}"
		return format

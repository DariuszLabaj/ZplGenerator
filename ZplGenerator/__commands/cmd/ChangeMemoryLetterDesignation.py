from typing import Any, Optional


class ChangeMemoryLetterDesignation:
	def __init__(self, aliasForB, aliasForE, aliasForR, aliasForA, multipleAlias) -> None:
		"""
		The ^CM command allows you to reassign a letter designation to the printer’s memory devices. If a format already exists, you can reassign the memory device to the corresponding letter without forcing, altering, or recreating the format itself.
		"""
		self.__aliasForB = aliasForB
		self.__aliasForE = aliasForE
		self.__aliasForR = aliasForR
		self.__aliasForA = aliasForA
		self.__multipleAlias = multipleAlias

	def __str__(self) -> str:
		format = f"^CM{self.__aliasForB},{self.__aliasForE},{self.__aliasForR},{self.__aliasForA},{self.__multipleAlias}"
		return format

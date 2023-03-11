from typing import Any, Optional


class CacheOn:
	def __init__(self, cacheOn, amountOfAdditionalMemory, cacheType) -> None:
		"""
		The ^CO command is used to change the size of the character cache. By definition, a character cache (referred to as cache) is a portion of the DRAM reserved for storing scalable characters. All printers have a default 40K cache that is always turned on. The maximum single character size that can be stored, without changing the size of the cache, is 450 dots by 450 dots
		"""
		self.__cacheOn = cacheOn
		self.__amountOfAdditionalMemory = amountOfAdditionalMemory
		self.__cacheType = cacheType

	def __str__(self) -> str:
		format = f"^CO{self.__cacheOn},{self.__amountOfAdditionalMemory},{self.__cacheType}"
		return format

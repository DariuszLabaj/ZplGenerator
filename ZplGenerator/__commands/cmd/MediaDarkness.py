from typing import Any, Optional


class MediaDarkness:
	def __init__(self, mediaDarknessLevel) -> None:
		"""
		The ^MD command adjusts the darkness relative to the current darkness setting.
		"""
		self.__mediaDarknessLevel = mediaDarknessLevel

	def __str__(self) -> str:
		format = f"^MD{self.__mediaDarknessLevel}"
		return format

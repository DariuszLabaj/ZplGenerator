from typing import Any, Optional


class FontLinking:
	def __init__(self, origFontPath, linkFontPath, link) -> None:
		"""
		The ^FL command provides the ability to link any TrueType font, including private character fonts, to associated fonts
		"""
		self.__origFontPath = origFontPath
		self.__linkFontPath = linkFontPath
		self.__link = link

	def __str__(self) -> str:
		format = f"^FL{self.__origFontPath},{self.__linkFontPath},{self.__link}"
		return format

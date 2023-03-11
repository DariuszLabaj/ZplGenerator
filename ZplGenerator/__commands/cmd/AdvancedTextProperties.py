from typing import Any, Optional


class AdvancedTextProperties:
	def __init__(self, defaultGlyph, bidirectionalTextLayout, characterShaping, openTypeTableSupport) -> None:
		"""
		The ^PA command is used to configure advanced text layout features.
		"""
		self.__defaultGlyph = defaultGlyph
		self.__bidirectionalTextLayout = bidirectionalTextLayout
		self.__characterShaping = characterShaping
		self.__openTypeTableSupport = openTypeTableSupport

	def __str__(self) -> str:
		format = f"^PA{self.__defaultGlyph},{self.__bidirectionalTextLayout},{self.__characterShaping},{self.__openTypeTableSupport}"
		return format

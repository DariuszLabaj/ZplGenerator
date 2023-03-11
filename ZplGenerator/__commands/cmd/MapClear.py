from typing import Any, Optional


class MapClear:
	def __init__(self, mapClear) -> None:
		"""
		In normal operation, the bitmap is cleared after the format has been printed. The ^MC command is used to retain the current bitmap. This applies to current and subsequent labels until cleared with ^MCY.
		"""
		self.__mapClear = mapClear

	def __str__(self) -> str:
		format = f"^MC{self.__mapClear}"
		return format

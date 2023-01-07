from typing import Any, Optional


class CutNow:
	def __init__(self, cutModeOverride) -> None:
		"""
		The ^CN causes the printer to cycle the media cutter
		"""
		self.__cutModeOverride = cutModeOverride

	def __str__(self) -> str:
		format = f"^CN{self.__cutModeOverride}"
		return format

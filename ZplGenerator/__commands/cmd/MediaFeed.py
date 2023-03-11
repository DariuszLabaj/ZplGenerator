from typing import Any, Optional


class MediaFeed:
	def __init__(self, feedActionAtPowerUp, feedActionAfterClosingPrinthead) -> None:
		"""
		The ^MF command dictates what happens to the media at power-up and at head-close after the error clears
		"""
		self.__feedActionAtPowerUp = feedActionAtPowerUp
		self.__feedActionAfterClosingPrinthead = feedActionAfterClosingPrinthead

	def __str__(self) -> str:
		format = f"^MF{self.__feedActionAtPowerUp},{self.__feedActionAfterClosingPrinthead}"
		return format

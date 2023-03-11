from typing import Any, Optional


class KioskValues:
	def __init__(self, kioskCutAmount, kioskCutMargin, kioskPresentType, kioskPresentTimeout, presentLoopLength) -> None:
		"""
		The ^KV command sets several parameters that affect the printers operation when ^MM is set to K - Kiosk mode
		"""
		self.__kioskCutAmount = kioskCutAmount
		self.__kioskCutMargin = kioskCutMargin
		self.__kioskPresentType = kioskPresentType
		self.__kioskPresentTimeout = kioskPresentTimeout
		self.__presentLoopLength = presentLoopLength

	def __str__(self) -> str:
		format = f"^KV{self.__kioskCutAmount},{self.__kioskCutMargin},{self.__kioskPresentType},{self.__kioskPresentTimeout},{self.__presentLoopLength}"
		return format

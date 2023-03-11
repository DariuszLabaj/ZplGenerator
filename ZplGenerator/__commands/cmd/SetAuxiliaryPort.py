from typing import Any, Optional


class SetAuxiliaryPort:
	def __init__(self, auxPortMode, appMode, startPrintSignal, errorMode, reprintMode, ribbonLowMode) -> None:
		"""
		The ^JJ command allows you to control an online verifier or applicator device
		"""
		self.__auxPortMode = auxPortMode
		self.__appMode = appMode
		self.__startPrintSignal = startPrintSignal
		self.__errorMode = errorMode
		self.__reprintMode = reprintMode
		self.__ribbonLowMode = ribbonLowMode

	def __str__(self) -> str:
		format = f"^JJ{self.__auxPortMode},{self.__appMode},{self.__startPrintSignal},{self.__errorMode},{self.__reprintMode},{self.__ribbonLowMode}"
		return format

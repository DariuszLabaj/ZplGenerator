from typing import Any, Optional


class PrinterSleep:
	def __init__(self, noOfSeocndPriorToShutdown, labelStatusAtShutdown) -> None:
		"""
		The ^ZZ command places the printer in an idle or shutdown mode
		"""
		self.__noOfSeocndPriorToShutdown = noOfSeocndPriorToShutdown
		self.__labelStatusAtShutdown = labelStatusAtShutdown

	def __str__(self) -> str:
		format = f"^ZZ{self.__noOfSeocndPriorToShutdown},{self.__labelStatusAtShutdown}"
		return format

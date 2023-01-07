from typing import Any, Optional


class PrintQuantity:
	def __init__(self, noOfLabelsToPrint, pauseAndCutValue, replicatesOfEachSerialNumber, overridePauseCount, cutOnErrorLabel) -> None:
		"""
		The ^PQ command gives control over several printing operations. It controls the number of labels to print, the number of labels printed before printer pauses, and the number of replications of each serial number
		"""
		self.__noOfLabelsToPrint = noOfLabelsToPrint
		self.__pauseAndCutValue = pauseAndCutValue
		self.__replicatesOfEachSerialNumber = replicatesOfEachSerialNumber
		self.__overridePauseCount = overridePauseCount
		self.__cutOnErrorLabel = cutOnErrorLabel

	def __str__(self) -> str:
		format = f"^PQ{self.__noOfLabelsToPrint},{self.__pauseAndCutValue},{self.__replicatesOfEachSerialNumber},{self.__overridePauseCount},{self.__cutOnErrorLabel}"
		return format

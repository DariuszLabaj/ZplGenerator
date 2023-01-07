from typing import Any, Optional


class SetSerialCommunications:
	def __init__(self, baudRate, wordLength, parity, stopBits, protocolMode, zebraProtocol) -> None:
		"""
		The ^SC command allows you to change the serial communications parameters you are using.
		"""
		self.__baudRate = baudRate
		self.__wordLength = wordLength
		self.__parity = parity
		self.__stopBits = stopBits
		self.__protocolMode = protocolMode
		self.__zebraProtocol = zebraProtocol

	def __str__(self) -> str:
		format = f"^SC{self.__baudRate},{self.__wordLength},{self.__parity},{self.__stopBits},{self.__protocolMode},{self.__zebraProtocol}"
		return format

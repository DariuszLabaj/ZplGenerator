from typing import Any, Optional


class HostVerification:
	def __init__(self, fieldNumber, noOfBytes, headerNo, termination, cmdApplyTo) -> None:
		"""
		Use this command to return data from specified fields, along with an optional ASCII header, to the host computer. You can use this command with any field that has been assigned a number with the ^FN and ^RF commands
		"""
		self.__fieldNumber = fieldNumber
		self.__noOfBytes = noOfBytes
		self.__headerNo = headerNo
		self.__termination = termination
		self.__cmdApplyTo = cmdApplyTo

	def __str__(self) -> str:
		format = f"^HV{self.__fieldNumber},{self.__noOfBytes},{self.__headerNo},{self.__termination},{self.__cmdApplyTo}"
		return format

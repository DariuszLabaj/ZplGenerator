from typing import Any, Optional


class SerializationData:
	def __init__(self, staringString, incrementValue, addLeadingZeros) -> None:
		"""
		The ^SN command allows the printer to index data fields by a selected increment or decrement value, making the data fields increase or decrease by a specified value each time a label is printed. This can be performed on 100 to 150 fields in a given format and can be performed on both alphanumeric and bar code fields. A maximum of 12 of the right- most integers are subject to indexing.
		"""
		self.__staringString = staringString
		self.__incrementValue = incrementValue
		self.__addLeadingZeros = addLeadingZeros

	def __str__(self) -> str:
		format = f"^SN{self.__staringString},{self.__incrementValue},{self.__addLeadingZeros}"
		return format

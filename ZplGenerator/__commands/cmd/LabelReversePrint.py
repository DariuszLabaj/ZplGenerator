from typing import Any, Optional


class LabelReversePrint:
	def __init__(self, reversePrintAllFields) -> None:
		"""
		The ^LR command reverses the printing of all fields in the label format. It allows a field to appear as white over black or black over white.
		"""
		self.__reversePrintAllFields = reversePrintAllFields

	def __str__(self) -> str:
		format = f"^LR{self.__reversePrintAllFields}"
		return format

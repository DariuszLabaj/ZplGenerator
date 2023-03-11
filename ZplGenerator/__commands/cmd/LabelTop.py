from typing import Any, Optional


class LabelTop:
	def __init__(self, labelTop) -> None:
		"""
		The ^LT command moves the entire label format a maximum of 120 dot rows up or down from its current position, in relation to the top edge of the label. A negative value moves the format towards the top of the label; a positive value moves the format away from the top of the label.
		"""
		self.__labelTop = labelTop

	def __str__(self) -> str:
		format = f"^LT{self.__labelTop}"
		return format

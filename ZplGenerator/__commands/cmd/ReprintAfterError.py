from typing import Any, Optional


class ReprintAfterError:
	def __init__(self, reprintAfterError) -> None:
		"""
		The ^JZ command reprints a partially printed label caused by a Ribbon Out, Media Out, or Head Open error condition. The label is reprinted as soon as the error condition is corrected
		"""
		self.__reprintAfterError = reprintAfterError

	def __str__(self) -> str:
		format = f"^JZ{self.__reprintAfterError}"
		return format

from typing import Any, Optional


class AbortDownloadGraphic:
	def __init__(self, ) -> None:
		"""
		After decoding and printing the number of bytes in parameter t of the ~DG command, the printer returns to normal Print Mode. Graphics Mode can be aborted and normal printer operation resumed by using the ~DN command
		"""
pass

	def __str__(self) -> str:
		format = f"~DN"
		return format

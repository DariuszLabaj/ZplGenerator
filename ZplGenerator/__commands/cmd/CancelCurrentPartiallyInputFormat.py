from typing import Any, Optional


class CancelCurrentPartiallyInputFormat:
	def __init__(self, ) -> None:
		"""
		The ~JX command cancels a format currently being sent to the printer. It does not affect any formats currently being printed, or any subsequent formats that might be sent.
		"""
pass

	def __str__(self) -> str:
		format = f"~JX"
		return format

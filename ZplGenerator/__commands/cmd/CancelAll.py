from typing import Any, Optional


class CancelAll:
	def __init__(self, ) -> None:
		"""
		The ~JA command cancels all format commands in the buffer. It also cancels any batches that are printing
		"""
pass

	def __str__(self) -> str:
		format = f"~JA"
		return format

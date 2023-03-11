from typing import Any, Optional


class DisableDiagnostics:
	def __init__(self, ) -> None:
		"""
		The ~JE command cancels Diagnostic Mode and returns the printer to normal label printing
		"""
pass

	def __str__(self) -> str:
		format = f"~JE"
		return format

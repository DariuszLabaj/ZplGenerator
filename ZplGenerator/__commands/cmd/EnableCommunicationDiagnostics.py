from typing import Any, Optional


class EnableCommunicationDiagnostics:
	def __init__(self, ) -> None:
		"""
		The ~JD command initiates Diagnostic Mode, which produces an ASCII printout (using current label length and full width of printer) of all characters received by the printer. This printout includes the ASCII characters, the hexadecimal value, and any communication errors.
		"""
pass

	def __str__(self) -> str:
		format = f"~JD"
		return format

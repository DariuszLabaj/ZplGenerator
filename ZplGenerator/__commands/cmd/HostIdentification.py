from typing import Any, Optional


class HostIdentification:
	def __init__(self, ) -> None:
		"""
		The ~HI command is designed to be sent from the host to the Zebra printer to retrieve information. Upon receipt, the printer responds with information on the model, software version, dots-per-millimeter setting, memory size, and any detected options.
		"""
pass

	def __str__(self) -> str:
		format = f"~HI"
		return format

from typing import Any, Optional


class PrintConfigurationLabel:
	def __init__(self, ) -> None:
		"""
		The ~WC command is used to generate a printer configuration label. The printer configuration label contains information about the printer setup, such as sensor type, network ID, ZPL mode, firmware version, and descriptive data on the R:, E:, B:, and A: devices
		"""
pass

	def __str__(self) -> str:
		format = f"~WC"
		return format

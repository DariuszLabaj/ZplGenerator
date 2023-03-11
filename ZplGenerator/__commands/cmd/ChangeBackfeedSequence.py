from typing import Any, Optional


class ChangeBackfeedSequence:
	def __init__(self, backfeedOrder) -> None:
		"""
		The ~JS command is used to control the backfeed sequence. This command can be used on printers with or without built-in cutters. This command is ignored on the HC100™ printer.
		"""
		self.__backfeedOrder = backfeedOrder

	def __str__(self) -> str:
		format = f"~JS{self.__backfeedOrder}"
		return format

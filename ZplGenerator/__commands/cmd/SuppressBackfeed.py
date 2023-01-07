from typing import Any, Optional


class SuppressBackfeed:
	def __init__(self, ) -> None:
		"""
		The ^XB command suppresses forward feed of media to tear-off position depending on the current printer mode. Because no forward feed occurs, a backfeed before printing of the next label is not necessary; this improves throughput. When printing a batch of labels, the last label should not contain this command.
		"""
pass

	def __str__(self) -> str:
		format = f"^XB"
		return format

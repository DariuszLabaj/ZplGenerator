from typing import Any, Optional


class ChangeNetworkSettings:
	def __init__(self, deviceBeingModified, IpResolution, IpAddress, subnetMask, defaultGateway, WinsServerAddress, connectionTimeoutChecking, timeoutValue, ArpBroadcastInterval, baseRawPOrtNumber) -> None:
		"""
		The ^ND command changes the network settings on supported printers
		"""
		self.__deviceBeingModified = deviceBeingModified
		self.__IpResolution = IpResolution
		self.__IpAddress = IpAddress
		self.__subnetMask = subnetMask
		self.__defaultGateway = defaultGateway
		self.__WinsServerAddress = WinsServerAddress
		self.__connectionTimeoutChecking = connectionTimeoutChecking
		self.__timeoutValue = timeoutValue
		self.__ArpBroadcastInterval = ArpBroadcastInterval
		self.__baseRawPOrtNumber = baseRawPOrtNumber

	def __str__(self) -> str:
		format = f"^ND{self.__deviceBeingModified},{self.__IpResolution},{self.__IpAddress},{self.__subnetMask},{self.__defaultGateway},{self.__WinsServerAddress},{self.__connectionTimeoutChecking},{self.__timeoutValue},{self.__ArpBroadcastInterval},{self.__baseRawPOrtNumber}"
		return format

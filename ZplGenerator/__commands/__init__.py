from ZplGenerator.__commands.__static import ALL_COMMANDS
from ZplGenerator.__commands.__static import ALPHANUMERIC
from ZplGenerator.__commands.__static import BARCODE_CREATING_COMMANDS
from ZplGenerator.__commands.__static import CARET_CHAR
from ZplGenerator.__commands.__static import CTR_CMD_CHAR
from ZplGenerator.__commands.__static import DELIMITER_CHAR
from ZplGenerator.__commands.__static import DOTS_VALUE_RANGE
from ZplGenerator.__commands.__static import HEX_IND_CHAR
from ZplGenerator.__commands.__static import ORIENTATIONS
from ZplGenerator.__commands.cmd.ScalableFontCommand import ScalableFontCommand
from ZplGenerator.__commands.cmd.ScalableFontCommandByName import ScalableFontCommandByName
from ZplGenerator.__commands.cmd.AztecBarcodeParameters import AztecBarcodeParameters
from ZplGenerator.__commands.cmd.Code11Barcode import Code11Barcode
from ZplGenerator.__commands.cmd.Interleaved2Of5Barcode import Interleaved2Of5Barcode
from ZplGenerator.__commands.cmd.Code39Barcode import Code39Barcode
from ZplGenerator.__commands.cmd.Code49Barcode import Code49Barcode
from ZplGenerator.__commands.cmd.PlanetCodeBarcode import PlanetCodeBarcode
from ZplGenerator.__commands.cmd.PDF417Barcode import PDF417Barcode
from ZplGenerator.__commands.cmd.EAN8Barcode import EAN8Barcode
from ZplGenerator.__commands.cmd.UPCeBarcode import UPCeBarcode
from ZplGenerator.__commands.cmd.Code93Barcode import Code93Barcode
from ZplGenerator.__commands.cmd.CodaBlockBarcode import CodaBlockBarcode
from ZplGenerator.__commands.cmd.Code128Barcode import Code128Barcode
from ZplGenerator.__commands.cmd.UpsMaxiCodeBarcode import UpsMaxiCodeBarcode
from ZplGenerator.__commands.cmd.EAN13Barcode import EAN13Barcode
from ZplGenerator.__commands.cmd.MicroPDF417Barcode import MicroPDF417Barcode
from ZplGenerator.__commands.cmd.Industrial2Of5Barcode import Industrial2Of5Barcode
from ZplGenerator.__commands.cmd.Standard2Of5Barcode import Standard2Of5Barcode
from ZplGenerator.__commands.cmd.AnsiCodaBarBarcode import AnsiCodaBarBarcode
from ZplGenerator.__commands.cmd.LogMarsBarcode import LogMarsBarcode
from ZplGenerator.__commands.cmd.MsiBarcode import MsiBarcode
from ZplGenerator.__commands.cmd.PlesseyBarcode import PlesseyBarcode
from ZplGenerator.__commands.cmd.QrCodeBarcode import QrCodeBarcode
from ZplGenerator.__commands.cmd.Gs1Barcode import Gs1Barcode
from ZplGenerator.__commands.cmd.Upc_EanExtensions import Upc_EanExtensions
from ZplGenerator.__commands.cmd.TLC39Barcode import TLC39Barcode
from ZplGenerator.__commands.cmd.UpcABarcode import UpcABarcode
from ZplGenerator.__commands.cmd.DataMatrixBarcode import DataMatrixBarcode
from ZplGenerator.__commands.cmd.BarcodeFieldDefault import BarcodeFieldDefault
from ZplGenerator.__commands.cmd.PostalBarcode import PostalBarcode
from ZplGenerator.__commands.cmd.ChangeCaret import ChangeCaret
from ZplGenerator.__commands.cmd.ChangeDelimiter import ChangeDelimiter
from ZplGenerator.__commands.cmd.ChangeAlphanumericDefaultFont import ChangeAlphanumericDefaultFont
from ZplGenerator.__commands.cmd.ChangeInternationalFontEncoding import ChangeInternationalFontEncoding
from ZplGenerator.__commands.cmd.ChangeMemoryLetterDesignation import ChangeMemoryLetterDesignation
from ZplGenerator.__commands.cmd.CutNow import CutNow
from ZplGenerator.__commands.cmd.CacheOn import CacheOn
from ZplGenerator.__commands.cmd.RemoveLabel import RemoveLabel
from ZplGenerator.__commands.cmd.ChangeControlCommandCharacter import ChangeControlCommandCharacter
from ZplGenerator.__commands.cmd.CodeValidation import CodeValidation
from ZplGenerator.__commands.cmd.FontIdentifier import FontIdentifier
from ZplGenerator.__commands.cmd.DownloadBitmapFont import DownloadBitmapFont
from ZplGenerator.__commands.cmd.DownloadEncoding import DownloadEncoding
from ZplGenerator.__commands.cmd.DownloadFormat import DownloadFormat
from ZplGenerator.__commands.cmd.DownloadGraphics import DownloadGraphics
from ZplGenerator.__commands.cmd.AbortDownloadGraphic import AbortDownloadGraphic
from ZplGenerator.__commands.cmd.DownloadScalableFont import DownloadScalableFont
from ZplGenerator.__commands.cmd.DownloadBoundedTrueTypeFont import DownloadBoundedTrueTypeFont
from ZplGenerator.__commands.cmd.DownloadUnboundedTrueTypeFont import DownloadUnboundedTrueTypeFont
from ZplGenerator.__commands.cmd.DownloadObjects import DownloadObjects
from ZplGenerator.__commands.cmd.EraseDownloadGraphics import EraseDownloadGraphics
from ZplGenerator.__commands.cmd.FieldBlock import FieldBlock
from ZplGenerator.__commands.cmd.FiledClock import FiledClock
from ZplGenerator.__commands.cmd.FiledData import FiledData
from ZplGenerator.__commands.cmd.FieldHexadecimalIndicator import FieldHexadecimalIndicator
from ZplGenerator.__commands.cmd.FontLinking import FontLinking
from ZplGenerator.__commands.cmd.MultipleFieldOriginLocations import MultipleFieldOriginLocations
from ZplGenerator.__commands.cmd.FieldNumber import FieldNumber
from ZplGenerator.__commands.cmd.FieldOrigin import FieldOrigin
from ZplGenerator.__commands.cmd.FieldParameter import FieldParameter
from ZplGenerator.__commands.cmd.FieldReversePrint import FieldReversePrint
from ZplGenerator.__commands.cmd.FieldSeparator import FieldSeparator
from ZplGenerator.__commands.cmd.FieldTypeset import FieldTypeset
from ZplGenerator.__commands.cmd.FieldVariable import FieldVariable
from ZplGenerator.__commands.cmd.FieldOrientation import FieldOrientation
from ZplGenerator.__commands.cmd.Comment import Comment
from ZplGenerator.__commands.cmd.GraphicBox import GraphicBox
from ZplGenerator.__commands.cmd.GraphicCircle import GraphicCircle
from ZplGenerator.__commands.cmd.GraphicDiagonalLine import GraphicDiagonalLine
from ZplGenerator.__commands.cmd.GraphicEllipse import GraphicEllipse
from ZplGenerator.__commands.cmd.GraphicField import GraphicField
from ZplGenerator.__commands.cmd.GraphicSymbol import GraphicSymbol
from ZplGenerator.__commands.cmd.BatteryStatus import BatteryStatus
from ZplGenerator.__commands.cmd.HeadDiagnostic import HeadDiagnostic
from ZplGenerator.__commands.cmd.HostFormat import HostFormat
from ZplGenerator.__commands.cmd.HostGraphic import HostGraphic
from ZplGenerator.__commands.cmd.ConfigurationLabelReturn import ConfigurationLabelReturn
from ZplGenerator.__commands.cmd.HostIdentification import HostIdentification
from ZplGenerator.__commands.cmd.HostRamStatus import HostRamStatus
from ZplGenerator.__commands.cmd.HostQuery import HostQuery
from ZplGenerator.__commands.cmd.HostStatusReturn import HostStatusReturn
from ZplGenerator.__commands.cmd.HostLinkedFontsList import HostLinkedFontsList
from ZplGenerator.__commands.cmd.ZebraNetAlertConfiguration import ZebraNetAlertConfiguration
from ZplGenerator.__commands.cmd.HostVerification import HostVerification
from ZplGenerator.__commands.cmd.HostDirectoryList import HostDirectoryList
from ZplGenerator.__commands.cmd.UploadGraphics import UploadGraphics
from ZplGenerator.__commands.cmd.DisplayDescriptionInformation import DisplayDescriptionInformation
from ZplGenerator.__commands.cmd.ObjectDelete import ObjectDelete
from ZplGenerator.__commands.cmd.ImageLoad import ImageLoad
from ZplGenerator.__commands.cmd.ImageMove import ImageMove
from ZplGenerator.__commands.cmd.ImageSave import ImageSave
from ZplGenerator.__commands.cmd.CancelAll import CancelAll
from ZplGenerator.__commands.cmd.InitializeFlashMemory import InitializeFlashMemory
from ZplGenerator.__commands.cmd.ResetOptionalMemory import ResetOptionalMemory
from ZplGenerator.__commands.cmd.SetMediaSensorCalibration import SetMediaSensorCalibration
from ZplGenerator.__commands.cmd.EnableCommunicationDiagnostics import EnableCommunicationDiagnostics
from ZplGenerator.__commands.cmd.DisableDiagnostics import DisableDiagnostics
from ZplGenerator.__commands.cmd.SetBatteryCondition import SetBatteryCondition
from ZplGenerator.__commands.cmd.GraphicSensorCalibration import GraphicSensorCalibration
from ZplGenerator.__commands.cmd.EarlyWarningSetting import EarlyWarningSetting
from ZplGenerator.__commands.cmd.StartZBI import StartZBI
from ZplGenerator.__commands.cmd.SetAuxiliaryPort import SetAuxiliaryPort
from ZplGenerator.__commands.cmd.SetLabelLength import SetLabelLength
from ZplGenerator.__commands.cmd.SetDotsPerMillimeter import SetDotsPerMillimeter
from ZplGenerator.__commands.cmd.HeadTestFatal import HeadTestFatal
from ZplGenerator.__commands.cmd.HeadTestNonFatal import HeadTestNonFatal
from ZplGenerator.__commands.cmd.PauseAndCancelFormat import PauseAndCancelFormat
from ZplGenerator.__commands.cmd.TerminateZebraBasicInterpreter import TerminateZebraBasicInterpreter
from ZplGenerator.__commands.cmd.PowerOnReset import PowerOnReset
from ZplGenerator.__commands.cmd.SensorSelect import SensorSelect
from ZplGenerator.__commands.cmd.ChangeBackfeedSequence import ChangeBackfeedSequence
from ZplGenerator.__commands.cmd.HeadTestInterval import HeadTestInterval
from ZplGenerator.__commands.cmd.ConfigurationUpdate import ConfigurationUpdate
from ZplGenerator.__commands.cmd.SetRibbonTension import SetRibbonTension
from ZplGenerator.__commands.cmd.CancelCurrentPartiallyInputFormat import CancelCurrentPartiallyInputFormat
from ZplGenerator.__commands.cmd.ReprintAfterError import ReprintAfterError
from ZplGenerator.__commands.cmd.KillBattery import KillBattery
from ZplGenerator.__commands.cmd.SelectDateAndTimeFormat import SelectDateAndTimeFormat
from ZplGenerator.__commands.cmd.DefineLanguage import DefineLanguage
from ZplGenerator.__commands.cmd.DefinePrinterName import DefinePrinterName
from ZplGenerator.__commands.cmd.DefinePassword import DefinePassword
from ZplGenerator.__commands.cmd.KioskValues import KioskValues
from ZplGenerator.__commands.cmd.ListFontLinks import ListFontLinks
from ZplGenerator.__commands.cmd.LabelHome import LabelHome
from ZplGenerator.__commands.cmd.LabelLength import LabelLength
from ZplGenerator.__commands.cmd.LabelReversePrint import LabelReversePrint
from ZplGenerator.__commands.cmd.LabelShift import LabelShift
from ZplGenerator.__commands.cmd.LabelTop import LabelTop
from ZplGenerator.__commands.cmd.SetMaintenanceAlerts import SetMaintenanceAlerts
from ZplGenerator.__commands.cmd.MapClear import MapClear
from ZplGenerator.__commands.cmd.MediaDarkness import MediaDarkness
from ZplGenerator.__commands.cmd.MediaFeed import MediaFeed
from ZplGenerator.__commands.cmd.SetMaintenanceInformationMessage import SetMaintenanceInformationMessage
from ZplGenerator.__commands.cmd.MaximumLabelLength import MaximumLabelLength
from ZplGenerator.__commands.cmd.PrintMode import PrintMode
from ZplGenerator.__commands.cmd.MediaTracking import MediaTracking
from ZplGenerator.__commands.cmd.ModeProtection import ModeProtection
from ZplGenerator.__commands.cmd.MediaType import MediaType
from ZplGenerator.__commands.cmd.SetUnitOfMeasurement import SetUnitOfMeasurement
from ZplGenerator.__commands.cmd.ModifyHeadColdWarning import ModifyHeadColdWarning
from ZplGenerator.__commands.cmd.SelectPrimaryNetworkDevice import SelectPrimaryNetworkDevice
from ZplGenerator.__commands.cmd.NetworkConnect import NetworkConnect
from ZplGenerator.__commands.cmd.ChangeNetworkSettings import ChangeNetworkSettings
from ZplGenerator.__commands.cmd.NetworkIdNumber import NetworkIdNumber
from ZplGenerator.__commands.cmd.SetAllNetworkPrintersTransparent import SetAllNetworkPrintersTransparent
from ZplGenerator.__commands.cmd.ChangeWiredNetworkingSettings import ChangeWiredNetworkingSettings
from ZplGenerator.__commands.cmd.SetCurrentConnectedPrinterTransparent import SetCurrentConnectedPrinterTransparent
from ZplGenerator.__commands.cmd.AdvancedTextProperties import AdvancedTextProperties
from ZplGenerator.__commands.cmd.SlewGivenNumberOfDotRows import SlewGivenNumberOfDotRows
from ZplGenerator.__commands.cmd.SlewToHomePosition import SlewToHomePosition
from ZplGenerator.__commands.cmd.PresentLengthAddition import PresentLengthAddition
from ZplGenerator.__commands.cmd.PrintingMirrorImageOfLabel import PrintingMirrorImageOfLabel
from ZplGenerator.__commands.cmd.DecommissioningMode import DecommissioningMode
from ZplGenerator.__commands.cmd.PresentNow import PresentNow
from ZplGenerator.__commands.cmd.PrintOrientation import PrintOrientation
from ZplGenerator.__commands.cmd.ProgramablePause import ProgramablePause
from ZplGenerator.__commands.cmd.PrintQuantity import PrintQuantity
from ZplGenerator.__commands.cmd.ApplicatorReprint import ApplicatorReprint
from ZplGenerator.__commands.cmd.PrintRate import PrintRate
from ZplGenerator.__commands.cmd.PrintStart import PrintStart
from ZplGenerator.__commands.cmd.PrintWidth import PrintWidth
from ZplGenerator.__commands.cmd.ResetAdvancedCounters import ResetAdvancedCounters
from ZplGenerator.__commands.cmd.SetSerialCommunications import SetSerialCommunications
from ZplGenerator.__commands.cmd.SetDarkness import SetDarkness
from ZplGenerator.__commands.cmd.SelectEncodingTable import SelectEncodingTable
from ZplGenerator.__commands.cmd.SerializationField import SerializationField
from ZplGenerator.__commands.cmd.SetSensorIntensity import SetSensorIntensity
from ZplGenerator.__commands.cmd.SetModeAndLanguage import SetModeAndLanguage
from ZplGenerator.__commands.cmd.SerializationData import SerializationData
from ZplGenerator.__commands.cmd.SetOffset import SetOffset
from ZplGenerator.__commands.cmd.StartPrint import StartPrint
from ZplGenerator.__commands.cmd.HaltZebraNetAlert import HaltZebraNetAlert
from ZplGenerator.__commands.cmd.SetPrintheadResistance import SetPrintheadResistance
from ZplGenerator.__commands.cmd.SetMediaSensors import SetMediaSensors
from ZplGenerator.__commands.cmd.SetDateAndTime import SetDateAndTime
from ZplGenerator.__commands.cmd.SetZebraNetAlert import SetZebraNetAlert
from ZplGenerator.__commands.cmd.SetZplMode import SetZplMode
from ZplGenerator.__commands.cmd.TearOffAdjustPosition import TearOffAdjustPosition
from ZplGenerator.__commands.cmd.TextBlocks import TextBlocks
from ZplGenerator.__commands.cmd.TransferObject import TransferObject
from ZplGenerator.__commands.cmd.PrintConfigurationLabel import PrintConfigurationLabel
from ZplGenerator.__commands.cmd.PrintDirectoryLabel import PrintDirectoryLabel
from ZplGenerator.__commands.cmd.WriteQuery import WriteQuery
from ZplGenerator.__commands.cmd.StartFormat import StartFormat
from ZplGenerator.__commands.cmd.SuppressBackfeed import SuppressBackfeed
from ZplGenerator.__commands.cmd.RecallFormat import RecallFormat
from ZplGenerator.__commands.cmd.RecallGraphic import RecallGraphic
from ZplGenerator.__commands.cmd.SetDynamicMediaCalibration import SetDynamicMediaCalibration
from ZplGenerator.__commands.cmd.EndFormat import EndFormat
from ZplGenerator.__commands.cmd.PrinterSleep import PrinterSleep

if __name__ == '__main__':
	help(ALL_COMMANDS)
	help(ALPHANUMERIC)
	help(BARCODE_CREATING_COMMANDS)
	help(CARET_CHAR)
	help(CTR_CMD_CHAR)
	help(DELIMITER_CHAR)
	help(DOTS_VALUE_RANGE)
	help(HEX_IND_CHAR)
	help(ORIENTATIONS)
	help(ScalableFontCommand)
	help(ScalableFontCommandByName)
	help(AztecBarcodeParameters)
	help(Code11Barcode)
	help(Interleaved2Of5Barcode)
	help(Code39Barcode)
	help(Code49Barcode)
	help(PlanetCodeBarcode)
	help(PDF417Barcode)
	help(EAN8Barcode)
	help(UPCeBarcode)
	help(Code93Barcode)
	help(CodaBlockBarcode)
	help(Code128Barcode)
	help(UpsMaxiCodeBarcode)
	help(EAN13Barcode)
	help(MicroPDF417Barcode)
	help(Industrial2Of5Barcode)
	help(Standard2Of5Barcode)
	help(AnsiCodaBarBarcode)
	help(LogMarsBarcode)
	help(MsiBarcode)
	help(AztecBarcodeParameters)
	help(PlesseyBarcode)
	help(QrCodeBarcode)
	help(Gs1Barcode)
	help(Upc_EanExtensions)
	help(TLC39Barcode)
	help(UpcABarcode)
	help(DataMatrixBarcode)
	help(BarcodeFieldDefault)
	help(PostalBarcode)
	help(ChangeCaret)
	help(ChangeCaret)
	help(ChangeDelimiter)
	help(ChangeDelimiter)
	help(ChangeAlphanumericDefaultFont)
	help(ChangeInternationalFontEncoding)
	help(ChangeMemoryLetterDesignation)
	help(CutNow)
	help(CacheOn)
	help(RemoveLabel)
	help(ChangeControlCommandCharacter)
	help(ChangeControlCommandCharacter)
	help(CodeValidation)
	help(FontIdentifier)
	help(DownloadBitmapFont)
	help(DownloadEncoding)
	help(DownloadFormat)
	help(DownloadGraphics)
	help(AbortDownloadGraphic)
	help(DownloadScalableFont)
	help(DownloadBoundedTrueTypeFont)
	help(DownloadUnboundedTrueTypeFont)
	help(DownloadObjects)
	help(EraseDownloadGraphics)
	help(FieldBlock)
	help(FiledClock)
	help(FiledData)
	help(FieldHexadecimalIndicator)
	help(FontLinking)
	help(MultipleFieldOriginLocations)
	help(FieldNumber)
	help(FieldOrigin)
	help(FieldParameter)
	help(FieldReversePrint)
	help(FieldSeparator)
	help(FieldTypeset)
	help(FieldVariable)
	help(FieldOrientation)
	help(Comment)
	help(GraphicBox)
	help(GraphicCircle)
	help(GraphicDiagonalLine)
	help(GraphicEllipse)
	help(GraphicField)
	help(GraphicSymbol)
	help(BatteryStatus)
	help(HeadDiagnostic)
	help(HostFormat)
	help(HostGraphic)
	help(ConfigurationLabelReturn)
	help(HostIdentification)
	help(HostRamStatus)
	help(HostQuery)
	help(HostStatusReturn)
	help(HostLinkedFontsList)
	help(ZebraNetAlertConfiguration)
	help(HostVerification)
	help(HostDirectoryList)
	help(UploadGraphics)
	help(DisplayDescriptionInformation)
	help(ObjectDelete)
	help(ImageLoad)
	help(ImageMove)
	help(ImageSave)
	help(CancelAll)
	help(InitializeFlashMemory)
	help(ResetOptionalMemory)
	help(SetMediaSensorCalibration)
	help(EnableCommunicationDiagnostics)
	help(DisableDiagnostics)
	help(SetBatteryCondition)
	help(GraphicSensorCalibration)
	help(EarlyWarningSetting)
	help(StartZBI)
	help(StartZBI)
	help(SetAuxiliaryPort)
	help(SetLabelLength)
	help(SetDotsPerMillimeter)
	help(HeadTestFatal)
	help(HeadTestNonFatal)
	help(PauseAndCancelFormat)
	help(TerminateZebraBasicInterpreter)
	help(PowerOnReset)
	help(SensorSelect)
	help(ChangeBackfeedSequence)
	help(HeadTestInterval)
	help(ConfigurationUpdate)
	help(SetRibbonTension)
	help(CancelCurrentPartiallyInputFormat)
	help(ReprintAfterError)
	help(KillBattery)
	help(SelectDateAndTimeFormat)
	help(DefineLanguage)
	help(DefinePrinterName)
	help(DefinePassword)
	help(KioskValues)
	help(ListFontLinks)
	help(LabelHome)
	help(LabelLength)
	help(LabelReversePrint)
	help(LabelShift)
	help(LabelTop)
	help(SetMaintenanceAlerts)
	help(MapClear)
	help(MediaDarkness)
	help(MediaFeed)
	help(SetMaintenanceInformationMessage)
	help(MaximumLabelLength)
	help(PrintMode)
	help(MediaTracking)
	help(ModeProtection)
	help(MediaType)
	help(SetUnitOfMeasurement)
	help(ModifyHeadColdWarning)
	help(SelectPrimaryNetworkDevice)
	help(NetworkConnect)
	help(ChangeNetworkSettings)
	help(NetworkIdNumber)
	help(SetAllNetworkPrintersTransparent)
	help(ChangeWiredNetworkingSettings)
	help(SetCurrentConnectedPrinterTransparent)
	help(AdvancedTextProperties)
	help(SlewGivenNumberOfDotRows)
	help(SlewToHomePosition)
	help(SlewToHomePosition)
	help(PresentLengthAddition)
	help(PrintingMirrorImageOfLabel)
	help(DecommissioningMode)
	help(PresentNow)
	help(PrintOrientation)
	help(ProgramablePause)
	help(ProgramablePause)
	help(PrintQuantity)
	help(ApplicatorReprint)
	help(PrintRate)
	help(PrintStart)
	help(PrintWidth)
	help(ResetAdvancedCounters)
	help(SetSerialCommunications)
	help(SetDarkness)
	help(SelectEncodingTable)
	help(SerializationField)
	help(SetSensorIntensity)
	help(SetModeAndLanguage)
	help(SerializationData)
	help(SetOffset)
	help(StartPrint)
	help(HaltZebraNetAlert)
	help(SetPrintheadResistance)
	help(SetMediaSensors)
	help(SetDateAndTime)
	help(SetZebraNetAlert)
	help(SetZplMode)
	help(TearOffAdjustPosition)
	help(TextBlocks)
	help(TransferObject)
	help(PrintConfigurationLabel)
	help(PrintDirectoryLabel)
	help(WriteQuery)
	help(StartFormat)
	help(SuppressBackfeed)
	help(RecallFormat)
	help(RecallGraphic)
	help(SetDynamicMediaCalibration)
	help(EndFormat)
	help(PrinterSleep)
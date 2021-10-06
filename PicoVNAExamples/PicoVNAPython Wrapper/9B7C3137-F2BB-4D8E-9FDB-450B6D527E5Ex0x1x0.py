# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.8.8 (default, Apr 13 2021, 15:08:07) [MSC v.1916 32 bit (Intel)]
# From type library 'PicoControl3.dll'
# On Wed Oct  6 15:25:16 2021
'PicoControl3 Library'
makepy_version = '0.5.01'
python_version = 0x30808f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{9B7C3137-F2BB-4D8E-9FDB-450B6D527E5E}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

from win32com.client import DispatchBaseClass
class _PicoVNA_3(DispatchBaseClass):
	CLSID = IID('{B4E14A04-45D2-4E31-AEB8-74C4E204105D}')
	coclass_clsid = IID('{80A5BF42-D3CB-4026-9A88-3BD878374F0A}')

	def AppCal(self, caltype=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809376, LCID, 1, (8, 0), ((8, 1),),caltype
			)

	def AppMemMath(self, Para=defaultNamedNotOptArg, Func=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809370, LCID, 1, (8, 0), ((12, 1), (12, 1)),Para
			, Func)

	def CloseVNA(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809348, LCID, 1, (8, 0), (),)

	def DLLVer(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809344, LCID, 1, (8, 0), (),)

	def DoAMPMCal(self, Loss1=defaultNamedNotOptArg, Loss2=defaultNamedNotOptArg, Ftest=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809386, LCID, 1, (8, 0), ((12, 1), (12, 1), (12, 1)),Loss1
			, Loss2, Ftest)

	def DoAMPMMeas(self, Ptest=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809387, LCID, 1, (8, 0), ((12, 1),),Ptest
			)

	def DoP1dBCal(self, Loss1=defaultNamedNotOptArg, Loss2=defaultNamedNotOptArg, Ftest=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809384, LCID, 1, (8, 0), ((12, 1), (12, 1), (12, 1)),Loss1
			, Loss2, Ftest)

	def DoP1dBMeas(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809385, LCID, 1, (8, 0), (),)

	def FND(self):
		return self._oleobj_.InvokeTypes(1610809345, LCID, 1, (2, 0), (),)

	def FNDSN(self, SN=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610809347, LCID, 1, (2, 0), ((8, 1),),SN
			)

	def FndPt(self, Freq=defaultNamedNotOptArg, Para=defaultNamedNotOptArg, MeasType=defaultNamedNotOptArg, Func=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809369, LCID, 1, (8, 0), ((12, 1), (12, 1), (12, 1), (12, 1)),Freq
			, Para, MeasType, Func)

	def GetData(self, Para=defaultNamedNotOptArg, MeasType=defaultNamedNotOptArg, Pnt=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809367, LCID, 1, (8, 0), ((12, 1), (12, 1), (12, 1)),Para
			, MeasType, Pnt)

	def GetInfo(self, Para=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809365, LCID, 1, (8, 0), ((8, 1),),Para
			)

	def GetMem(self, Para=defaultNamedNotOptArg, MeasType=defaultNamedNotOptArg, Pnt=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809368, LCID, 1, (8, 0), ((12, 1), (12, 1), (12, 1)),Para
			, MeasType, Pnt)

	def InitVar(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809351, LCID, 1, (8, 0), (),)

	def InsDiag(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809349, LCID, 1, (8, 0), (),)

	def LoadCal(self, filename=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809374, LCID, 1, (8, 0), ((12, 1),),filename
			)

	def MeasCal(self, caltype=defaultNamedNotOptArg, Standard=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809375, LCID, 1, (8, 0), ((8, 1), (8, 1)),caltype
			, Standard)

	def Measure(self, Para=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809372, LCID, 1, (8, 0), ((12, 1),),Para
			)

	def PulseTrigOut(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809364, LCID, 1, (8, 0), (),)

	def ReOpenUSB(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809346, LCID, 1, (8, 0), (),)

	def ResetErr(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809350, LCID, 1, (8, 0), (),)

	def SOTMeasure(self, j=defaultNamedNotOptArg, Trg=defaultNamedNotOptArg, Para=defaultNamedNotOptArg, Tout=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809359, LCID, 1, (8, 0), ((12, 1), (8, 1), (8, 1), (12, 1)),j
			, Trg, Para, Tout)

	def SOT_CopySweep(self, Swp=defaultNamedNotOptArg, Trc=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809358, LCID, 1, (8, 0), ((2, 1), (8, 1)),Swp
			, Trc)

	def SOT_SaveData(self, Fl=defaultNamedNotOptArg, Par=defaultNamedNotOptArg, frm=defaultNamedNotOptArg, Md=defaultNamedNotOptArg
			, f=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809360, LCID, 1, (8, 0), ((8, 1), (8, 1), (8, 1), (8, 1), (12, 1)),Fl
			, Par, frm, Md, f)

	def SaveCal(self, filename=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809373, LCID, 1, (8, 0), ((12, 1),),filename
			)

	def SaveKit(self, filename=defaultNamedNotOptArg, port=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809381, LCID, 1, (8, 0), ((12, 1), (2, 1)),filename
			, port)

	def SaveToMem(self, Para=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809371, LCID, 1, (8, 0), ((12, 1),),Para
			)

	def SelectAMPM(self):
		return self._oleobj_.InvokeTypes(1610809378, LCID, 1, (24, 0), (),)

	def SelectCal(self, filename=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809356, LCID, 1, (8, 0), ((8, 1),),filename
			)

	def SelectKit(self, filename=defaultNamedNotOptArg, port=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809352, LCID, 1, (8, 0), ((8, 1), (2, 1)),filename
			, port)

	def SelectMixerFrm(self):
		return self._oleobj_.InvokeTypes(1610809379, LCID, 1, (24, 0), (),)

	def SelectP1dB(self):
		return self._oleobj_.InvokeTypes(1610809377, LCID, 1, (24, 0), (),)

	def SelectSOT(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809357, LCID, 1, (8, 0), (),)

	def SelectSaveMeas(self):
		return self._oleobj_.InvokeTypes(1610809380, LCID, 1, (24, 0), (),)

	def SelectSigGen(self):
		return self._oleobj_.InvokeTypes(1610809353, LCID, 1, (24, 0), (),)

	def SetCWmode(self, f=defaultNamedNotOptArg, i=defaultNamedNotOptArg, U=defaultNamedNotOptArg, T=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610809361, 1, (12, 0), ((12, 1), (12, 1), (12, 1), (12, 1)), 'SetCWmode', None,f
			, i, U, T)

	def SetEnhance(self, Para=defaultNamedNotOptArg, k=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809366, LCID, 1, (8, 0), ((12, 1), (12, 1)),Para
			, k)

	def SetFreqPlan(self, Fstart=defaultNamedNotOptArg, Fstep=defaultNamedNotOptArg, i=defaultNamedNotOptArg, P=defaultNamedNotOptArg
			, ub=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809362, LCID, 1, (8, 0), ((12, 1), (12, 1), (12, 1), (12, 1), (12, 1)),Fstart
			, Fstep, i, P, ub)

	def SetKit(self, name=defaultNamedNotOptArg, Ksex=defaultNamedNotOptArg, Koff=defaultNamedNotOptArg, Koff2=defaultNamedNotOptArg
			, CF0=defaultNamedNotOptArg, CF1=defaultNamedNotOptArg, CF2=defaultNamedNotOptArg, CF3=defaultNamedNotOptArg, ShortL=defaultNamedNotOptArg
			, OffLoss1=defaultNamedNotOptArg, OffLoss2=defaultNamedNotOptArg, port=defaultNamedNotOptArg, MData=defaultNamedNotOptArg, filename=defaultNamedNotOptArg
			, TData=defaultNamedNotOptArg, FileName2=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809355, LCID, 1, (8, 0), ((8, 1), (8, 1), (12, 1), (12, 1), (12, 1), (12, 1), (12, 1), (12, 1), (12, 1), (12, 1), (12, 1), (2, 1), (8, 1), (8, 1), (8, 1), (8, 1)),name
			, Ksex, Koff, Koff2, CF0, CF1
			, CF2, CF3, ShortL, OffLoss1, OffLoss2
			, port, MData, filename, TData, FileName2
			)

	def SetLimits(self, Segment=defaultNamedNotOptArg, Para=defaultNamedNotOptArg, FreqLow=defaultNamedNotOptArg, FreqHigh=defaultNamedNotOptArg
			, min=defaultNamedNotOptArg, max=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809390, LCID, 1, (8, 0), ((2, 1), (8, 1), (12, 1), (12, 1), (12, 1), (12, 1)),Segment
			, Para, FreqLow, FreqHigh, min, max
			)

	def SetRXQ(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809388, LCID, 1, (8, 0), (),)

	def SetRef(self, Para=defaultNamedNotOptArg, k=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809383, LCID, 1, (8, 0), ((12, 1), (12, 1)),Para
			, k)

	def SetRefLoss(self, Para=defaultNamedNotOptArg, k=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809382, LCID, 1, (8, 0), ((12, 1), (12, 1)),Para
			, k)

	def SetSigGen(self, Mode=defaultNamedNotOptArg, P1=defaultNamedNotOptArg, P2=defaultNamedNotOptArg, Prt=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809354, LCID, 1, (8, 0), ((12, 1), (12, 1), (12, 1), (8, 1)),Mode
			, P1, P2, Prt)

	def SetSysZo(self, SysZo=defaultNamedNotOptArg, ExMatch=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809389, LCID, 1, (8, 0), ((2, 1), (12, 1)),SysZo
			, ExMatch)

	def SetTrig(self, Para=defaultNamedNotOptArg, T=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809363, LCID, 1, (8, 0), ((8, 1), (12, 1)),Para
			, T)

	def TestLimits(self, Para=defaultNamedNotOptArg, FreqLow=defaultNamedNotOptArg, FreqHigh=defaultNamedNotOptArg, MeasType=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809392, LCID, 1, (8, 0), ((8, 1), (12, 1), (12, 1), (12, 1)),Para
			, FreqLow, FreqHigh, MeasType)

	def ZConversion(self, ZoOld=defaultNamedNotOptArg, ZoNew=defaultNamedNotOptArg, A11R=defaultNamedNotOptArg, A11I=defaultNamedNotOptArg
			, A21R=defaultNamedNotOptArg, A21I=defaultNamedNotOptArg, A12R=defaultNamedNotOptArg, A12I=defaultNamedNotOptArg, A22R=defaultNamedNotOptArg
			, A22I=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610809391, 1, (8, 0), ((12, 1), (12, 1), (12, 1), (16396, 3), (16396, 3), (16396, 3), (16396, 3), (16389, 3), (16389, 3), (16389, 3)), 'ZConversion', None,ZoOld
			, ZoNew, A11R, A11I, A21R, A21I
			, A12R, A12I, A22R, A22I)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

from win32com.client import CoClassBaseClass
# This CoClass is known by the name 'PicoControl3.PicoVNA_3'
class PicoVNA_3(CoClassBaseClass): # A CoClass
	CLSID = IID('{80A5BF42-D3CB-4026-9A88-3BD878374F0A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PicoVNA_3,
	]
	default_interface = _PicoVNA_3

_PicoVNA_3_vtables_dispatch_ = 1
_PicoVNA_3_vtables_ = [
	(( 'DLLVer' , None , ), 1610809344, (1610809344, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'FND' , None , ), 1610809345, (1610809345, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'ReOpenUSB' , None , ), 1610809346, (1610809346, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'FNDSN' , 'SN' , None , ), 1610809347, (1610809347, (), [ (8, 1, None, None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'CloseVNA' , None , ), 1610809348, (1610809348, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'InsDiag' , None , ), 1610809349, (1610809349, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'ResetErr' , None , ), 1610809350, (1610809350, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'InitVar' , None , ), 1610809351, (1610809351, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'SelectKit' , 'filename' , 'port' , None , ), 1610809352, (1610809352, (), [ 
			 (8, 1, None, None) , (2, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'SelectSigGen' , ), 1610809353, (1610809353, (), [ ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'SetSigGen' , 'Mode' , 'P1' , 'P2' , 'Prt' , 
			 None , ), 1610809354, (1610809354, (), [ (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , 
			 (8, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'SetKit' , 'name' , 'Ksex' , 'Koff' , 'Koff2' , 
			 'CF0' , 'CF1' , 'CF2' , 'CF3' , 'ShortL' , 
			 'OffLoss1' , 'OffLoss2' , 'port' , 'MData' , 'filename' , 
			 'TData' , 'FileName2' , None , ), 1610809355, (1610809355, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , 
			 (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , 
			 (2, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'SelectCal' , 'filename' , None , ), 1610809356, (1610809356, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'SelectSOT' , None , ), 1610809357, (1610809357, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'SOT_CopySweep' , 'Swp' , 'Trc' , None , ), 1610809358, (1610809358, (), [ 
			 (2, 1, None, None) , (8, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'SOTMeasure' , 'j' , 'Trg' , 'Para' , 'Tout' , 
			 None , ), 1610809359, (1610809359, (), [ (12, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , 
			 (12, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'SOT_SaveData' , 'Fl' , 'Par' , 'frm' , 'Md' , 
			 'f' , None , ), 1610809360, (1610809360, (), [ (8, 1, None, None) , (8, 1, None, None) , 
			 (8, 1, None, None) , (8, 1, None, None) , (12, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'SetCWmode' , 'f' , 'i' , 'U' , 'T' , 
			 None , ), 1610809361, (1610809361, (), [ (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , 
			 (12, 1, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'SetFreqPlan' , 'Fstart' , 'Fstep' , 'i' , 'P' , 
			 'ub' , None , ), 1610809362, (1610809362, (), [ (12, 1, None, None) , (12, 1, None, None) , 
			 (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'SetTrig' , 'Para' , 'T' , None , ), 1610809363, (1610809363, (), [ 
			 (8, 1, None, None) , (12, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'PulseTrigOut' , None , ), 1610809364, (1610809364, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'GetInfo' , 'Para' , None , ), 1610809365, (1610809365, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'SetEnhance' , 'Para' , 'k' , None , ), 1610809366, (1610809366, (), [ 
			 (12, 1, None, None) , (12, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'GetData' , 'Para' , 'MeasType' , 'Pnt' , None , 
			 ), 1610809367, (1610809367, (), [ (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'GetMem' , 'Para' , 'MeasType' , 'Pnt' , None , 
			 ), 1610809368, (1610809368, (), [ (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( 'FndPt' , 'Freq' , 'Para' , 'MeasType' , 'Func' , 
			 None , ), 1610809369, (1610809369, (), [ (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , 
			 (12, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'AppMemMath' , 'Para' , 'Func' , None , ), 1610809370, (1610809370, (), [ 
			 (12, 1, None, None) , (12, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( 'SaveToMem' , 'Para' , None , ), 1610809371, (1610809371, (), [ (12, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Measure' , 'Para' , None , ), 1610809372, (1610809372, (), [ (12, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( 'SaveCal' , 'filename' , None , ), 1610809373, (1610809373, (), [ (12, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'LoadCal' , 'filename' , None , ), 1610809374, (1610809374, (), [ (12, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( 'MeasCal' , 'caltype' , 'Standard' , None , ), 1610809375, (1610809375, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'AppCal' , 'caltype' , None , ), 1610809376, (1610809376, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( 'SelectP1dB' , ), 1610809377, (1610809377, (), [ ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'SelectAMPM' , ), 1610809378, (1610809378, (), [ ], 1 , 1 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( 'SelectMixerFrm' , ), 1610809379, (1610809379, (), [ ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'SelectSaveMeas' , ), 1610809380, (1610809380, (), [ ], 1 , 1 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
	(( 'SaveKit' , 'filename' , 'port' , None , ), 1610809381, (1610809381, (), [ 
			 (12, 1, None, None) , (2, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'SetRefLoss' , 'Para' , 'k' , None , ), 1610809382, (1610809382, (), [ 
			 (12, 1, None, None) , (12, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 180 , (3, 0, None, None) , 0 , )),
	(( 'SetRef' , 'Para' , 'k' , None , ), 1610809383, (1610809383, (), [ 
			 (12, 1, None, None) , (12, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'DoP1dBCal' , 'Loss1' , 'Loss2' , 'Ftest' , None , 
			 ), 1610809384, (1610809384, (), [ (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 188 , (3, 0, None, None) , 0 , )),
	(( 'DoP1dBMeas' , None , ), 1610809385, (1610809385, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'DoAMPMCal' , 'Loss1' , 'Loss2' , 'Ftest' , None , 
			 ), 1610809386, (1610809386, (), [ (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 196 , (3, 0, None, None) , 0 , )),
	(( 'DoAMPMMeas' , 'Ptest' , None , ), 1610809387, (1610809387, (), [ (12, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'SetRXQ' , None , ), 1610809388, (1610809388, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 204 , (3, 0, None, None) , 0 , )),
	(( 'SetSysZo' , 'SysZo' , 'ExMatch' , None , ), 1610809389, (1610809389, (), [ 
			 (2, 1, None, None) , (12, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'SetLimits' , 'Segment' , 'Para' , 'FreqLow' , 'FreqHigh' , 
			 'min' , 'max' , None , ), 1610809390, (1610809390, (), [ (2, 1, None, None) , 
			 (8, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 212 , (3, 0, None, None) , 0 , )),
	(( 'ZConversion' , 'ZoOld' , 'ZoNew' , 'A11R' , 'A11I' , 
			 'A21R' , 'A21I' , 'A12R' , 'A12I' , 'A22R' , 
			 'A22I' , None , ), 1610809391, (1610809391, (), [ (12, 1, None, None) , (12, 1, None, None) , 
			 (12, 1, None, None) , (16396, 3, None, None) , (16396, 3, None, None) , (16396, 3, None, None) , (16396, 3, None, None) , 
			 (16389, 3, None, None) , (16389, 3, None, None) , (16389, 3, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'TestLimits' , 'Para' , 'FreqLow' , 'FreqHigh' , 'MeasType' , 
			 None , ), 1610809392, (1610809392, (), [ (8, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , 
			 (12, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 220 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{B4E14A04-45D2-4E31-AEB8-74C4E204105D}' : _PicoVNA_3,
	'{80A5BF42-D3CB-4026-9A88-3BD878374F0A}' : PicoVNA_3,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{B4E14A04-45D2-4E31-AEB8-74C4E204105D}' : '_PicoVNA_3',
}


NamesToIIDMap = {
	'_PicoVNA_3' : '{B4E14A04-45D2-4E31-AEB8-74C4E204105D}',
}



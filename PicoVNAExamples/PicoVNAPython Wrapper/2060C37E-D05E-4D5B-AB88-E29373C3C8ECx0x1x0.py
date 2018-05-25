# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 2.7.14 |Anaconda, Inc.| (default, Nov  8 2017, 13:40:13) [MSC v.1500 32 bit (Intel)]
# From type library 'PicoControl2.dll'
# On Fri May 25 09:48:43 2018
'PicoControl2 Library'
makepy_version = '0.5.01'
python_version = 0x2070ef0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{2060C37E-D05E-4D5B-AB88-E29373C3C8EC}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

from win32com.client import DispatchBaseClass
class _PicoVNA_2(DispatchBaseClass):
	CLSID = IID('{966B8A4B-5130-4990-A784-33EFFF27F468}')
	coclass_clsid = IID('{2856BC1D-2651-4153-A8D6-9AE79DFA6744}')

	def AppCal(self, caltype=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809370, LCID, 1, (8, 0), ((8, 1),),caltype
			)

	def AppMemMath(self, para=defaultNamedNotOptArg, Func=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809364, LCID, 1, (8, 0), ((12, 1), (12, 1)),para
			, Func)

	def CloseVNA(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809347, LCID, 1, (8, 0), (),)

	def DLLVer(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809344, LCID, 1, (8, 0), (),)

	def DoAMPMCal(self, Loss1=defaultNamedNotOptArg, Loss2=defaultNamedNotOptArg, Ftest=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809378, LCID, 1, (8, 0), ((12, 1), (12, 1), (12, 1)),Loss1
			, Loss2, Ftest)

	def DoAMPMMeas(self, Ptest=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809379, LCID, 1, (8, 0), ((12, 1),),Ptest
			)

	def DoP1dBCal(self, Loss1=defaultNamedNotOptArg, Loss2=defaultNamedNotOptArg, Ftest=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809376, LCID, 1, (8, 0), ((12, 1), (12, 1), (12, 1)),Loss1
			, Loss2, Ftest)

	def DoP1dBMeas(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809377, LCID, 1, (8, 0), (),)

	def FND(self):
		return self._oleobj_.InvokeTypes(1610809345, LCID, 1, (2, 0), (),)

	def FNDSN(self, SN=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610809346, LCID, 1, (2, 0), ((8, 1),),SN
			)

	def FndPt(self, Freq=defaultNamedNotOptArg, para=defaultNamedNotOptArg, MeasType=defaultNamedNotOptArg, Func=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809363, LCID, 1, (8, 0), ((12, 1), (12, 1), (12, 1), (12, 1)),Freq
			, para, MeasType, Func)

	def GetData(self, para=defaultNamedNotOptArg, MeasType=defaultNamedNotOptArg, Pnt=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809361, LCID, 1, (8, 0), ((12, 1), (12, 1), (12, 1)),para
			, MeasType, Pnt)

	def GetInfo(self, para=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809359, LCID, 1, (8, 0), ((8, 1),),para
			)

	def GetMem(self, para=defaultNamedNotOptArg, MeasType=defaultNamedNotOptArg, Pnt=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809362, LCID, 1, (8, 0), ((12, 1), (12, 1), (12, 1)),para
			, MeasType, Pnt)

	def InitVar(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809350, LCID, 1, (8, 0), (),)

	def InsDiag(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809348, LCID, 1, (8, 0), (),)

	def LoadCal(self, FileName=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809368, LCID, 1, (8, 0), ((12, 1),),FileName
			)

	def MeasCal(self, caltype=defaultNamedNotOptArg, Standard=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809369, LCID, 1, (8, 0), ((8, 1), (8, 1)),caltype
			, Standard)

	def Measure(self, para=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809366, LCID, 1, (8, 0), ((12, 1),),para
			)

	def ResetErr(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809349, LCID, 1, (8, 0), (),)

	def SaveCal(self, FileName=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809367, LCID, 1, (8, 0), ((12, 1),),FileName
			)

	def SaveKit(self, FileName=defaultNamedNotOptArg, port=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809374, LCID, 1, (8, 0), ((12, 1), (2, 1)),FileName
			, port)

	def SaveToMem(self, para=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809365, LCID, 1, (8, 0), ((12, 1),),para
			)

	def SelectAMPM(self):
		return self._oleobj_.InvokeTypes(1610809372, LCID, 1, (24, 0), (),)

	def SelectCal(self, FileName=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809355, LCID, 1, (8, 0), ((8, 1),),FileName
			)

	def SelectKit(self, FileName=defaultNamedNotOptArg, port=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809351, LCID, 1, (8, 0), ((8, 1), (2, 1)),FileName
			, port)

	def SelectP1dB(self):
		return self._oleobj_.InvokeTypes(1610809371, LCID, 1, (24, 0), (),)

	def SelectSaveMeas(self):
		return self._oleobj_.InvokeTypes(1610809373, LCID, 1, (24, 0), (),)

	def SelectSigGen(self):
		return self._oleobj_.InvokeTypes(1610809352, LCID, 1, (24, 0), (),)

	def SetCWmode(self, f=defaultNamedNotOptArg, i=defaultNamedNotOptArg, U=defaultNamedNotOptArg, T=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610809356, 1, (12, 0), ((12, 1), (12, 1), (12, 1), (12, 1)), u'SetCWmode', None,f
			, i, U, T)

	def SetEnhance(self, para=defaultNamedNotOptArg, k=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809360, LCID, 1, (8, 0), ((12, 1), (12, 1)),para
			, k)

	def SetFreqPlan(self, Fstart=defaultNamedNotOptArg, Fstep=defaultNamedNotOptArg, i=defaultNamedNotOptArg, P=defaultNamedNotOptArg
			, b=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809357, LCID, 1, (8, 0), ((12, 1), (12, 1), (12, 1), (12, 1), (12, 1)),Fstart
			, Fstep, i, P, b)

	def SetKit(self, name=defaultNamedNotOptArg, Ksex=defaultNamedNotOptArg, Koff=defaultNamedNotOptArg, Koff2=defaultNamedNotOptArg
			, CF0=defaultNamedNotOptArg, CF1=defaultNamedNotOptArg, CF2=defaultNamedNotOptArg, CF3=defaultNamedNotOptArg, ShortL=defaultNamedNotOptArg
			, OffLoss1=defaultNamedNotOptArg, OffLoss2=defaultNamedNotOptArg, port=defaultNamedNotOptArg, MData=defaultNamedNotOptArg, FileName=defaultNamedNotOptArg
			, TData=defaultNamedNotOptArg, FileName2=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809354, LCID, 1, (8, 0), ((8, 1), (8, 1), (12, 1), (12, 1), (12, 1), (12, 1), (12, 1), (12, 1), (12, 1), (12, 1), (12, 1), (2, 1), (8, 1), (8, 1), (8, 1), (8, 1)),name
			, Ksex, Koff, Koff2, CF0, CF1
			, CF2, CF3, ShortL, OffLoss1, OffLoss2
			, port, MData, FileName, TData, FileName2
			)

	def SetLimits(self, Segment=defaultNamedNotOptArg, para=defaultNamedNotOptArg, FreqLow=defaultNamedNotOptArg, FreqHigh=defaultNamedNotOptArg
			, min=defaultNamedNotOptArg, max=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809382, LCID, 1, (8, 0), ((2, 1), (8, 1), (12, 1), (12, 1), (12, 1), (12, 1)),Segment
			, para, FreqLow, FreqHigh, min, max
			)

	def SetRXQ(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809380, LCID, 1, (8, 0), (),)

	def SetRef(self, para=defaultNamedNotOptArg, k=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809375, LCID, 1, (8, 0), ((12, 1), (12, 1)),para
			, k)

	def SetSigGen(self, Mode=defaultNamedNotOptArg, P1=defaultNamedNotOptArg, P2=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809353, LCID, 1, (8, 0), ((12, 1), (12, 1), (12, 1)),Mode
			, P1, P2)

	def SetSysZo(self, SysZo=defaultNamedNotOptArg, ExMatch=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809381, LCID, 1, (8, 0), ((2, 1), (12, 1)),SysZo
			, ExMatch)

	def SetTrig(self, para=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809358, LCID, 1, (8, 0), ((8, 1),),para
			)

	def TestLimits(self, para=defaultNamedNotOptArg, FreqLow=defaultNamedNotOptArg, FreqHigh=defaultNamedNotOptArg, MeasType=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809384, LCID, 1, (8, 0), ((8, 1), (12, 1), (12, 1), (12, 1)),para
			, FreqLow, FreqHigh, MeasType)

	def ZConversion(self, ZoOld=defaultNamedNotOptArg, ZoNew=defaultNamedNotOptArg, A11R=defaultNamedNotOptArg, A11I=defaultNamedNotOptArg
			, A21R=defaultNamedNotOptArg, A21I=defaultNamedNotOptArg, A12R=defaultNamedNotOptArg, A12I=defaultNamedNotOptArg, A22R=defaultNamedNotOptArg
			, A22I=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610809383, 1, (8, 0), ((12, 1), (12, 1), (12, 1), (16396, 3), (16396, 3), (16396, 3), (16396, 3), (16389, 3), (16389, 3), (16389, 3)), u'ZConversion', None,ZoOld
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
# This CoClass is known by the name 'PicoControl2.PicoVNA_2'
class PicoVNA_2(CoClassBaseClass): # A CoClass
	CLSID = IID('{2856BC1D-2651-4153-A8D6-9AE79DFA6744}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PicoVNA_2,
	]
	default_interface = _PicoVNA_2

_PicoVNA_2_vtables_dispatch_ = 1
_PicoVNA_2_vtables_ = [
	(( u'DLLVer' , None , ), 1610809344, (1610809344, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'FND' , None , ), 1610809345, (1610809345, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'FNDSN' , u'SN' , None , ), 1610809346, (1610809346, (), [ (8, 1, None, None) , 
			(16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'CloseVNA' , None , ), 1610809347, (1610809347, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'InsDiag' , None , ), 1610809348, (1610809348, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'ResetErr' , None , ), 1610809349, (1610809349, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'InitVar' , None , ), 1610809350, (1610809350, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'SelectKit' , u'FileName' , u'port' , None , ), 1610809351, (1610809351, (), [ 
			(8, 1, None, None) , (2, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'SelectSigGen' , ), 1610809352, (1610809352, (), [ ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'SetSigGen' , u'Mode' , u'P1' , u'P2' , None , 
			), 1610809353, (1610809353, (), [ (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'SetKit' , u'name' , u'Ksex' , u'Koff' , u'Koff2' , 
			u'CF0' , u'CF1' , u'CF2' , u'CF3' , u'ShortL' , 
			u'OffLoss1' , u'OffLoss2' , u'port' , u'MData' , u'FileName' , 
			u'TData' , u'FileName2' , None , ), 1610809354, (1610809354, (), [ (8, 1, None, None) , 
			(8, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , 
			(12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , 
			(2, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'SelectCal' , u'FileName' , None , ), 1610809355, (1610809355, (), [ (8, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'SetCWmode' , u'f' , u'i' , u'U' , u'T' , 
			None , ), 1610809356, (1610809356, (), [ (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , 
			(12, 1, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'SetFreqPlan' , u'Fstart' , u'Fstep' , u'i' , u'P' , 
			u'b' , None , ), 1610809357, (1610809357, (), [ (12, 1, None, None) , (12, 1, None, None) , 
			(12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'SetTrig' , u'para' , None , ), 1610809358, (1610809358, (), [ (8, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'GetInfo' , u'para' , None , ), 1610809359, (1610809359, (), [ (8, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'SetEnhance' , u'para' , u'k' , None , ), 1610809360, (1610809360, (), [ 
			(12, 1, None, None) , (12, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'GetData' , u'para' , u'MeasType' , u'Pnt' , None , 
			), 1610809361, (1610809361, (), [ (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'GetMem' , u'para' , u'MeasType' , u'Pnt' , None , 
			), 1610809362, (1610809362, (), [ (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'FndPt' , u'Freq' , u'para' , u'MeasType' , u'Func' , 
			None , ), 1610809363, (1610809363, (), [ (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , 
			(12, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'AppMemMath' , u'para' , u'Func' , None , ), 1610809364, (1610809364, (), [ 
			(12, 1, None, None) , (12, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'SaveToMem' , u'para' , None , ), 1610809365, (1610809365, (), [ (12, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'Measure' , u'para' , None , ), 1610809366, (1610809366, (), [ (12, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'SaveCal' , u'FileName' , None , ), 1610809367, (1610809367, (), [ (12, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'LoadCal' , u'FileName' , None , ), 1610809368, (1610809368, (), [ (12, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( u'MeasCal' , u'caltype' , u'Standard' , None , ), 1610809369, (1610809369, (), [ 
			(8, 1, None, None) , (8, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'AppCal' , u'caltype' , None , ), 1610809370, (1610809370, (), [ (8, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( u'SelectP1dB' , ), 1610809371, (1610809371, (), [ ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'SelectAMPM' , ), 1610809372, (1610809372, (), [ ], 1 , 1 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( u'SelectSaveMeas' , ), 1610809373, (1610809373, (), [ ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'SaveKit' , u'FileName' , u'port' , None , ), 1610809374, (1610809374, (), [ 
			(12, 1, None, None) , (2, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( u'SetRef' , u'para' , u'k' , None , ), 1610809375, (1610809375, (), [ 
			(12, 1, None, None) , (12, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'DoP1dBCal' , u'Loss1' , u'Loss2' , u'Ftest' , None , 
			), 1610809376, (1610809376, (), [ (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( u'DoP1dBMeas' , None , ), 1610809377, (1610809377, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'DoAMPMCal' , u'Loss1' , u'Loss2' , u'Ftest' , None , 
			), 1610809378, (1610809378, (), [ (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( u'DoAMPMMeas' , u'Ptest' , None , ), 1610809379, (1610809379, (), [ (12, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'SetRXQ' , None , ), 1610809380, (1610809380, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
	(( u'SetSysZo' , u'SysZo' , u'ExMatch' , None , ), 1610809381, (1610809381, (), [ 
			(2, 1, None, None) , (12, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'SetLimits' , u'Segment' , u'para' , u'FreqLow' , u'FreqHigh' , 
			u'min' , u'max' , None , ), 1610809382, (1610809382, (), [ (2, 1, None, None) , 
			(8, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 180 , (3, 0, None, None) , 0 , )),
	(( u'ZConversion' , u'ZoOld' , u'ZoNew' , u'A11R' , u'A11I' , 
			u'A21R' , u'A21I' , u'A12R' , u'A12I' , u'A22R' , 
			u'A22I' , None , ), 1610809383, (1610809383, (), [ (12, 1, None, None) , (12, 1, None, None) , 
			(12, 1, None, None) , (16396, 3, None, None) , (16396, 3, None, None) , (16396, 3, None, None) , (16396, 3, None, None) , 
			(16389, 3, None, None) , (16389, 3, None, None) , (16389, 3, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( u'TestLimits' , u'para' , u'FreqLow' , u'FreqHigh' , u'MeasType' , 
			None , ), 1610809384, (1610809384, (), [ (8, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , 
			(12, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 188 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{966B8A4B-5130-4990-A784-33EFFF27F468}' : _PicoVNA_2,
	'{2856BC1D-2651-4153-A8D6-9AE79DFA6744}' : PicoVNA_2,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{966B8A4B-5130-4990-A784-33EFFF27F468}' : '_PicoVNA_2',
}


NamesToIIDMap = {
	'_PicoVNA_2' : '{966B8A4B-5130-4990-A784-33EFFF27F468}',
}



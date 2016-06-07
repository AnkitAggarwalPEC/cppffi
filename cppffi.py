import cffi,cppyy

class FFI(cffi.FFI):

	def __init__(self):
		"""init function of the cppffi
		"""
		super(cffi.FFI, self).__init__()
		self._gblInterpreter = cppyy.gbl.gInterpreter
		self._cdefsources = []
		self._libraries = []

	def cdef(self,cppsource,override=False,packed=False):
		
		if not isinstance(cppsource,str):
			if not isinstance(cppsource,basestring):
				raise TypeError("cdef() arguments must be a string")
			cppsource = cppsource.encode('ascii')
		
		val = self._gblInterpreter.Declare(cppsource)
		if val == False:
			raise TypeError("Error in the Compilation Process")
		
	def sizeof( self , cdecl = ""):

		if isinstance(cdecl, basestring):
			s = "sizeof("
			s += cdecl
			s += ");"
			val = self._gblInterpreter.ProcessLine(s)
			if val == 0:
				raise TypeError("Error in the Compilation Process")
			else:
				print val
		else:
			raise TypeError("cdef() arguments must be a string")

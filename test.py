import sys

sys.path.append(".")

import cppffi

def test_cppffi_sizeof():

	assert cppffi.sizeof("float") == 4
	print "121"
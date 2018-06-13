#!/usr/bin/env python3
#main.py
# created by: Kurt L. Manion
# on: Mon., 11 June 2018
# Transposition Cypher
#

# DESIDERATUM #
# Input may be:
#   o a message to be encrypted with the current cypher settings
#   o a keyword to set the value of the cypher's settings
#   o a keyword to print out the cypher's settings
#
# Keywords:
# with values:
#   o xdim (alias: rows)
#       - may be set to `auto' (default),
#       - `square' (alias: sq),
#       - or an integer
#   o ydim (alias: cols, collums)
#       - `auto', `square', or integer
#   o dir (alias: direction, rot, rotation)
#       the dir may be set to:
#       - clockwise, cw
#       - counter-clockwise, ccw
#       - twice, tw
# without values:
#   o settings (alias: set, cur, current, curset)
#	o quit (alias: exit)
#

import math

# keyword definitions are lists with their aliases
KW_XDIM =	[ "xdim", "rows" ]
KW_YDIM =	[ "ydim", "cols", "columns" ]
KW_ROT =	[ "rot", "rotation", "dir", "direction" ]
KW_CURSET =	[ "curset", "cur", "current", "settings", "set" ]
KW_HELP =	[ "help", "usage" ]
KW_QUIT =	[ "quit", "exit" ]
KW_LST =	[ KW_XDIM, KW_YDIM, KW_ROT, KW_CURSET, KW_HELP, KW_QUIT ]

KW_XDIM_DESC = "X-dimension of the matrix the message is mapped to before" \
				+"being rotated."
KW_YDIM_DESC = "Y-dimension of the matrix the message is mapped to before" \
				+"being rotated."
KW_ROT_DESC = "Direction to rotate the matrix.\nValues:\n" \
		+"\tclockwise (alias: cw),\n" \
		+"\tcounter-clockwise (alias: ccw),\n" \
		+"\ttwice (alias: tw)."
KW_CURSET_DESC = "Display the current settings."
KW_HELP_DESC = "Dispay usage information."
KW_QUIT_DESC = "Exit the application."
KW_DESC = [ KW_XDIM_DESC, KW_YDIM_DESC, KW_ROT_DESC, KW_CURSET_DESC,
			KW_HELP_DESC, KW_QUIT_DESC ]

DIM_AUTO =	[ "auto" ]
DIM_SQ =	[ "sq", "square" ]
KW_DIM_VAL = [ DIM_AUTO, DIM_SQ ]

ROT_CW =	[ "cw", "clockwise" ]
ROT_CCW =	[ "ccw", "counter-clockwise" ]
ROT_TW =	[ "tw", "twice" ]
KW_ROT_VAL = [ ROT_CW, ROT_CCW, ROT_TW ]

# returned by match_keyword if given an invalid keyword
INV_KW = []

# will be made mutable later
PAD_CHAR = 'X'

# settings variables
xdim = DIM_AUTO
ydim = DIM_AUTO
rot = ROT_CW

ver_major = 1
ver_minor = 0
ver_patch = 1
version = str(ver_major)+"."+str(ver_minor)+"."+str(ver_patch)


def match_keyword(kw):
	if kw in KW_LST: # already been matched
		return kw

	if "=" in kw:
		kw = kw[:kw.index("=")]
	kw = kw.strip()

	for i in range(len(KW_LST)):
		for j in range(len(KW_LST[i])):
			if KW_LST[i][j] == kw:
				return KW_LST[i]
	return INV_KW

def is_valid_keyword(kw):
	if kw == INV_KW:
		return False

	return match_keyword(kw) in KW_LST

def is_valid_dim(val):
	if isinstance(val, int) and val > 0:
		return True

	if isinstance(val, str) and val.isdigit():
		return True

	for lst in KW_DIM_VAL:
		if val == lst:
			return True
		for alias in lst:
			if val == alias:
				return True

	return False

# takes raw unsanitized input as argument
def sanitize_dim(s):
	assert is_valid_dim(s)

	if s.isdigit():
		return int(s)

	for lst in KW_DIM_VAL:
		for alias in lst:
			if s == alias:
				return lst

	# this will never happen
	return ""
	
def dim_to_str(dim):
	assert is_valid_dim(dim)

	if dim == DIM_AUTO:
		return "auto"
	elif dim == DIM_SQ:
		return "square"
	else:
		return str(dim)

def banner():
	print("transposition-cypher -- v"+version)
	print("Type `help' for usage information")

def usage(kw=None):
	if kw is None or kw == "":
		print("Input may be either:\n"
				+"\t(1) a message to be encrypted with the currect settings"
				+"\n"
				+"\t(2) a keyword to change or print the setting")
		print("To differentiate keywords from messages starting with the"
				+"keyword, the keyword must be alone, or, if it has a "
				+"corresponding value, be immediately followed by an "
				+"equal sign.")
		print("Type `help' followed by a keyword for aliases, "
				+"and its description")
		for i in range(len(KW_LST)):
			print('{}\t{}'.format(KW_LST[i][0], KW_DESC[i]))
	else:
		kw = match_keyword(kw)
		if is_valid_keyword(kw):
			print(kw[0], end='')

			sz = len(kw)
			if sz > 1:
				print(" (alias: ", end='')
				for i in range(1, sz-1):
					print(kw[i],", ", sep='', end='')
				print(kw[sz-1],")", sep='')

			print(KW_DESC[KW_LST.index(kw)])
		else:
			print("invalid keyword")

def curset():
	print("xdim:",dim_to_str(xdim), sep='\t\t')
	print("ydim:",dim_to_str(ydim), sep='\t\t')
	print("rotation:",rot[1], sep='\t')

def encrypt(s):
	sz = len(s)
	global xdim
	global ydim
	global rot
	if xdim == DIM_SQ or ydim == DIM_SQ:
		x = 1
		y = x
		while x * y < sz:
			x += 1
			y = x
	elif xdim == DIM_AUTO and ydim == DIM_AUTO:
		#find rectangle whose sides are closest to each other in length,
		#and can contain the message--
		#in other words, minimize the difference of the message length
		#and the product of the sides
		x = 1
		y = x
		while x * y < sz:
			x += 1
			y = x

		#take off blank trailing lines
		while sz - x*y >= x:
			y -= 1

		#shrink width
		while sz - x*y >= y:
			x -= 1
	elif x == DIM_AUTO or y == DIM_AUTO:
		#only one of the dimensions are to be automatically set
		if x == DIM_AUTO:
			x = math.ceil(sz / y)
		else:
			y = math.ceil(sz / x)

	pad_sz = x*y - sz

	matrix = []
	for i in range(0, sz, x):
		lst = []
		if sz - i < x:
			lst = list(s[i:])
			for i in range(pad_sz):
				lst.append(PAD_CHAR)
		else:
			lst = list(s[i:i+x])
		matrix.append(lst[:])

	enc = []
	if rot == ROT_CW:
		for i in range(x):
			lst = []
			for j in reversed(range(y)):
				lst.append(matrix[j][i])
			enc.append(lst[:])

	elif rot == ROT_CCW:
		for i in reversed(range(x)):
			lst = []
			for j in range(y):
				lst.append(matrix[j][i])
			enc.append(lst[:])

	elif rot == ROT_TW:
		for i in reversed(range(y)):
			enc.append(matrix[i].reverse())

	#convert encoded matrix to a string
	return ''.join(''.join(lst) for lst in enc)

def main():
	running = True
	global xdim
	global ydim
	global rot

	banner()

	while running:
		s = input()

		if s == "":
			continue

		kw = s.split()[0]
		if "=" in kw:
			kw = kw.split("=")
			val = kw[1].strip()
			kw = kw[0].strip()
		else:
			val = ""
		kw = match_keyword(kw)

		if is_valid_keyword(kw):
			if kw == KW_XDIM:
				if is_valid_dim(val):
					xdim = sanitize_dim(val)
				else:
					print("xdim set to invalid value")

			elif kw == KW_YDIM:
				if is_valid_dim(val):
					ydim = sanitize_dim(val)
				else:
					print("ydim set to invalid value")

			elif kw == KW_ROT:
				if val == "":
					print("rotation keyword requires a value")
					usage(kw)
				else:
					saved = rot
					rot = ""
					for vrot in KW_ROT_VAL:
						for alias in vrot:
							if val == alias:
								rot = vrot
					if rot == "":
						rot = saved
						print("invalid value passed to rotation")
						usage(kw)

			elif kw == KW_CURSET:
				curset()

			elif kw == KW_HELP:
				s = s.split()
				if len(s) >= 2:
					usage(s[1])
				else:
					usage()

			elif kw == KW_QUIT:
				running = False

		else:
			print(encrypt(s))

	return 1

main()

# vim: set ts=4 sw=4 noexpandtab tw=79:

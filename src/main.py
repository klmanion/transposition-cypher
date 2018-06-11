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

# keyword definitions are lists with their aliases
KW_XDIM = [ "xdim", "rows" ]
KW_YDIM = [ "ydim", "cols", "columns" ]
KW_ROT = [ "rot", "rotation", "dir", "direction" ]
KW_CURSET = [ "curset", "cur", "current", "settings", "set" ]
KW_HELP = [ "help", "usage" ]
KW_QUIT = [ "quit", "exit" ]
KW_LST = [ KW_XDIM, KW_YDIM, KW_ROT, KW_CURSET, KW_HELP, KW_QUIT ]

KW_XDIM_DESC = "X-dimension of the matrix the message is mapped to before" \
				+"being rotated."
KW_YDIM_DESC = "Y-dimension of the matrix the message is mapped to before" \
				+"being rotated."
KW_ROT_DESC = "Direction to rotate the matrix."
KW_CURSET_DESC = "Display the current settings."
KW_HELP_DESC = "Dispay usage information."
KW_QUIT_DESC = "Exit the application."
KW_DESC = [ KW_XDIM_DESC, KW_YDIM_DESC, KW_ROT_DESC, KW_CURSET_DESC,
			KW_HELP_DESC, KW_QUIT_DESC ]

DIM_AUTO = [ "auto" ]
DIM_SQ = [ "sq", "square" ]
KW_DIM_VAL = [ DIM_AUTO, DIM_SQ ]

ROT_CW = [ "cw", "clockwise" ]
ROT_CCW = [ "ccw", "counter-clockwise" ]
ROT_TW = [ "tw", "twice" ]
KW_ROT_VAL = [ ROT_CW, ROT_CCW, ROT_TW ]

# returned by match_keyword if given an invalid keyword
INV_KW = []

# settings variables
xdim = DIM_AUTO
ydim = DIM_AUTO
rot = ROT_CW

ver_major = 1
ver_minor = 0
ver_patch = 1
version = str(ver_major)+"."+str(ver_minor)+"."+str(ver_patch)

def encrypt(s):
	print(s)

def match_keyword(kw):
	if "=" in kw:
		kw = kw[:kw.index("=")]
	kw = kw.strip()

	for i in range(len(KW_LST)):
		for j in range(len(KW_LST[i])):
			if KW_LST[i][j] == kw:
				return KW_LST[i]
	return INV_KW

def is_valid_dim(val):
	if val.isdigit():
		return True

	for lst in KW_DIM_VAL:
		for alias in lst:
			if val == alias:
				return True

	return False

def banner():
	print("transposition-cypher -- v"+version)
	print("Type `help' for usage information")

def usage(kw=None):
	if kw is None or kw == "":
		print("Input may be either:\n" \
				+"\t(1) a message to be encrypted with the currect settings"
				+"\n"
				+"\t(2) a keyword to change or print the setting")
		print("To differentiate keywords from messages starting with the" \
				+"keyword, the keyword must be alone, or, if it has a " \
				+"corresponding value, be immediately followed by an " \
				+"equal sign.")
		print("Type `help' followed by a keyword for aliases, " \
				+"and its description")
		for i in range(len(KW_LST)):
			print('{}\t{}'.format(KW_LST[i][0], KW_DESC[i]))
	else:
		kw = match_keyword(kw)
		if kw == INV_KW:
			print("invalid keyword")
		else:
			print(kw[0], end='')

			if len(kw) > 1:
				print(" (alias: ", end='')
				for i in range(1, len(kw)):
					print(kw[i],", ", sep='', end='')
				print(")")

			dex = KW_LST.index(kw)
			print(KW_DESC[dex])

def curset():
	if xdim == DIM_AUTO:
		print("xdim:\t\tauto")
	else:
		print("xdim:",str(xdim), sep='\t\t')

	if ydim == DIM_AUTO:
		print("ydim:\t\tauto")
	else:
		print("ydim:",str(ydim), sep='\t\t')

	print("rotation:",rot[1], sep='\t')

def main():
	running = True

	banner()

	while running:
		s = input()

		if s == "":
			continue

		kw = s.split()[0]
		if "=" in kw:
			kw = kw.split("=")
			val = kw[1]
			kw = kw[0]
		else:
			val = ""
		kw = match_keyword(kw)

		if kw != INV_KW:
			if kw == KW_XDIM:
				if is_valid_dim(val):
					if val.isdigit():
						val = int(val)
					xdim = val
				else:
					print("invalid value passed to xdim")
			elif kw == KW_YDIM:
				if is_valid_dim(val):
					if val.isdigit():
						val = int(val)
					ydim = val
				else:
					print("invalid value passed to ydim")
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
			encrypt(s)

main()

# vim: set ts=4 sw=4 noexpandtab tw=79:

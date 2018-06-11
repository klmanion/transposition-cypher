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
#

# keyword definitions are lists with their aliases
KW_XDIM = [ "xdim", "rows" ]
KW_YDIM = [ "ydim", "cols", "columns" ]
KW_ROT = [ "rot", "rotation", "dir", "direction" ]
KW_CURSET = [ "settings", "set", "cur", "current", "curset" ]

DIM_AUTO = [ "auto" ]
DIM_SQ = [ "sq", "square" ]
KW_DIM_VAL = [ DIM_AUTO, DIM_SQ ]

ROT_CW = [ "cw", "clockwise" ]
ROT_CCW = [ "ccw", "counter-clockwise" ]
ROT_TW = [ "tw", "twice" ]
KW_ROT_VAL = [ ROT_CW, ROT_CCW, ROT_TW ]

# settings variables
xdim = DIM_AUTO
ydim = DIM_AUTO
rot = ROT_CW

def main():
    print(rot)

    return 1

main()

# vim: set ts=4 sw=4 noexpandtab tw=79:

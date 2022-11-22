import argparse
from soubor import *

parser = argparse.ArgumentParser()
#parser.add_argument("square", help="display a square of a given number", type=int)
parser.add_argument("--verbosity", help="increase output verbosity")
#parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("filename", help="jmeno souboru", type=str)

args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")
#print(args.square*args.square)

analyzujSoubor(args.filename)
#!/usr/lib/python3
# -*- coding: utf-8 -*-

import sys
import os

def buildHomerowTex(filename, homerow, layout):
  file = open(filename, "r")
  text = file.read()
  output = ""
  for char in text:
    if char == " ": 
      output += char
    else:
      if char in homerow:
        color = "green"
      else:
        color = "red"
      output += "\\textcolor{" + color + "}{" + char + "}"

  newfile = open(filename + "_" + layout + ".tex", 'w+')
  newfile.write(output)

#main
if __name__ == "__main__":
  if len(sys.argv) > 1:
    filename = sys.argv[1]

    neo = "uiaeosnrtdyUIAEOSNRTDY\/{}():456"
    qwertz = "asdfghjklöäASDFGHJKLÖÄ"

    buildHomerowTex(filename, neo, "neo")
    buildHomerowTex(filename, qwertz, "qwertz")

  else:
    print ("missing filename...")

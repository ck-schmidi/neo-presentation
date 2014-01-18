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

  newfile = open(filename + "_homerow_" + layout + ".tex", 'w+')
  newfile.write(output)

def get_hand(char, left):
  if char in left:
    return 0
  else:
    return 1

def buildHandChangeTex(filename, left, layout):
  file = open(filename, "r")
  text = file.read()
  output = ""
  #0 for left, 1 for right
  lasthand = -1
  for char in text:
    if char == " ":
      output += char
    else:
      hand = get_hand(char, left)
      if (lasthand == -1) or (lasthand != hand):
        color = "green"
      else:
        color = "red"
      lasthand = hand
      output += "\\textcolor{" + color + "}{" + char + "}"
    
  newfile = open(filename + "_handchange_" + layout + ".tex", 'w+')
  newfile.write(output)

#main
if __name__ == "__main__":
  if len(sys.argv) > 1:
    filename = sys.argv[1]

    #changing of hand
    neo_left = "xvlcwuiaeoüöäp"
    neo_left += str.upper(neo_left)

    qwertz_left = "qwertasdfgyxcvb"
    qwertz_left += str.upper(qwertz_left)

    buildHandChangeTex(filename, neo_left, "neo")
    buildHandChangeTex(filename, qwertz_left, "qwertz")

    # homerow
    neo_homerow = "uiaeosnrtdyUIAEOSNRTDY\/{}():456"
    qwertz_homerow = "asdfghjklöäASDFGHJKLÖÄ"

    buildHomerowTex(filename, neo_homerow, "neo")
    buildHomerowTex(filename, qwertz_homerow, "qwertz")

  else:
    print ("missing filename...")

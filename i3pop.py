#! /usr/bin/env python

import i3ipc, subprocess, argparse

# Initialises the argument parser
parser = argparse.ArgumentParser(description='Pops out a tiled window into a floating window in the same place')

# Adds the --sticky option
sticky_parser = parser.add_mutually_exclusive_group(required=False)
sticky_parser.add_argument('--sticky', dest='stick', action='store_true')
sticky_parser.set_defaults(stick=False)
args = parser.parse_args()
sticky = bool(args.stick)

i3 = i3ipc.Connection()

focused = i3.get_tree().find_focused()
windowWidth, windowHeight = str(focused.rect.width), str(focused.rect.height)
#print(windowWidth + ' ' + windowHeight)
windowX, windowY = str(focused.rect.x), str(focused.rect.y)
#print(windowX + ' ' + windowY)

float_window = subprocess.run(['i3-msg', 'floating', 'enable'])

move_window = subprocess.run(['i3-msg', 'move', 'absolute', 'position', windowX, windowY])
resize_window = subprocess.run(['i3-msg', 'resize', 'set', windowWidth, windowHeight])

if sticky == True: stick_window = subprocess.run(['i3-msg', 'sticky', 'toggle'])
else:   pass

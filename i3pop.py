#! /usr/bin/env python

import i3ipc, subprocess, argparse

parser = argparse.ArgumentParser(description='Pops out a tiled window into a floating window in the same place')

sticky_parser = parser.add_mutually_exclusive_group(required=False)
sticky_parser.add_argument('--sticky', dest='stick', action='store_true')
sticky_parser.set_defaults(stick=False)

args = parser.parse_args()

i3 = i3ipc.Connection()

focused = i3.get_tree().find_focused()
windowWidth, windowHeight = str(focused.rect.width), str(focused.rect.height)
print(windowWidth + ' ' + windowHeight)
windowX, windowY = str(focused.rect.x), str(focused.rect.y)
print(windowX + ' ' + windowY)

Float = subprocess.run(['i3-msg', 'floating', 'enable'])
Move = subprocess.run(['i3-msg', 'move', 'absolute', 'position', windowX, windowY])
Resize = subprocess.run(['i3-msg', 'resize', 'set', windowWidth, windowHeight])

sticky = bool(args.stick)
if sticky == True: Stick = subprocess.run(['i3-msg', 'sticky', 'toggle'])
else:   pass

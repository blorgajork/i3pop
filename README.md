# i3pop
A small python script to "pop" out a tiled window by turning it into a floating window with the same dimensions and position.

[![i3pop Demo](https://github.com/blorgajork/i3pop/blob/master/i3pop_demo.gif)](https://github.com/blorgajork/i3pop)

To use this add this line in the i3 config:
### binds i3pop to mod & scrollwheeldown
>bindsym --whole-window $mod+button5 exec /home/george/Python/i3Tools/i3pop/i3pop.py
### does the same but toggles sticky windows
>bindsym --whole-window $mod+Shift+button5 exec /home/george/Python/i3Tools/i3pop/i3pop.py --stick

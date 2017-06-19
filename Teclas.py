#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import Tkinter as Tk
#testes
def handleKeypress (evento ) : 
	pressedKey = event.char
	print (pressedKey)


mainHandle = tk.Tk () 
mainHandle.bind_all (' ' , handleKeypress ) 

mainHandle.withdraw () 
mainHandle.mainloop () 

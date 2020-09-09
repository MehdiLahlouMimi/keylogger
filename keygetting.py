#importement
import pynput

#data
keys = ""
 
#functions
	#callback
def on_press(key) : 
	"""
	A simple function called on pressing a key
	"""
	global keys        #globalise the keys variable

	keys += str(key)   #adding the key to the variable
	


	#important
def listen() : 
	"""
	A simple function to wrap pynput listener and use it in a way that suits our code
	"""

	with pynput.keyboard.Listener(on_press = on_press, on_release = None) as Listener : 
		Listener.join()

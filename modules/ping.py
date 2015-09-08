'''
   author: Ashutosh Das
   email: mail@ashutoshdas.com
   
   This module checks internet connection.
   ping google to test net connectivity.
'''

import subprocess
def ping():
	cmd=["ping","-c1","google.com"]
	try:
		output = subprocess.check_output(cmd)
	except subprocess.CalledProcessError,e:
		return(True)
	else:
		return(False)

if __name__ == '__main__':
	ping()



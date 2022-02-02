

import sys
from os.path import exists
import os


def main():

	if len(sys.argv) != 2:
	    print()
	    print('Usage: `python mbox-splitter.py filename.mbox size`')
	    print('         where `size` is a positive integer in Mb')
	    print()
	    print('Example: `python mbox-splitter.py inbox_test.mbox 50`')
	    print('         where inbox_test.mbox size is about 125 Mb')
	    print()
	    print('Example Result:')
	    print('Created file `example_out.html`') 
	    print('Done')
	    exit()


	filename = sys.argv[1]
	if not exists(filename):
	    print('File `{}` does not exist.'.format(filename))
	    exit()




	# if mailbox.mbox(filename).__len__() == 0: # This is too long for a 32gig file, need to find a faster way to test if there is message in the file.
	if os.stat(filename).st_size == 0:
	    print('Data in `{}` not found.'.format(filename))
	    exit()


	output = filename.rsplit(".", 1)[0] + "out." + filename.rsplit(".", 1)[1]
	# if exists(output):
	#     print('The file `{}` has already been splitted. Delete chunks to continue.'.format(filename))
	#     exit()



	INCREASER = ('<')
	DECREASER = ('</')
	NEUTRAL = ("<img", "<input", "<br")




	with open(filename, 'r', encoding='iso-8859-1') as original_file:

		read_string = original_file.read()
		replaced_string = read_string.replace(">", ">\n")
		replaced_string2 = replaced_string.replace("<", "\n<")
		replaced_string3 = replaced_string2.replace("\n\n", "\n")
	

	with open(output, "w", encoding='iso-8859-1') as new_file:
		level = 0
		going_up = True
		for line in replaced_string3.split("\n"):
			print(line)
			if line.startswith(DECREASER):
				if going_up == True:
					going_up = False
				elif going_up == False:
					level -= 1
				elif going_up == None:
					going_up == False
					level -= 1

			elif line.startswith(NEUTRAL):
				if going_up == True:
					going_up = None
					level += 1
				elif going_up == False:
					going_up = None
					# level -= 1


			elif line.startswith(INCREASER):
				if going_up == True:
					level += 1
					going_up = True
				elif going_up == False:
					going_up = True
				elif going_up == None:
					going_up = True


			else: # This is also neutral
				if going_up == True:
					level += 1
					going_up = None
				elif going_up == False:
					# level -= 1
					going_up = None


			new_file.write("\t"*level + line + "\n")





	print('Created file `{}`.'.format(output, ))
	print('\nDone')



if __name__ == '__main__':
	main()

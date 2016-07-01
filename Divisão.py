splitLen = 20         # 20 lines per file
outputBase = 'output' # output.1.txt, output.2.txt, etc.

# This is shorthand and not friendly with memory
# on very large files (Sean Cavanagh), but it works.
at = 1 
with open('input.txt', 'rb') as input:
            buf = input.read(1024)
            while (buf):
		output = open(outputBase + str(at) + '.txt', 'wb')
    		output.write(buf)
    		output.close()
                buf = input.read(1024)
		at += 1

















#at = 1
#for lines in range(0, len(input), splitLen):
    # First, get the list slice
    #outputData = input[lines:lines+splitLen]

    # Now open the output file, join the new slice with newlines
    # and write it out. Then close the file.
    #output = open(outputBase + str(at) + '.txt', 'w')
    #output.write('\n'.join(outputData))
    #output.close()

    # Increment the counter
    #at += 1


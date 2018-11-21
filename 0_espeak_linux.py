from subprocess import call

cmd_beg= 'espeak '

# To play back the stored .wav file and to dump the std errors to /dev/null
cmd_end= ' | aplay /home/pi/Desktop/Text.wav  2>/dev/null'

# To store the voice file
cmd_out= '--stdout > /home/pi/Desktop/Text.wav ' 

text = input("Enter the Text: ")
print(text)
text = text.replace(' ', '_')

call([cmd_beg+cmd_out+text+cmd_end], shell=True)


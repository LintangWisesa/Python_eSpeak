import subprocess

path = 'C:\Program Files (x86)\eSpeak\command_line\espeak.exe'
text = str(input("Enter a text: "))
print(text)

subprocess.call([path, text], shell=True)
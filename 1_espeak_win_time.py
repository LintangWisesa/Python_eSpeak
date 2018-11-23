import subprocess
import datetime

now = datetime.datetime.now()
tahun = now.year
bulan = now.strftime("%B")
tanggal = now.strftime("%d")
hari = now.strftime("%A")

path = 'C:\Program Files (x86)\eSpeak\command_line\espeak.exe'
text = str('Now is ' + hari + ', ' + str(tanggal) + ' ' + bulan + ' ' + str(tahun))
print(text)

subprocess.call([path, text], shell=True)
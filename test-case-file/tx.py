from subprocess import Popen, PIPE

p = Popen(['./text',], shell=True, stdout=PIPE, stdin=PIPE)
print(p.stdout.readline().strip())
#print("File Created!")

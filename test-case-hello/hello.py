from subprocess import Popen, PIPE

p = Popen(['./hello'], shell=True, stdout=PIPE, stdin=PIPE)
print(p.stdout.readline().strip())

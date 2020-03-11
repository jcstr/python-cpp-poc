from subprocess import Popen, PIPE

p = Popen(['./args test test1 test2'], shell=True, stdout=PIPE, stdin=PIPE)
print(p.stdout.readline().strip())

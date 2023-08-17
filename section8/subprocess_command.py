# subprocessというものを用いて、いつもターミナルで行なっているコマンドをpython上で行う

import subprocess


subprocess.run(['ls', '-al'])
# subprocess.run('ls -al', shell=True)   # こっちはあんまり使わないようにする


# r = subprocess.run('ls', shell=True, check=True)
# print('###')

print('###############')

# パイプをやるには
p1 = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep', 'section8'], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
output = p2.communicate()[0]
print(output)
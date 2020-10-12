#coding=utf-8
# -------------------------------------
#$PYTHONHOME/bin/online2.py
onlinePy='''
#coding=utf-8
import os,sys
from fabric.api import env,run,put,output

env.hosts=['{}']
env.password='{}'
output['running']=False
output['status']=False
output['aborts']=True
env.output_prefix=False

pyhome=os.popen('echo $PYTHONHOME').read().strip()
os.chdir(pyhome+'/bin')

def shell():run('{}')
    
def file(sfile):
    dfile=sfile.split('/')[-1]
    put(sfile,dfile)
    run('{} %s'%dfile)
    
if __name__ == '__main__':
    argv=[i for i in sys.argv if i]
    if len(argv) < 2:
        os.system('fab -f online2.py shell')
    else:
        os.system('fab -f online2.py file:%s'%argv[1])
'''

#$PYTHONHOME/bin/qpython-android5.sh A
qpython_android5='''
#!/system/bin/sh
DIR=${0%/*}
. $DIR/init.sh && $DIR/python-android5 "$@" && $DIR/end.sh
'''

#$PYTHONHOME/bin/qpython-android5.sh B
qpython_android6='''
#!/system/bin/sh
DIR=${0%/*}
. $DIR/init.sh && $DIR/python-android5 $DIR/online2.py "$@" && $DIR/end.sh
'''
# -------------------------------------
	
import os,sys,re
write=sys.stdout.write


class Rterminal(object):
    hostname=''
    password=''
    command=''
    
    def __init__(self):
        pyhome = os.popen('echo $PYTHONHOME').read().strip()
        self.online=os.path.join(pyhome,'bin','online2.py')
        self.android5=os.path.join(pyhome,'bin','qpython-android5.sh')
        
        if sys.version[0]=='3':
            self.retconfig()
        
        try:
            import fabric
        except ImportError:
            print('\nHello, please install Fabric on QPYPI, and run again rterminal.py')
            sys.exit()
        if not os.path.exists(self.online):
            with open(self.online,'w') as f:
                f.write(onlinePy.format('pi@127.0.0.1:22','12345678','python','python'))

        self.getconfig()
        self.welcome()
        self.setconfig()
                         
    def welcome(self):
        from fabric.colors import yellow,green
        os.system('clear')
        print('\nRemote Terminal for QPython')
        print('rterminal is running Python on server by ssh(fabric)')
        print(yellow('You should enter the following information:'))
        write('user@hostname:port')
        write(green(' --> '))
        print(yellow(self.hostname))
        write(' '*10+'password')
        write(green(' --> '))
        print(yellow(self.password))
        write(' '*11+'command')
        write(green(' --> '))
        print(yellow(self.command))
        print('')

    def getconfig(self):
        with open(self.online,'r') as f:r=f.read()
        self.hostname=re.findall("env\.hosts=\['(.*?)'\]",r)[0]
        self.password=re.findall("env\.password='(.*?)'",r)[0]
        self.command=re.findall("def shell\(\)\:run\('(.*?)'\)",r)[0]
        
        
    def setconfig(self):
        from fabric.colors import yellow,green
        if raw_input("do you want to save the information(Enter or n): ")!='n':
            pass
        else:
            print(yellow('please enter the following information:'))
            self.hostname=raw_input('user@hostname:port --> ')
            self.password=raw_input(' '*10+'password --> ')
            self.command=raw_input(' '*11+'command --> ')
        with open(self.online,'w') as f:f.write(onlinePy.format(self.hostname,self.password,self.command,self.command))
        with open(self.android5,'w') as f:f.write(qpython_android6)
        print('\nok, rterminal is now on.')
        print(yellow('if you want to off rterminal,please switch python3 and run rterminal.py'))
        sys.exit()

    def retconfig(self):
        with open(self.android5,'w') as f:
            f.write(qpython_android5)
        print('\nok, rterminal is now off.')
        sys.exit()
    
    
def main():
    r=Rterminal()

if __name__ == '__main__':
    main()

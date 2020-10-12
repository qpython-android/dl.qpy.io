#qpy:console
__doc__ = """
Fabric for qpython, the pythonic tool for remote execution and deployment

@version: 0.1
@Author: lr
"""
__title__ = "Fabric for QPython"

import os,sys


try:
    import androidhelper
    droid = androidhelper.Android()
except:
    pass

def first_welcome():
    msg = __doc__+"\n\n"\
        +"To use fabric, you need install fabric-qpython first"
    droid.dialogCreateAlert(__title__, msg)
    droid.dialogSetPositiveButtonText('OK')
    droid.dialogSetNegativeButtonText('NO')
    droid.dialogShow()
    response = droid.dialogGetResponse().result
    if response['which'] == 'positive':
        #droid.dialogCreateSpinnerProgress(title, "Installing ...")
        os.system(sys.executable+" "+sys.prefix+"/bin/pip install fabric-qpython -i  http://qpypi.qpython.org/simple  --extra-index-url  https://pypi.python.org/simple/")
        #droid.dialogDismiss()

        message = 'Please restart this program'
        droid.dialogCreateAlert(__title__, message)
        droid.dialogSetPositiveButtonText('OK')
        droid.dialogShow()
        sys.exit()

    else:
        sys.exit()

def init_parameters():
    env.hosts=['root@127.0.0.1:22']
    env.password='admin1234'
    #env.passwords={'root@127.0.0.1:22':'admin1234'}


try:
    from fabric.api import env,run
except:
    first_welcome()
else:
    init_parameters()

ROOT    = "/sdcard/qpython"
os.chdir(os.path.dirname(__file__))

def test():
    run('python -V')

def op(msg):
    print(msg)

def modcmd(arg):
  os.system(sys.executable+" "+sys.prefix+"/bin/"+arg)

if __name__ == "__main__":

    import fabric

    modcmd("fab -h")
    op("\nok, you can change env.hosts and env.password in line 16,\nand exec this command to run test function: \nfab -f fabricman.py test\n")

    while(True):
      cmd=raw_input("-->")
      if (cmd==""): break;
      modcmd(cmd)

#qpy:console
__doc__ = """
Sqlmap for qpython

@version: 0.9
@Author: River
"""

import os,sys

ROOT    = "/sdcard/qpython"

def op(msg):
    print(msg)

def modcmd(arg):
  os.system(sys.executable+" "+sys.prefix+"/bin/"+arg)

def modcmdh(arg):
  os.system(sys.executable+" "+sys.prefix+"/bin/"+arg+" --output-dir="+ROOT+"/cache")


if __name__ == "__main__":

    op(__doc__)
    try:
        import sqlmap

        modcmd("sqlmap -h")

        while(True):
          cmd=raw_input("-->")
          if (cmd==""): break;
          modcmdh(cmd)

    except ImportError:


        opt = raw_input("QPY> sqlmap library not found, do you want to install it ?\n yes/no\n")
        if opt=='yes':
            os.system(sys.executable+" "+sys.prefix+"/bin/pip install sqlmap")
            op("You can restart this script after sqlmap being installed")


#qpy:console
#qpy://127.0.0.1:13000/?token=qpythonotebook
"""
QPython Notebook Manage Script, you could run QPyNotebook service
@version: 0.9
@Author: River
"""

import os,sys


def modcmd(arg):
  os.system(sys.executable+" "+sys.prefix+"/bin/"+arg)


if __name__ == '__main__':
    try:
        import notebook
    except:
        import androidhelper
        droid = androidhelper.Android()

        title = 'QPyNotebook'

        message = "You must enable QPyNotebook from QPython's setting"
        droid.dialogCreateAlert(title, message)
        droid.dialogSetPositiveButtonText('Close')
        droid.dialogShow()

        droid.getIntent()
        sys.exit()

    os.putenv('JUPYTER_TOKEN', 'qpythonotebook')
    modcmd("jupyter notebook --ip 0.0.0.0 --port 13000")

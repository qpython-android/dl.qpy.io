#-*coding:utf8;-*-
__doc__ = """
IPython for QPython

@version: 0.9
@Author: River

"""
def op(msg):
    print(msg)

def main():
    from IPython.terminal.prompts import Prompts, Token

    class CustomPrompt(Prompts):

        def in_prompt_tokens(self, cli=None):

           return [
                (Token.Prompt, 'In <'),
                (Token.PromptNum, str(self.shell.execution_count)),
                (Token.Prompt, '>: '),
                ]

        def out_prompt_tokens(self):
           return [
                (Token.OutPrompt, 'Out<'),
                (Token.OutPromptNum, str(self.shell.execution_count)),
                (Token.OutPrompt, '>: '),
            ]

    from traitlets.config.loader import Config
    try:
        get_ipython
    except NameError:
        nested = 0
        cfg = Config()
        cfg.TerminalInteractiveShell.prompts_class=CustomPrompt
    else:
        print("Running nested copies of IPython.")
        print("The prompts for the nested copy have been modified")
        cfg = Config()
        nested = 1

    # First import the embeddable shell class
    from IPython.terminal.embed import InteractiveShellEmbed

    # Now create an instance of the embeddable shell. The first argument is a
    # string with options exactly as you would type them if you were starting
    # IPython at the system command line. Any parameters you want to define for
    # configuration can thus be specified here.
    ipshell = InteractiveShellEmbed(config=cfg,
                           banner1 = 'IPython on QPython',
                           exit_msg = '')

    ipshell("""IPython 5.5.0 - An enhanced Interactive Python
    Type 'copyright', 'credits' or 'license' for more information, Type '?' for help, 'exit' for exit.
    """)


try:
    import platform
    if int(''.join(platform.python_version().split('.')[:-1]))<27:

        op(__doc__)
        op("You must switch to Python2.7, please install Python2 in setting")
    else:

        main()
except ImportError:
    op(__doc__)

    op("QPY> IPython library not found, please install it from QPYPI first.")


import sys
import colorama

class SacalonError:
    def __init__(self, exception_message,filename="",exit=True):
        colorama.init()
        if filename == "" :
            sys.stderr.write(colorama.Fore.RED + "Error : ")
        else :
            sys.stderr.write(colorama.Back.BLUE + colorama.Fore.WHITE + filename + "::" 
                                + colorama.Style.RESET_ALL 
                                + colorama.Fore.RED + "\nError : ")
        sys.stderr.write(colorama.Style.RESET_ALL)
        sys.stderr.write(exception_message)
        sys.stderr.write("\n")
        if exit :
            sys.exit(1)

class SacalonWarning:
    def __init__(self, warning_message,filename="",exit=False):
        colorama.init()

        if filename == "" :
            print(
                colorama.Fore.YELLOW
                + "Warning : "
                + colorama.Style.RESET_ALL
                + warning_message
            )
        else :
            print(
                colorama.Back.BLUE
                + colorama.Fore.WHITE 
                + filename 
                + "::" 
                + colorama.Style.RESET_ALL 
                + colorama.Fore.YELLOW
                + "\nWarning : "
                + colorama.Style.RESET_ALL
                + warning_message
            )
        if exit :
            sys.exit(1)
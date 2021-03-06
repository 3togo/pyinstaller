import os
import sys

basedir = sys._MEIPASS

tcldir = os.path.join(basedir, '_MEI', 'tcl')
tkdir = os.path.join(basedir, '_MEI', 'tk')

if not os.path.isdir(tcldir):
    # darwin platform uses differnt names
    tcldir = os.path.join(basedir, '_MEI', "Tcl.framework/Resources/Scripts")
    tkdir = os.path.join(basedir, '_MEI', "Tk.framework/Resources/Scripts")

os.environ["TCL_LIBRARY"] = tcldir
os.environ["TK_LIBRARY"] = tkdir

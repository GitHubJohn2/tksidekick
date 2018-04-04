#  ~~~~~~~~~ tkSidekick ~~~~~~~~~~~~~~~~
#  (c) 2018 John A Oakey
#  Permission given for educational and personal use of this program
#  Version: development: 0404A18

#  IMPORTS & ROOT SET UP
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import inspect
import pydoc
import pydoc_data
from pydoc_data import topics as pdt

root = Tk()
scrW = root.winfo_screenwidth()
scrH = root.winfo_screenheight()
root.wm_title("tkSideKick" + " "*150 + "V:0404A18 (c) 2018 John A. Oakey")
workwindow = str(1500) + "x" + str(900) + "+" + str(int((scrW-1500)/2)) + "+" + str(int((scrH-900)/2))
root.geometry(workwindow)

rtn = "\n"
top_tx_clr = "ghost white"
btm_tx_clr = "old lace"
notes_tx_clr = "grey50"
btn_clr = 'ivory3'

# ________________________________________________________________

#  DATA

widgettup = 'Toplevel', 'Button', 'Canvas', 'Checkbutton', 'Entry', 'Frame', 'Label', \
    'LabelFrame', 'Listbox', 'Menu', 'Menubutton', 'Message', 'PanedWindow',\
    'Radiobutton', 'Scale', 'Scrollbar', 'Spinbox', 'Text'

badwidget = ('toplevel', 'button', 'canvas', 'checkbutton', 'entry', 'frame', 'label',
    'labelframe', 'listbox', 'menu', 'menubutton', 'message', 'panedwindow',
    'radiobutton', 'scale', 'scrollbar', 'spinbox', 'text')

vocab = '''The inconsistency with the way various Python and tkinter information sources intermix \
and confuse terminology can be frustrating to the new programmer.  Here are the definitions we use.  
Wikipython is trying to \
standardize these terms in all our content. \n \nPlease send any comments to oakey.john@yahoo.com.   Thank you.\n\n   \
OPTION : a changeable but usually static feature of an object. An option's value can be set programatically. \
For example, "background" is one of the color-set options of a widget. \n \n\
   ATTRIBUTE: the value of an option or shorthand for an option with a specific value. "Slategray2" \
is a possible attribute of the option "background".\n \n   METHOD: an action performed by or on behalf of a specific \
widget.  "cget" and "configure" are by far the most common methods and the only two which all widgets share.\n \n\
   COMMAND: see method. \n \n   EVENT: something the user of the program does, or causes the \
   program to do, which tkinter can detect and to which it can be programmed to respond.
    '''

tipsdict = {'Toplevel': 'top1 = Toplevel(root, bg=”linen”)\ntop1.attributes(“-fullscreen”, True)\n\
top1.title(“Top 1 – Workwindow”)\ntop1.attributes(“-topmost”, 1) ', 'Button': 'b3=Button \
(root, text="Egress", command=root.destroy) ', 'Canvas': 'mycanvas = Canvas(top1, width=960, \
height=700, bg="beige")', 'Checkbutton': 'c1 = Checkbutton(f, text="Ham  $4", variable=var1, onvalue=4,\
command=cb)', 'Entry':  'e1 = Entry(top1, width=60, textvariable=in_var, bg="linen", relief=GROOVE)',
'Frame': 'f1 = Frame(top1, relief=RAISED , borderwidth=10, width=60)', 'Label': 'l1 = Label(top1, width=60,\
textvariable=in_var, bg="linen", pady=10, relief=GROOVE)', 'LabelFrame': 'lf = LabelFrame(top1, text=”This is \
a LabelFrame”, height=”2i”, width=”4i”, bg=”linen”)\nlf.pack()\nlb1 = Label(lf, text=”This is a label inside \
the LabelFrame”, bd=5, relief=GROOVE)\nlb1.pack()\ntop1.pack_propagate(False)\nlf.pack_propagate(False)',
          'Listbox': 'def initializeListBox():\n    for item in mylist:\n        listbox.insert(END, item)\nlistbox =\
Listbox(top1, font=”arial 12”)', 'Menu': 'menu = Menu(top1, bd=30)\ntop1.config(menu=menu)\nfilemenu = \
Menu(menu)\nmenu.add_cascade(label="File", menu=filemenu)\nfilemenu.add_command(label="New", command=\
NewFile)\nfilemenu.add_command(label="Open...", command=OpenFile)\nfilemenu.add_separator()\nfilemenu.add_command\
(label="Exit", command=root.quit) ', 'Menubutton': 'myMb= Menubutton (top1, text="Animals", indicatoron=True, \
justify="left")\nmyMb.pack(anchor=W)', 'Message': 'textOfMsg = "This is a message"\nmsg=Message(top1, bg="wheat1", \
text=textOfMsg, relief=GROOVE, font="Georgia 14")\nmsg.pack(padx=50, pady=50) ', 'PanedWindow': '# take up \
all the toplevel window with pw1 being the big framework\npw1 = PanedWindow(top1)\npw1.pack(fill=BOTH, \
expand=1) # use a geometry to install this widget\n# fill the left side with a big LabelFrame\nleft = \
LabelFrame(pw1, text="left pane",relief="groove", width = 400)\npw1.add(left) # pw has its own "geometry" \
for arranging things internally\n# now create another paned window inside the first one\nsubpw1 = \
PanedWindow(pw1, orient=VERTICAL)\npw1.add(subpw1)\n# and divide it up between 2 more LabelFrames\nupper = \
LabelFrame(subpw1, text="upper pane", relief="groove", height =384)\nsubpw1.add(upper)\nlower = \
LabelFrame(subpw1, text="lower pane", relief="groove")\nsubpw1.add(lower)', 'Radiobutton': 'var = \
IntVar()\nR1 = Radiobutton(top1, text="Option 1", variable=var, value=1, command=sel)\nR1.grid( column=1, \
row=1, padx=20,pady=5, ipadx=5, ipady=5, sticky=”w”)\nR2 = Radiobutton(top1, text="Option 2", variable=var, \
value=2, command=sel)\nR2.grid( column=1,row=2, padx=20, pady=5, ipadx=5, ipady=5, sticky=”w”)', 'Scale': 'def \
scaletest(self):\n    l1.configure(text=myscalevalue.get())\nmyscalevalue=IntVar()\nmyscalevalue.set\
(125)\nmyscale=Scale(top1,\n              bigincrement=30,\n              command=scaletest,\n              \
digits=3,\n              from_= 0,\n              to=255,\n              repeatdelay=900,\n              \
repeatinterval=100,\n              resolution=5,\n              tickinterval=50,\n              \
variable=myscalevalue,\n              width=100)\nmyscale.pack(pady=10)\n', 'Scrollbar': 'sbar1 = \
Scrollbar(lf1)    # create a scrollbar and pack in LabelFrame on right\nsbar1.pack(side="right", \
fill="y")\n# create a text and pack in LabelFrame on left, \
fill both\nt1=Text(lf1, width=40, height=30, wrap=CHAR, yscrollcommand=sbar1.set)\nt1.pack(side="left", \
fill="both", expand=True) # pack it in lf1\nt1.insert(END, t1text)                      # then fill it \
up\nsbar1.config(command=t1.yview) # now connect scrollbar and text frame\n', 'Spinbox'
            : 'sb1=Spinbox(top1, \
textvariable=sb1value, values=sbtuple, width=20, wrap=True)\nsb1.configure(activebackground="light \
blue",\n              bg="beige",\n              bd=10,\n              command=sbaction,\n              \
font=demofont,\n              buttonbackground="LightGoldenrod2",\n              fg="black",\n              \
justify="center",\n              repeatinterval=500,\n              width=2)\nsb1.pack(padx=300, pady=200, \
ipadx=40, ipady=30) ', 'Text': 'l1=Text(f1, width=100, height=5, bg="light goldenrod2", wrap=WORD)\nl1.grid\
(column=0,row=4, padx=10, pady=10)\nkidslist=f1.winfo_children()\nl1.insert(END, kidslist) '}

pdcrite = """copyrights for pydoc topic data extracted real time from your system: 
Copyright (c) 2001-2017 Python Software Foundation. All Rights Reserved.
Copyright (c) 2000 BeOpen.com. All Rights Reserved.
Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.
Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam. All Rights Reserved., 
credits: Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands for supporting Python development.\n
See www.python.org for more information. \n\ntkSidekick is Copyright (c) 2018 by John A. Oakey\n\n\n   
     To view one of the topics select -> Objects & Topics -> Select/Display topic.
 \n\n     A topic listing will display on the right.  Click the topic you want to review."""

widdict = dict(enumerate(widgettup, start=1))
rbvar = StringVar()  # radiobutton variable
rbvar.set("0")
current_button = StringVar()  # button currently active
current_button.set('Toplevel')
opttype = IntVar()  # which attribute option is selected
opttype.set(1)
pydoc_topics = BooleanVar()
pydoc_topics.set(False)
index_num = IntVar()
index_num.set(0)
tklist = []
listvar = StringVar()
listvar.set(tklist)
std_font = "TkFixedFont"

# ________________________________________________________________

# MENU CONSTRUCTION


# menu control function
def econtrol(cmd):
    if cmd in widgettup:
        current_button.set(cmd)
        reset("3")
        methact()
        if opttype.get() == 1:
            rbconfigshort(cmd)
        elif opttype.get() == 2:
            rbconfigcomp(cmd)
        elif opttype.get() == 3:
            rbkeys(cmd)
        else:
            messagebox.showwarning("Menu Control Failure", "An unexpected opttype value has occured", parent=lf1)
            root.destroy()
    elif cmd == "Info":
        winfolist()
    elif cmd == "wm":
        winmanager()
    elif cmd == "MA":
        methact()
    elif cmd == "Vn":
        vocabnotes()
    elif cmd == "Geo":
        geometries()
    elif cmd == "Gcon":
        glo_constants()
    elif cmd == "Tips":
        tips()
    elif cmd == "CR":
        cpyrte()
    elif cmd == "obhlp":
        obj_explore()
    elif cmd == "pdshow":
        pdshow()        # show pydoc topics
    elif cmd == "pddisplay":
        pddisplay()
    elif cmd == "py_lib_doc":
        py_lib_doc()
    elif cmd == "Cc":
        color1()
    else:
        messagebox.showwarning("Ut Oh", "Command not coded: " + cmd)
        exit()

# create the menubar itself
sidekickmenubar = Menu(root, bd=7, tearoff=0)  # create the menu widget that will be the menu bar

# create all the header labeled menus - in our special case we have a single command first
sidekickmenubar.add_command(label="Exit", command=lambda: root.destroy())

# now the pull downs
optionstypemenu = Menu(sidekickmenubar, tearoff=0)
optionstypemenu.add_radiobutton(variable=opttype, value=1,
                                label="Config: short", command=lambda: econtrol(current_button.get()))
optionstypemenu.add_radiobutton(variable=opttype, value=2,
                                label="Config: complete", command=lambda: econtrol(current_button.get()))
optionstypemenu.add_radiobutton(variable=opttype, value=3,
                                label="Keys data", command=lambda: econtrol(current_button.get()))

displaytopmenu = Menu(sidekickmenubar, tearoff=0)           # no idea why current_button.get() is necessary below
displaytopmenu.add_command(label="Options", command=lambda cmd=current_button.get(): econtrol(current_button.get()))
displaytopmenu.add_command(label="winfo Commands", command=lambda cmd='Info': econtrol(cmd))
displaytopmenu.add_command(label="wm_ Commands", command=lambda cmd='wm': econtrol(cmd))
displaytopmenu.add_command(label="Instantiate ex", command=lambda cmd='Tips': econtrol(cmd))

displaybottommenu = Menu(sidekickmenubar, tearoff=0)
displaybottommenu.add_command(label="Methods/Actions", command=lambda cmd='MA': econtrol(cmd))
displaybottommenu.add_command(label="Geometries", command=lambda cmd='Geo': econtrol(cmd))
displaybottommenu.add_command(label="Constants (global)", command=lambda cmd="Gcon": econtrol(cmd))
displaybottommenu.add_command(label="Color Chooser", command=lambda cmd="Cc": econtrol(cmd))

displayaboutmenu = Menu(sidekickmenubar, tearoff=0)
displayaboutmenu.add_command(label="Vocabulary notes", command=lambda cmd='Vn': econtrol(cmd))
displayaboutmenu.add_command(label="About", command=lambda cmd="CR": econtrol(cmd))

displayhelpmenu = Menu(sidekickmenubar, tearoff=0)
displayhelpmenu.add_command(label="Basic Object Search", command=lambda cmd="obhlp": econtrol(cmd))
displayhelpmenu.add_command(label="Show pydoc topics", command=lambda cmd="pdshow": econtrol(cmd))
displayhelpmenu.add_command(label="List & Select topics", command=lambda cmd="pddisplay": econtrol(cmd))
displayhelpmenu.add_command(label="Python Library Docs", command=lambda cmd="py_lib_doc": econtrol(cmd))

# add cascade entries to the menu bar
sidekickmenubar.add_cascade(label="Options Source", menu=optionstypemenu)
sidekickmenubar.add_cascade(label="Top Display", menu=displaytopmenu)
sidekickmenubar.add_cascade(label="Bottom Display", menu=displaybottommenu)
sidekickmenubar.add_cascade(label="Objects & Topics", menu=displayhelpmenu)
sidekickmenubar.add_cascade(label="About", menu=displayaboutmenu)

# last but not least, add the menu bar to the root or toplevel
root.config(menu=sidekickmenubar)

# ________________________________________________________________

# CONTAINTER WIDGETS SET UP FOR APP
# We will use two Panedwindows and three labelFrames for 3 display panels

# first, a main panedwindow to hold everything
mainPw = PanedWindow(root, width=1500, height=800, bg="grey30")
mainPw.pack(fill=BOTH, expand=1)
# and we secure a vertical area on the left side with a labelframe - Radiobuttons go in here
lf1 = LabelFrame(mainPw, relief=GROOVE, width=400, bd=12, bg='grey90')
mainPw.add(lf1)
# now another panedwindow to hold the rest of the area, but spliting it in vertical areas
vSplitPw = PanedWindow(mainPw, orient=VERTICAL)
mainPw.add(vSplitPw)
# finally, 2 labelframes to divide
lftop = LabelFrame(vSplitPw, relief=GROOVE, width=1100, height=400, text="top pane", bd=12)
vSplitPw.add(lftop)
lfbottom = LabelFrame(vSplitPw, relief=GROOVE, width=1100, text="bottom pane", bd=12)
vSplitPw.add(lfbottom)
# now call propagate
mainPw.pack_propagate(False)
# Install top text display and Scrollbar...
sbartop = Scrollbar(lftop)
sbartop.pack(side="right", fill="y")
t1 = Text(lftop, font="Consolas 9", bg=top_tx_clr, yscrollcommand=sbartop.set)  # bg=top_tx_clr???
t1.pack(anchor=NW, expand=TRUE, fill='both')
sbartop.config(command=t1.yview)
# ...and bottom text display and Scrollbar
sbarbtm = Scrollbar(lfbottom)
sbarbtm.pack(side="right", fill="y")
t2 = Text(lfbottom, bg=btm_tx_clr, wrap='word', yscrollcommand=sbarbtm.set)
t2.pack(expand=TRUE, fill='both')
sbarbtm.config(command=t2.yview)
# a little room left for a small text box - maybe for notes?
linelabel = Label(lf1, height=1, bg="blue", fg="white", text='NOTES', font="bold")
linelabel.grid(column=1, row=19, sticky=E+W)
geotext = Text(lf1, height=18, bg=notes_tx_clr, fg="white", width=15, font="Consolas 8")
geotext.grid(column=1, row=20)
geotext.insert(END, "WIKIPYTHON.COM\n")
lf1.pack_propagate(False)

# ________________________________________________________________

#  U T I L I T Y  and  S E T U P   F U N C T I O N S


#  create radio buttons given a widget name and value
def rb(widname, val):
    rbvar.set(val)
    newrbut = Radiobutton(lf1, text=widname, variable=rbvar, value=val, indicatoron=FALSE, bg=btn_clr,
                          command=lambda: econtrol(widname))
    newrbut.grid(column=1, row=int(val), sticky=E + W)
    return newrbut


#  returns the dir results minus most non-callable methods
def clear_list(info_object):
    method_list = (dir(eval(info_object)))
    clean_list = []
    for item in method_list:
        if not (item.startswith('_') or item.startswith('winfo')):
            clean_list.append(item)
    return clean_list


#  insets clear_list into top text box
def objdir(info_object):
    newobj = clear_list(info_object)
    reset('1')
    for item in newobj:
        t1.insert(END, item)
        t1.insert(END, "\n")
    return clear_list


def reset(cmd):
    ht = "Thanks for using tksidekick - www.wikipython.com"
    if cmd == "1":
        t1.delete(1.0, END)
        t1.config(font=std_font)
        t1.config(bg=top_tx_clr)
        headertitle(lftop, ht)
    elif cmd == "2":
        t2.delete(1.0, END)
        t2.config(font=std_font)
        t2.config(bg=btm_tx_clr)
        headertitle(lfbottom, ht)
    elif cmd == "3":
        t1.delete(1.0, END)
        t1.config(font=std_font)
        t1.config(bg=top_tx_clr)
        headertitle(lftop, ht)
        t2.delete(1.0, END)
        t2.config(font=std_font)
        t2.config(bg=btm_tx_clr)
        headertitle(lfbottom, ht)
    else:
        messagebox.showwarning("Reset fell through - 310", "An unexpected opttype value has occured", parent=lf1)


#  puts a bold header title on selected text box 1/top 2/bottom
def headertitle(pane, tstring):
    pane.config(text=tstring, font="Arial 10 bold")


#  For a list, calc the # of cols avail, insert items in cols across til done
def listincols(pane, outlist):
    panel = eval("t" + pane)  # top and bottom text panels are t1 and t2
    scrnwidth = eval("t" + pane + ".winfo_width()")  # get screen width
    pix_inch = 9.3
    itemlengths = []
    sw_char = int(scrnwidth/pix_inch)
    for aug in range(len(outlist)):
        itemlengths.append(len(outlist[aug]))
    maxlen = max(itemlengths) + 2   # find the longest string in outlist in chars, add 2
    availcols = int(sw_char/maxlen)  # calculate the number of available columns
    itemcount = len(outlist)  # get total number of items to display
    itemnum = 0  # reset a counter to track what we display

    while itemcount > 0:
        nxlineitemsqty = availcols if (itemcount >= availcols) else itemcount  # set items in next line
        nxline = ""
        for item in range(1, nxlineitemsqty + 1):
            nxline += f"{outlist[itemnum + item -1]: <{maxlen}s}"
            itemcount -= 1
        panel.insert(END, nxline)
        panel.insert(END, "\n")
        itemnum += nxlineitemsqty


# ________________________________________________________________


# A C T I V I T Y    F U N C T I O N S

#  Short option list from configure
def rbconfigshort(widstr):  # gets and prints a concise list of options and default attributes
    w1 = eval(widstr)(lfbottom)
    reset('1')
    header = f"{'OPTIONS': <30s}" + "DEFAULT/CURRENT VALUE"
    t1.insert(END, header + rtn)
    wdictionary = w1.config()  # get all options from configure
    wditems = iter(wdictionary)
    attribute = ""
    while attribute is not "stopend":
        attribute = next(wditems, "stopend")
        if attribute == "stopend":
            break
        else:
            t1.insert(END, f"{attribute : <30s}")
            t1.insert(END, w1.cget(attribute))
            t1.insert(END, rtn)
    w1.destroy()
    current_button.set(widstr)
    headertitle(lftop, "Options/Attributes (short list) from 'configure' for widget class:  " + widstr + " ")


#   Complete option value from option dictionary returned
def rbconfigcomp(cmd):
    widget_temp = eval(cmd)(lftop)  # design in but do not pack it
    widdict = widget_temp.config()  # get all option info
    reset('1')
    header = f"{'OPTIONS': <30s}" + "COMPLETE KEY VALUES TUPLE"
    t1.insert(END, header + rtn)
    v = iter(widdict)
    optattrib = ""
    while optattrib is not "endit":
        optattrib = next(v, "endit")
        if optattrib == "endit":
            break
        t1.insert(END, F"{optattrib: <22s}")
        t1.insert(END, "     ")
        t1.insert(END, ascii(widdict[optattrib]))
        t1.insert(END, rtn)
    widget_temp.destroy()
    current_button.set(cmd)
    headertitle(lftop, "Options/Attributes (complete) from 'configure' for widget class:  "
                + current_button.get() + " ")


#  Options and Attributes from a KEY query of an object name
def rbkeys(cmd):
    reset('1')
    w3 = eval(cmd)(lftop)
    attribs = w3.keys()
    akeys = iter(attribs)
    attribute = ""
    header = f"{'OPTION NAME': <27s}" + f"{'ATTRIBUTE CLASS': <32s}" + "DEFAULT VALUE\n"
    t1.insert(END, header)
    while attribute is not "_____":
        attribute = next(akeys, "_____")
        if attribute == "_____":
            t1.insert(END, attribute)
            break
        t1.insert(END, f"{attribute: <27s}")
        t1.insert(END, f"{str(type(w3[attribute])): <32s}")
        t1.insert(END, f"{w3[attribute]}")
        t1.insert(END, "\n")
    current_button.set(cmd)
    headertitle(lftop, "Options/Attributes from key() query for widget class:  " + current_button.get() + " ")
    w3.destroy()


#  Information (winfo) commands - not displayed with toplevel commands
def winfolist():
    reset('1')
    t1.insert(END, "Winfo commands give an access to a world of environmental information. For example:\nif the "
                   "name of your toplevel wideget is 'Top1', you can get a list of all the\nchild widgets "
                   "managed under Top1 with the command: 'top1.winfo_children'\nSome addition information may "
                   "be available - use Basic Object Search and join 'Toplevel' to the winfo \ncommand, "
                   "for example: 'Toplevel.winfo_children'.\n\n")
    tlist = (dir(Toplevel))
    clean_list = []
    for item in tlist:
        if item.startswith('winfo'):
            clean_list.append(item)

    listincols("1", clean_list)
    headertitle(lftop, "Information (winfo_) Commands - use with root or Toplevel   ")


#  Window Manager (wm_ commands - not displayed with toplevel commands
def winmanager():
    reset("1")
    t1.insert(END, "Many of the window manager commands below may have document text that can be seen by using either"
                   " 'Basic Object Search' or 'Python Library Docs' under the 'Objects and Topics' tab if they are "
                   "linked to the Toplevel widget. i.e., search for 'Toplevel.iconbitmap'\n\n")
    tplist = (dir(Toplevel))
    clean_list = []
    for item in tplist:
        if item.startswith('wm_'):
            shortitem = item[3:len(item)]
            clean_list.append(f"{shortitem: <19}" + item)
    listincols("1", clean_list)
    t1.insert(END, "\nThe 'attributes command is especially helpful.\nOptions of wm_atributes are:" + rtn)
    t1.insert(END, '"-alpha", "-topmost", "-disabled", "-type",'
                   '"-transparentcolor", "-toolwindow", "-fullscreen", "-transparent", "-titlepath"' + rtn)
    t1.insert(END, 'Example: root.attributes("-fullscreen", TRUE)')
    t1.insert(END, "\nspecial note: fullscreen is new in version 8.6")
    headertitle(lftop, "Window Manager (wm_) commands - note the 'wm_' part is now optional ")


#  All methods or actions returned that are associated with the selected widget object
def methact():
    reset('2')
    current_widget = current_button.get()
    if current_widget == 'Menubutton':
        t2.insert(END, "Special Note: Menubutton is obsolete.\n")
    t2.insert(END, "Display all " + current_widget + " related method and action key words.\n")
    headertitle(lfbottom, "All Methods and Actions for widget class: " + current_widget + " ")
    # set up section headers
    headerunderline = "*" * 18
    standardlist = [rtn + "STANDARD Methods" + rtn, headerunderline + rtn]
    winfolist = [rtn + "INFORMATION Methods" + rtn, headerunderline + rtn]
    specmethlist = [rtn + "SPECIAL Methods" + rtn, headerunderline + rtn]
    privatelist = [rtn + "PRIVATE Methods" + rtn, headerunderline + rtn]
    wmlist = [rtn + "WINDOW MGR Methods" + rtn, headerunderline + rtn]
    # get dir info on the widget and separate it into categories
    objmethlist = (dir(eval(current_widget)))
    for item in objmethlist:
        if item.startswith('winfo'):
            winfolist.append(item)
        elif item.startswith('__') and item.endswith('__'):
            specmethlist.append(item)
        elif item.startswith('_'):
            privatelist.append(item)
        elif item.startswith('wm_'):
            wmlist.append(item)
        else:
            standardlist.append(item)
    # now print headers and send lists to listincols
    obj_list = [standardlist, specmethlist, privatelist, winfolist, wmlist]
    for category in obj_list:
        if len(category) == 2:
            category.append("None")
    for category in obj_list:
        temp = category.pop(0)
        t2.insert(END, temp)
        t2.insert(END, category.pop(0))
        listincols("2", category)


#  Short notes on terms and meanings
def vocabnotes():
    reset('2')
    t2.config(font=12)
    t2.insert(END, vocab)
    headertitle(lfbottom, "Vocabulary Notes")


#  List of all geometry methods returned by pack, grid or place in 3 columns
def geometries():
    t2.config(font='TkFixedFont')
    gridlist = clear_list('Grid')
    packlist = clear_list('Pack')
    placelist = clear_list('Place')
    lenmax = max(len(gridlist), len(packlist), len(placelist))
    if len(gridlist) < lenmax:
        adds = int(lenmax - len(gridlist))
        for inc in range(0, adds):
            gridlist.append("-")
    if len(packlist) < lenmax:
        adds = lenmax - len(packlist)
        for inc in range(0, adds):
            packlist.append("-")
    if len(placelist) < lenmax:
        adds = lenmax - len(placelist)
        for inc in range(0, adds):
            placelist.append("-")
    geoprint = ""
    for inc in range(0, lenmax):
        xstr = (f"{gridlist[inc]: <40}" + f"{packlist[inc]: <40}" + f"{placelist[inc]: <40}" + "\n")
        geoprint += xstr
    reset('2')
    t2.insert(END, f'{"G R I D": <40}' + f'{"P A C K": <40}' + f'{"P L A C E": <40}' + "\n")
    t2.insert(END, geoprint)
    headertitle(lfbottom, "Geometry Methods: Grid, Pack and Place ")


# List of constants in the global scope
def glo_constants():
    names_in_global_scope = (globals())
    nls = names_in_global_scope.copy()
    headertitle(lfbottom, 'Constants in global scope from globals()')
    global_constants = []
    v = iter(nls)
    nextname = ""
    while nextname is not "stop_end":
        nextname = str(next(v, "stop_end"))
        if nextname.startswith("names_in_global_scope"):
            pass
        elif nextname.isupper():
            global_constants.append(f"{nextname: <12s}" + "=  " + str(nls[nextname]) + " ")
    reset('2')
    listincols("2", global_constants)

    addtxt1 = '''  The following constants live in Python's built-in namespace: \n\
False, True, None, NotImplemented, Ellipis, __debug__ \n\
Attempted assignments to None, False, True or __debug__ raise SyntaxError. \n\
__________________________________________________________________________________\n\n\
  These constants are added by the automatically imported site module:\n\
quit(code=None), exit(code=None) \n\
  When printed, these objects print a message like “Use quit() or Ctrl-D (i.e. EOF) to exit", \n\
  and when called, raise SystemExit with the specified exit code.\n\
copyright , credits\n\
  These objects when printed or called, print the text of copyright or credits, respectively.\n\
  And finally,\n\
license \n\
  An object that when printed, prints the message “Type license() to see the full license text”,\n\
and when called, displays the full license text in a pager-like fashion (one screen at a time).\n'''
    t2.insert(END, "\n")
    t2.insert(END, addtxt1)


# examples under top display
def tips():
    reset("1")
    t1.insert(END, "Typical example code (partial) for: ")
    t1.insert(END, current_button.get() + "\n\n")
    t1.insert(END, tipsdict[current_button.get()])
    headertitle(lftop, " Partial code example of typical instantiation of: " + current_button.get())


# Copyright and credits info text for ABOUT menu choice under help
def cpyrte():
    cpyrte_text = "tksidekick copyright 2018 by John A. Oakey\nAll commercial rights are reserved.\n\n" \
                "Permission is given for free personal use and for distribution within a public " \
                "or non-profit educational institution or group.\n\n" \
                "tksidekick (c) is a project developed for www.wikipython.com by John A. Oakey.\n" \
                "www.wikipython.com is a non-commerical hobby enterprise.\n\nPlease send comments to: oakey.john@yahoo.com\n\n" \
                "More information about tksidekick and a download url for GitHub may (or may not) " \
                "be available on www.wikipython.com\n\nAdditional coding and concepts by:\n\nMany thanks " \
                "to tksidekick's Beta testers:\n"
    reset('1')
    t1.config(font=12)
    t1.insert(END, cpyrte_text)


# explore object using the object string and the inspect module
def obj_explore():
    global obj1
    global objstr
    obj1 = ""   # will hold the object
    objstr = ""  # will hold a copy of obj when it is input
    helpout = ""  # will hold string for lower panel
    init = "__init__"
    reset("3")  # clears both panels
    headertitle(lftop, "Explore an Object")  # reestablish panel heads
    headertitle(lfbottom, "Information for " + objstr)
    obj = simpledialog.askstring("Short Help Report for an Object", "Enter a possible\
 object term (like, 'Button', 'ord', or 'print')", parent=t1)
    objstr = obj  # make a copy
    if obj is None or type(obj) is 'NoneType' or obj == "":   # handle cancel or no response
        obj = "No input"
        objstr = obj
        t1.insert(END, "No input received.")
        helpout = "no selection was made" + " :: " + rtn
        t2.insert(END, helpout)
        return
    try:
        obj1 = eval(str(obj))
    except Exception as e:
        if objstr.lower() in badwidget:  # check for bad widget capitalization is eval fails
            index_num.set(badwidget.index(objstr.lower()))
            objstr = widgettup[index_num.get()]  # load good spelling of Widget
            obj1 = eval(objstr)  # and with it get a good object in obj1
            helpout = "Input received was: " + obj + "\nPossible bad widget capitalization: \nReturning " \
                                                     "information for " + objstr + rtn
            obj = objstr
        else:
            reset("2")
            helpout = helpout + obj + " :  " + str(e) + " - can not evaluate as an object." + rtn   # use original value
            t2.insert(END, helpout)
            t1.insert(END, "Oops")
            return
    finally:
        try:
            obdoc = inspect.getdoc(obj1)  # use inspect.getdoc to get object docs
        except Exception as e:  # what? no doc string?
            helpout = helpout + objstr + " " + str(e) + "  -  does not have a document string."
            t2.insert(END, helpout)
            return
        else:
            if objstr in widgettup:   # if this is a widget update the buttons
                index_num.set(widgettup.index(objstr))
                current_button.set(objstr)
                rbvar.set(index_num.get() + 1)
                tips()
            helpout = helpout + "doc string: " + str(obdoc) + rtn
        try:  # add init doc for the object
            initstr = eval(objstr + "." + init).__doc__
            helpout = helpout + "initialization string: " + initstr + rtn + rtn
        except Exception as e:
            initstr = "'obj'" + " returned with " + str(e)
            helpout += " " + initstr
    if obj in widgettup and obj != "Toplevel":
        gridstr = eval(obj + "." + "grid").__doc__
        gridhdr = "Abbreviated Grid help for " + objstr + ":" + rtn
        helpout = helpout + gridhdr + gridstr + rtn
        packstr = eval(obj + "." + "pack").__doc__
        packhdr = "Abbreviated Pack help for " + obj + ":" + rtn
        helpout = helpout + packhdr + packstr + rtn
        placestr = eval(obj + "." + "place").__doc__
        placehdr = "Abbreviated Place help for " + obj + ":" + rtn
        helpout = helpout + placehdr + placestr + rtn
        current_button.set(obj)
        rbvar.set(index_num.get() + 1)
        tips()
    elif obj == "Toplevel":
        current_button.set(obj)
        rbvar.set(index_num.get() + 1)
        tips()
        root.update()
    else:
        reset("1")
        t1.insert(END, "Input received: " + obj + "\n")
        if obj == "":
            t1.insert(END, "Unknown Input")
        elif obj != NONE:
            t1.insert(END, 'Python object.' + rtn)
        else:
            t1.insert(END, 'No input.' + rtn)
            t1.insert(END, 'Please see below')
    reset("2")
    t2.insert(END, helpout)
    return


# explore object using pydoc.render to get Python Library documentation
def py_lib_doc():
    global obj1
    global objstr
    obj1 = ""   # will hold the object
    objstr = ""  # will hold a copy of obj when it is input
    helpout = ""  # will hold string for lower panel
    reset("3")  # clears both panels
    headertitle(lftop, " Explore an Object ")  # reestablish panel heads
    headertitle(lfbottom, " Information for " + objstr)
    obj = simpledialog.askstring("Short Help Report for an Object", "Enter a possible\
    object term (like, 'Button', 'ord', or 'print')", parent=t1)
    objstr = obj  # make a copy
    if obj is None or type(obj) is 'NoneType' or obj == "":   # handle cancel or no response
        obj = "No input"
        objstr = obj
        t1.insert(END, "No input received.")
        helpout = "no selection was made" + " :: " + rtn
        t2.insert(END, helpout)
        return
    else:
        t1.insert(END, "Possible object to be evaluated: " + objstr)
    try:
        obj1 = eval(obj)
    except Exception as e:
        if objstr.lower() in badwidget:  # check for bad widget capitalization is eval fails
            index_num.set(badwidget.index(objstr.lower()))
            objstr = widgettup[index_num.get()]  # load good spelling of Widget

            obj1 = eval(objstr)  # and with it get a good object in obj1
            helpout = "Input received was: " + obj + "\nPossible bad widget capitalization: \nReturning " \
                                                     "information for " + objstr + rtn
            obj = objstr
            t2.insert(END, helpout)
        else:
            print('how did it get here?')
            reset("2")
            helpout = helpout + obj + " " + str(e) + " - can not evaluate as an object." + rtn  # use original value
            t2.insert(END, helpout)
            return
    finally:
        try:
            pldoc = pydoc.render_doc(obj1)
        except Exception as e:  # what? no doc string?
            helpout = helpout + objstr + " " + str(e) + "  -  does not have a document string."
            t2.insert(END, helpout)
            return
        finally:
            v = iter(pldoc)
            code = chr(0)  # null char
            while code != chr(4):  # end of transmission character
                code = next(v, chr(4))
                if ord(code) == 124:
                    code = " "
                    t2.insert(END, code)
                elif ord(code) == 8:
                    code = next(v, chr(4))
                else:
                    t2.insert(END, code)
    return


# Display pydoc (c) in top panel and list of topics available in bottom panel
def pdshow():
    headertitle(lftop, ' Copyright (c) notice for pydoc topics ')
    reset("3")
    t1.insert(END, pdcrite)
    t1.insert(END, "\n\n")
    headertitle(lfbottom, ' Help topics available in pydoc data ')
    listincols("2", tklist)


# create a listbox for selection of a topic with instruction message
def pddisplay():
    pydoc_topics.set(True)  # a flag - we have this data already
    reset("3")     # clears and resets top and bottom
    t1.insert(END, '\n'*10 + "  "*20 + 'Please select a topic from the list at right '+chr(10144))
    headertitle(lftop, ' Select pydoc Topic at Right-> ')
    headertitle(lfbottom, " Your Chosen Help Topic Will Display Here ")
    mystr = StringVar()
    mystr.set("")
    listvar.set(tklist)

    def callback(self):
        idextup = lbx.curselection()
        idex = int(idextup[0])
        try:
            mystr.set(tklist[idex])
            if mystr.get() == "~~~ CLOSE ~~~":
                lbx.destroy()
                scrollbar.destroy()
                reset("3")
                return
        except Exception as e:
            reset("3")
            lbx.pack_forget()
            scrollbar.pack_forget()
            pydoc_topics.set(FALSE)
            t1.insert(END, pdcrite)
            t1.insert(END, "\nidex= "+str(idex))
            t2.insert(END, "\nexception encountered: " + str(idex) + " / " + str(e))
            geotext.focus_set()
        else:
            headertitle(lfbottom, " You Selected Help Topic: " + mystr.get() + " ")
            reset("2")
            t2.insert(END, pdt.topics[tklist[idex]])
            lbx.pack_forget()
            scrollbar.pack_forget()
            reset("1")
            t1.insert(END, pdcrite)

    scrollbar = Scrollbar(t1, bd=7, cursor="cross", background="aliceblue")
    scrollbar.pack(side=RIGHT, fill=Y)
    lbx = Listbox(t1, relief=GROOVE, bd=8, yscrollcommand=scrollbar.set, cursor="arrow",
                  bg="Slategray1", selectmode="browse", listvariable=listvar, width=20)
    lbx.pack(expand=True, fill=Y, anchor=E)
    scrollbar.config(command=lbx.yview)
    lbx.bind("<<ListboxSelect>>", callback)
    lbx.focus_set()
    root.update()


def color1():
    reset("2")
    from tkinter import colorchooser
    t2.insert(END, "Results from Color Chooser selection by pressing 'OK': \n")
    rgb_color, web_color = colorchooser.askcolor(parent=t2, initialcolor=(255, 0, 0))
    t2.insert(END, "The RBG formula tuple for your color: " + repr(rgb_color) + rtn)
    t2.insert(END, "The web (hex value) for you (closest) color should be: " + repr(web_color) + rtn)
    t2.insert(END, "Note: you can copy and paste these value to NOTES.")


# ________________________________________________________________

# CREATING THE PROGRAM -

# Set up the radiobuttons - "rb"
for i in range(len(widgettup)):
    newrb = rb(widgettup[i], str(i+1))
rbvar.set("1")  # highlight the first button)
rbconfigshort(current_button.get())
root.update()
methact()
root.update()

# Grab the pydoc data
tklist = list(pdt.topics)
tklist.insert(0, "~~~ CLOSE ~~~")

# ________________________________________________________________

#  and now the symphony begins

root.mainloop()

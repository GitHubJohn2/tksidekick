#  ~~~~~~~~~ tkSidekick ~~~~~~~~~~~~~~~~
#  (c) 2018 John A Oakey
#  Permission given for educational and personal use of this program
#  Version: development: 031118C

#  IMPORTS & ROOT SET UP
from tkinter import *
root = Tk()
scrW = root.winfo_screenwidth()
scrH = root.winfo_screenheight()
root.wm_title("tkSideKick" + " "*150 + "V:A031118C  (c) 2018 John A. Oakey")
workwindow = str(1500) + "x" + str(900) + "+" + str(int((scrW-1500)/2)) + "+" + str(int((scrH-900)/2))
root.geometry(workwindow)

#  DATA
widgetlist = ['Toplevel', 'Button', 'Canvas', 'Checkbutton', 'Entry', 'Frame', 'Label',
'LabelFrame', 'Listbox', 'Menu', 'Menubutton', 'Message', 'PanedWindow',
'Radiobutton', 'Scale', 'Scrollbar', 'Spinbox', 'Text']
vocab = '''The almost humorous inconsistency with the way various Python and tkinter information sources intermix \
and confuse terminology can be frustrating to the new programmer.  We will leave the discussion of what terminology \
"should be" to another venue.  In this program the following are our definitions. Wikipython is trying to \
standardize these terms in all our content.  Please send any comments to oakey.john@yahoo.com.   Thank you. \n  \n \
OPTION : a changeable but usually static feature of an object. An option's value can be set programatically. \
For example, "background" is one of the color-set options of a widget. \n \n \
ATTRIBUTE: the value of an option or shorthand for an option with a specific value. "Slategray2" \
is a possible attribute of the option "background".\n \n METHOD: an action performed by or on behalf of a specific \
widget.  "cget" and "configure" are by far the most common methods and the only two which all 18 widgets share.\n \n \
COMMAND: see method. \n \n EVENT: something the user of the program does, or causes the program to do, which tkinter \
can detect and to which it can be programmed to respond.
'''
widdict = dict(enumerate(widgetlist, start=1))
rbvar = StringVar()
rbvar.set("0")
current_button = StringVar()
current_button.set('Toplevel')
opttype = IntVar()
opttype.set(1)


# MENU CONSTRUCTION

# menu control function
def econtrol(cmd):
    if cmd in widgetlist:
        current_button.set(cmd)
        methact()
        if opttype.get() == 1:
            rbconfigshort(cmd)
        elif opttype.get() == 2:
            rbconfigcomp(cmd)
        elif opttype.get() == 3:
            rbkeys(cmd)
    elif cmd == "Info":
        winfolist(cmd)
    elif cmd == "wm":
        winmanager(cmd)
    elif cmd == "MA":
        methact()
    elif cmd == "Vn":
        vocabnotes(cmd)
    elif cmd == "Geo":
        geometries(cmd)
    elif cmd == "Gcon":
        glo_constants()
    elif cmd == "CR":
        cpyrte()

# create the menubar itself
sidekickmenubar = Menu(root, bd=7, tearoff=0)  # create the menu widget that will be the menu bar

# create all the header labeled menus
# in our special case we have a single command first
sidekickmenubar.add_command(label="Exit", command=lambda: root.destroy())

# now the pull downs
optionstypemenu = Menu(sidekickmenubar, tearoff=0)
optionstypemenu.add_radiobutton(variable=opttype, value=1, label="Config: short", command=lambda: econtrol(current_button.get()))
optionstypemenu.add_radiobutton(variable=opttype, value=2, label="Config: complete", command=lambda: econtrol(current_button.get()))
optionstypemenu.add_radiobutton(variable=opttype, value=3, label="Keys data", command=lambda: econtrol(current_button.get()))

displaytopmenu = Menu(sidekickmenubar, tearoff=0)
displaytopmenu.add_command(label="Options", command=lambda cmd=current_button.get(): econtrol(cmd))
displaytopmenu.add_command(label="Info Commands", command=lambda cmd='Info': econtrol(cmd))
displaytopmenu.add_command(label="wm_ Commands", command=lambda cmd='wm': econtrol(cmd))

displaybottommenu = Menu(sidekickmenubar, tearoff=0)
displaybottommenu.add_command(label="Methods/Actions", command=lambda cmd='MA': econtrol(cmd))
displaybottommenu.add_command(label="Geometries", command=lambda cmd='Geo': econtrol(cmd))
displaybottommenu.add_command(label="Constants (global)", command=lambda cmd="Gcon": econtrol(cmd))

displayaboutmenu = Menu(sidekickmenubar, tearoff=0)
displayaboutmenu.add_command(label="Vocabulary notes", command=lambda cmd='Vn': econtrol(cmd))
displayaboutmenu.add_command(label="About", command=lambda cmd="CR": econtrol(cmd))

# add cascade entries to the menu bar
sidekickmenubar.add_cascade(label="Options Source", menu=optionstypemenu)
sidekickmenubar.add_cascade(label="Top Display", menu=displaytopmenu)
sidekickmenubar.add_cascade(label="Bottom Display", menu=displaybottommenu)
sidekickmenubar.add_cascade(label="Help", menu=displayaboutmenu)

# last but not least, add the menu bar to the root or toplevel
root.config(menu=sidekickmenubar)


# CONTAINTER WIDGETS SET UP FOR APP
# We will use two Panedwindows and three labelFrames for 3 display panels

# first, a main panedwindow to hold everything
mainPw = PanedWindow(root, width=1500, height=800, bg="black")
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
t1 = Text(lftop, font="Consolas 9", bg="linen", yscrollcommand=sbartop.set)
t1.pack(anchor=NW, expand=TRUE, fill='both')
sbartop.config(command=t1.yview)
# ...and bottom text display and Scrollbar
sbarbtm = Scrollbar(lfbottom)
sbarbtm.pack(side="right", fill="y")
t2 = Text(lfbottom, bg="aliceblue", wrap='word', yscrollcommand=sbarbtm.set)
t2.pack(expand=TRUE, fill='both')
sbarbtm.config(command=t2.yview)
# a little room left for a small text box - maybe for notes?
linelabel = Label(lf1, height=1, bg="blue", fg="white", text='NOTES', font="bold")
linelabel.grid(column=1, row=19, sticky=E+W)
geotext = Text(lf1, height=18, bg="Slategray3", width=15, font="Consolas 8")
geotext.grid(column=1, row=20)
geotext.insert(END, "WIKIPYTHON.COM")
lf1.pack_propagate(False)

#  U T I L I T Y  and  S E T U P   F U N C T I O N S

#  create radio buttons given a widget name and value
def rb(widname, val):
    rbvar.set(val)
    newrbut = Radiobutton(lf1, text=widname, variable=rbvar, value=val, indicatoron=FALSE, bg='grey90',
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
    t1.delete(1.0, END)
    for item in newobj:
        t1.insert(END, item)
        t1.insert(END, "\n")
    return clear_list


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


# A C T I V I T Y    F U N C T I O N S

#  Short option list from configure
def rbconfigshort(widstr):  # gets and prints a concise list of options and default attributes
    rtn = "\n"
    w1 = eval(widstr)(lfbottom)
    t1.delete(1.0, END)
    header = f"{'OPTIONS': <30s}" + "DEFAULT/CURRENT VALUE"
    t1.insert(END, header + rtn)
    wdictionary = w1.config()
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
    headertitle(lftop, "Options/Attributes (short list) from 'configure' for widget class:  " + widstr + " ")


#   Complete option value from option dictionary returned
def rbconfigcomp(cmd):
    rtn = "\n"
    w2 = eval(cmd)(lftop)  # design in but do not pack it
    widdict = w2.config()
    t1.delete(1.0, END)
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
    w2.destroy()
    headertitle(lftop, "Options/Attributes (complete) from 'configure' for widget class:  " + cmd + " ")


#  Options and Attributes from a KEY query of an object name
def rbkeys(cmd):
    t1.delete(1.0, END)
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
    headertitle(lftop, "Options/Attributes from key() query for widget class:  " + cmd + " ")
    w3.destroy()


#  Information (winfo) commands - not displayed with toplevel commands
def winfolist(cmd):
    tlist = (dir(Toplevel))
    clean_list = []
    for item in tlist:
        if item.startswith('winfo'):
            clean_list.append(item)
    t1.delete(1.0, END)
    listincols("1", clean_list)
    headertitle(lftop, "Information (winfo_) Commands - use with root or Toplevel   ")


#  Window Manager (wm_ commands - not displayed with toplevel commands
def winmanager(cmd):
    tplist = (dir(Toplevel))
    clean_list = []
    rtn = "\n"
    for item in tplist:
        if item.startswith('wm_'):
            shortitem = item[3:len(item)]
            clean_list.append(f"{shortitem: <19}" + item)
    t1.delete(1.0, END)
    listincols("1", clean_list)
    t1.insert(END, "Options of wm_atributes are:" + rtn)
    t1.insert(END, '"-alpha", "-topmost", "-disabled", "-type",'
                   '"-transparentcolor", "-toolwindow", "-fullscreen", "-transparent", "-titlepath"' + rtn)
    t1.insert(END, 'Example: root.attributes("-fullscreen", TRUE)')
    t1.insert(END, "   special note: fullscreen is new in version 8.6")
    headertitle(lftop, "Window Manager (wm_) commands - note the 'wm_' part is now optional ")


#  All methods or actions returned that are associated with the selected widget object
def methact():
    t2.delete(1.0, END)
    current_widget = current_button.get()
    t2.insert(END, "Display all SELECTED WIDGET method and action key words.\n")
    headertitle(lfbottom, "All Methods and Actions for widget class: " + current_widget + " ")
    # set up section headers
    headerunderline = "*" * 18
    rtn = "\n"
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
def vocabnotes(cmd):
    t2.delete(1.0, END)
    t2.insert(END, vocab)
    headertitle(lfbottom, "Vocabulary Notes")


#  List of all geometry methods returned by pack, grid or place in 3 columns
def geometries(cmd):
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
    t2.delete(1.0, END)
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
    t2.delete(1.0, END)
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


# text for ABOUT menu choice under help
def cpyrte():
    cpyrte_text = "tksidekick copyright 2018 by John A. Oakey\nAll commercial rights are reserved.\n\n" \
               "Permission is given for free personal use and for distribution within a public\n" \
               "or non-profit educational institution or group.\n\n" \
               "tksidekick (c) is a project developed for www.wikipython.com by John A. Oakey and is\n" \
                "a non-commerical enterprise. Please send comments to: \noakey.john@yahoo.com\n\n" \
                "More information about tksidekick and a download url for GitHub may or may not\n" \
                "be available on www.wikipython.com"
    t1.delete(1.0, END)
    t1.insert(END, cpyrte_text)


# CREATING THE PROGRAM -

# Set up the radiobuttons - "rb"
for i in range(len(widgetlist)):
    newrb = rb(widgetlist[i], str(i+1))
rbvar.set("1")  # highlight the first button
rbconfigshort("Toplevel")
root.update()
methact()


#  and now the symphony begins
# _______________

root.mainloop()

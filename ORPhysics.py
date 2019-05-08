import Tkinter
import tkFileDialog
import os

root = Tkinter.Tk()
root.withdraw() #use to hide tkinter window

currdir = os.getcwd()
engineFile = ""
incFile = ""
includeDir = os.getcwd()
trainsetDir = os.getcwd()

trainsetDir = tkFileDialog.askdirectory(parent=root, initialdir=currdir, title='Please select your TrainSet directory')
print trainsetDir
targetLocodir = tkFileDialog.askdirectory(parent=root, initialdir=trainsetDir, title='Please select a Locomotive directory')
if len(targetLocodir) > 0:
    print "You chose %s" % targetLocodir
    engineFile = os.path.basename(tkFileDialog.askopenfilename())
    print "engine filename is: %s" % engineFile


includeDir = trainsetDir + "/Common.inc/Locomotives"
os.chdir(trainsetDir)
print os.getcwd()
print "choose .include file"
incFile = os.path.basename(tkFileDialog.askopenfilename())
print "include file is: %s" %incFile
   

os.mkdir(targetLocodir+"/OpenRails")
print "OpenRails dir created"
os.chdir(targetLocodir+"/OpenRails")
print "In OpenRails dir"
eng = open(engineFile, "w+")
eng.write(
	'include ("..\\')
eng.write(engineFile)
eng.write('" )\nEngine (\ninclude ( "..\\..\\Common.inc\\Locomotives\\')
eng.write(incFile)
eng.write('" )\n)')

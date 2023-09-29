#!/usr/bin/env python

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'

from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding
import serial
import psychopy.iohub as io
from psychopy.hardware import keyboard

try:
    ser = serial.Serial('COM5', 57600) #modify to COM4,5,6 depending on available port on device - dont forget to adapt the bits per sec !
    print("Connected to serial")
except:
    ser = False
    print("No serial port detected")
MRTrigger = 's' # the trigger from the scanner

def get_response():
    key_out=[]
    resp=event.getKeys()
    if resp:
        key=resp[0]
        if key=="escape":key_out=99
        elif key:
            key_out=key
        return key_out

def read_trigger():
    if ser!=False:
        incoming=''
        while ser.inWaiting():
            incoming = incoming + ser.read().decode()
        return(incoming)
        

# a loop for cleaning the serial port
while True:
    inputS = read_trigger()
    if not inputS:
        break
        
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.2'
expName = 'Ownership'  

expInfo = {
    'participant': "F0101",
    'Owner': ['yellow', 'blue'],
    'KeyA' : ['a', 'b'],
    'threshold' : round(float('50')),
}

# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion
Owner = expInfo['Owner']
KeyA = expInfo['KeyA']
threshold = expInfo['threshold']

if (threshold < 15 ) :
 threshold = float(15)
elif(threshold > 85) :
 threshold = float(85)
else : 
 threshold = threshold 


# Data file name stem = absolute path + name; later add .csv, 
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# ExperimentHandler for data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\lucie\\Documents\\Analyse-scripts\\PsychoPy\\OwnPPS\\Ownership.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
    
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code -

# --- Setup the Window ---
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=True,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False


# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
ioServer = io.launchHubServer(window=win, **ioConfig)

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

#---------------------------------------------Initialize all components----------------------------------------------------

# --- Initialize components for Routine "instructions" ---
text_norm = visual.TextStim(win=win, name='text_norm',
    text='',
    font='Arial',
    units='norm', pos=(0, -0.4), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_instruct = keyboard.Keyboard()
picload = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='picload')
text_norm_2 = visual.TextStim(win=win, name='text_norm_2',
    text='',
    font='Arial',
    units='norm', pos=(0, +0.55), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_norm_2.alignText= 'left'

image = visual.ImageStim(
    win=win,
    name='image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(+0.55, +0.20), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)


image.setImage('stim_'+str(Owner)+'.jpg')


# --- Initialize components for Routine "mask" ---
Mask_2 = visual.ImageStim(
    win=win,
    name='Mask_2', units='norm', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
    
Mask_2.setImage('mask.jpg')

# --- Initialize components for Routine "trial" ---

# Run 'Begin Experiment' code from imgSelec
import random
import pandas as pd
import csv
from ast import literal_eval


Stim = visual.ImageStim(
    win=win,
    name='Stim', units='norm', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "Response" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text='?',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "MidBreak" ---
text_norm = visual.TextStim(win=win, name='text_norm',
    text='',
    font='Arial',
    units='norm', pos=(0, -0.4), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_instruct = keyboard.Keyboard()
picload = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='picload')
text_norm_2 = visual.TextStim(win=win, name='text_norm_2',
    text='',
    font='Arial',
    units='norm', pos=(0, +0.44), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_norm_2.alignText= 'left'

text_norm_3 = visual.TextStim(win=win, name='text_norm_2',
    text='',
    font='Arial',
    units='norm', pos=(0, +0.85), height=0.12, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_norm_3.alignText= 'center'

image = visual.ImageStim(
    win=win,
    name='image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(+0.50, +0.22), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)


image.setImage('stim_'+str(Owner)+'.jpg')

# --- Initialize components for Routine "End" ---
TextEnd = visual.TextStim(win=win, name='TextEnd',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_instruct_3 = keyboard.Keyboard()

#------------------------------------------------------Prepare to start---------------------------------------------------------------
# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine - set info  ---
if (Owner == "blue" or Owner == "Blue" or Owner == "blue " or Owner == "Blue " or Owner == " blue" or Owner == " Blue"):
 Owner = 'blue'
 Other = 'yellow'
 Ownertxt = 'azul'
 Othertxt = 'amarelo'
 
if (Owner == "yellow" or Owner == "Yellow" or Owner == "yellow " or Owner == "Yellow " or Owner == " yellow" or Owner == " Yellow"):
 Owner = 'yellow'
 Other = 'blue'
 Ownertxt = 'amarelo'
 Othertxt = 'azul'

if (KeyA == "A" or KeyA =="a"):
 KeyB = "b"
 KeyA = "a"
 KeyBtxt = "dedo indicador "
 KeyAtxt = "dedo polegar"
 
elif (KeyA == "B" or KeyA =="b"):
 KeyB = "a"
 KeyA = "b"
 KeyBtxt = "dedo polegar"
 KeyAtxt = "dedo indicador "


thisExp.addData('KeyA', KeyA)
thisExp.addData('KeyB', KeyB)
thisExp.addData('Owner', Owner)
thisExp.addData('Other', Other)


# --- Prepare to start Routine "instructions" ---
continueRoutine = True
# update component parameters for each repeat
key_instruct.keys = []
key_instruct.rt = []
_key_instruct_allKeys = []
text_norm_3.setText('Instruções')
text_norm_2.setText('Por favor tenha em mente que o copo '+ str(Ownertxt) +' \npertence-lhe : \n \n e que o copo '+str(Othertxt) + ' pertence ao avatar.')
text_norm.setText('Se um " ? " aparece : \n     - Responder rapidamente com a sua ' + str(KeyAtxt) + ' se o copo estiver acessível \n     - Responder rapidamente com a sua ' + str(KeyBtxt) + ' se o copo não estiver acessível \n \n Ready?')

# keep track of which components have finished
instructionsComponents = [text_norm, key_instruct, picload, text_norm_2, text_norm_3, image]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

#---------------------------------------------------------------------Instructions---------------------------------------------------------
# --- Run Routine "instructions" ---
routineForceEnded = not continueRoutine


while continueRoutine and routineTimer.getTime() < 25:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # above manipulation draw back PsychoPy Runner window on focus. Bring back experiment window on focus
    win.winHandle.maximize()
    win.winHandle.set_fullscreen(True) 
    win.winHandle.activate()
    win.flip()
    
    
    # *text_norm_3* updates
    
    # if text_norm_3 is starting this frame...
    if text_norm_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_norm_3.frameNStart = frameN  # exact frame index
        text_norm_3.tStart = t  # local t and not account for scr refresh
        text_norm_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_norm_3, 'tStartRefresh')  # time at next scr refresh
        # update status
        text_norm_3.status = STARTED
        text_norm_3.setAutoDraw(True)
    
    # if text_norm is active this frame...
    if text_norm_3.status == STARTED:
        # update params
        pass
    
        # *text_norm* updates
    
    # if text_norm is starting this frame...
    if text_norm.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_norm.frameNStart = frameN  # exact frame index
        text_norm.tStart = t  # local t and not account for scr refresh
        text_norm.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_norm, 'tStartRefresh')  # time at next scr refresh
        # update status
        text_norm.status = STARTED
        text_norm.setAutoDraw(True)
    
    # if text_norm is active this frame...
    if text_norm.status == STARTED:
        # update params
        pass
    
    # *key_instruct* updates
    waitOnFlip = False
    
    # if key_instruct is starting this frame...
    if key_instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_instruct.frameNStart = frameN  # exact frame index
        key_instruct.tStart = t  # local t and not account for scr refresh
        key_instruct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_instruct, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_instruct.started')
        # update status
        key_instruct.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_instruct.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_instruct.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_instruct.status == STARTED and not waitOnFlip:
        theseKeys = key_instruct.getKeys(keyList=['space'], waitRelease=False)
        _key_instruct_allKeys.extend(theseKeys)
        if len(_key_instruct_allKeys):
            key_instruct.keys = _key_instruct_allKeys[0].name  # just the first key pressed
            key_instruct.rt = _key_instruct_allKeys[0].rt
            # a response ends the routine
            continueRoutine = True
    
    # if text_norm_2 is starting this frame...
    if text_norm_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_norm_2.frameNStart = frameN  # exact frame index
        text_norm_2.tStart = t  # local t and not account for scr refresh
        text_norm_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_norm_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_norm_2.started')
        # update status
        text_norm_2.status = STARTED
        text_norm_2.setAutoDraw(True)
        # Updating other components during *picload*
        TextEnd.setText('A experiência está terminada. Obrigado pela vossa participação ! \n\n')
    
    # if text_norm_2 is active this frame...
    if text_norm_2.status == STARTED:
        # update params
        pass
    
    # *image* updates
    
    # if image is starting this frame...
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image.started')
        # update status
        image.status = STARTED
        image.setAutoDraw(True)
    
    # if image is active this frame...
    if image.status == STARTED:
        # update params
        pass
    # *picload* period
    
    # if picload is starting this frame...
    if picload.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        picload.frameNStart = frameN  # exact frame index
        picload.tStart = t  # local t and not account for scr refresh
        picload.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(picload, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('picload.started', t)
        # update status
        picload.status = STARTED
        picload.start(1)
    elif picload.status == STARTED:  # one frame should pass before updating params and completing
        # Component updates done
        picload.complete()  # finish the static period
        picload.tStop = picload.tStart + 1  # record stop time
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions" ---
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#trigger scanner - remove if not working
while True:
    inputS = read_trigger()
    if inputS == MRTrigger:
        break
    resp = get_response()
    if resp:
        if resp=='s':
            break

#------------------------------------------------------------------------Prepare Loops---------------------------------------------

# set up handler to look after randomisation of conditions etc
LoopTask = data.TrialHandler(nReps=4.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='LoopTask')
thisExp.addLoop(LoopTask)  # add the loop to the experiment
thisLoopTask = LoopTask.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoopTask.rgb)
if thisLoopTask != None:
    for paramName in thisLoopTask:
        exec('{} = thisLoopTask[paramName]'.format(paramName))
win.flip()

for thisLoopTask in LoopTask:
    currentLoop = LoopTask
    # abbreviate parameter names if possible (e.g. rgb = thisLoopTask.rgb)
    if thisLoopTask != None:
        for paramName in thisLoopTask:
            exec('{} = thisLoopTask[paramName]'.format(paramName))
        
    # set up handler to look after randomisation of conditions etc
    Bloc_1 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions' + str(LoopTask.thisRepN) + '.csv'),
        seed=None, name='Bloc_1')
    thisExp.addLoop(Bloc_1)  # add the loop to the experiment
    thisBloc_1 = Bloc_1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBloc_1.rgb)
    if thisBloc_1 != None:
        for paramName in thisBloc_1:
            exec('{} = thisBloc_1[paramName]'.format(paramName))
    
    for thisBloc_1 in Bloc_1:
        currentLoop = Bloc_1
        # abbreviate parameter names if possible (e.g. rgb = thisBloc_1.rgb)
        if thisBloc_1 != None:
            for paramName in thisBloc_1:
                exec('{} = thisBloc_1[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "mask" ---
        continueRoutine = True
        
        # --- update component parameters for each repeat ---
        # Arrays for jitter : non-random as it was optimized with OptSeq
        
        jitter_0 = [2,2,2,6,6,2,4,2,2,12,4,2,2,4,2,6,2,4,2,10,4,2,8,4,10,2,4,4,4,2,4,2,2,2,2,10,4,2,2,4,2,4,4,2,2,6,2,2,4,2,2,6,2,6,4,4,4,4,2,2]
        jitter_1 = [2,2,2,2,8,2,4,6,2,2,2,12,2,4,4,6,2,4,2,2,4,2,2,10,4,2,2,6,4,6,2,2,2,6,2,2,8,2,2,2,2,6,4,4,2,6,2,10,2,2,6,4,4,2,4,2,4,4,6,2]
        jitter_2 = [2,2,2,4,4,6,8,4,2,2,4,2,10,2,4,2,6,4,2,8,2,2,4,2,4,4,4,2,2,4,4,2,10,2,4,2,4,2,2,6,2,2,2,6,2,2,4,4,2,4,6,12,4,2,4,6,2,2,4,2]
        jitter_3 = [2,2,2,2,6,4,6,2,2,6,6,2,2,2,12,2,2,4,2,8,2,2,8,2,2,6,2,4,2,2,4,6,2,2,6,6,4,2,2,2,6,2,10,2,2,4,2,6,2,2,2,4,6,2,8,4,2,8,2,2]
        selected_jitter = 'jitter_' + str(LoopTask.thisTrialN) + '[' + str(Bloc_1.thisTrialN) + ']'
        current_jitter = eval(selected_jitter) # extract one entry on each trial
        thisExp.addData('jitter', current_jitter) # record in the data for this trial
        # keep track of which components have finished
        maskComponents = [Mask_2]
        for thisComponent in maskComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "mask" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Mask_2* updates
            
            # if Mask_2 is starting this frame...
            if Mask_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Mask_2.frameNStart = frameN  # exact frame index
                Mask_2.tStart = t  # local t and not account for scr refresh
                Mask_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Mask_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Mask_2.started')
                # update status
                Mask_2.status = STARTED
                Mask_2.setAutoDraw(True)
            
            # if Mask_2 is active this frame...
            if Mask_2.status == STARTED:
                # update params
                pass
            
            # if Mask_2 is stopping this frame...
            if Mask_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Mask_2.tStartRefresh + current_jitter-frameTolerance:
                    # keep track of stop time/frame for later
                    Mask_2.tStop = t  # not accounting for scr refresh
                    Mask_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Mask_2.stopped')
                    # update status
                    Mask_2.status = FINISHED
                    Mask_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in maskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mask" ---
        for thisComponent in maskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "mask" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from imgSelec
        
        if (own == "S") :
            col = Owner[0]
        elif (own == "O") :
            col = Other[0]
        if (dist == 1 and space == "PPS") :
            pos = round((threshold/5)*0.5)*5
        elif (dist == 2 and space== "PPS"):
            pos = round((threshold/5)*0.6)*5
        elif (dist == 3 and space == "PPS"):
            pos = round((threshold/5)*0.7)*5
        elif (dist == 1 and space == "EPS"):
            pos = round((threshold/5)*1.5)*5
        elif (dist == 2 and space == "EPS"):
            pos = round((threshold/5)*1.6)*5
        elif (dist == 3 and space == "EPS"):
            pos = round((threshold/5)*1.7)*5
        elif (dist == 1 and space == "bound"):
            pos = round((threshold/5)*0.9)*5
        elif (dist == 2 and space == "bound"):
            pos = round((threshold/5)*1)*5
        elif (dist == 3 and space == "bound"): 
            pos = round((threshold/5)*1.1)*5
        
        pos = int(pos)
        name = "stim_" + str(pos) + "_" + col + "_u.jpg"
        
        thisExp.addData('pos', pos)
        thisExp.addData('space', space)
        thisExp.addData('col', col)
        thisExp.addData('name', name)
        
        trialtype = ""
        
        if (space == "bound" or resp == "y"):
            trialtype = "filler"
        else :
            trialtype = "test"
        
        thisExp.addData('trialtype', trialtype)
        
        Stim.setImage(name)
        # keep track of which components have finished
        trialComponents = [Stim]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Stim* updates
            
            # if Stim is starting this frame...
            if Stim.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Stim.frameNStart = frameN  # exact frame index
                Stim.tStart = t  # local t and not account for scr refresh
                Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stim.started')
                # update status
                Stim.status = STARTED
                Stim.setAutoDraw(True)
            
            # if Stim is active this frame...
            if Stim.status == STARTED:
                # update params
                pass
            
            # if Stim is stopping this frame...
            if Stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim.tStop = t  # not accounting for scr refresh
                    Stim.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Stim.stopped')
                    # update status
                    Stim.status = FINISHED
                    Stim.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.500000)
        
        # --- Prepare to start Routine "Response" ---
        continueRoutine = True
        # update component parameters for each repeat
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # Run 'Begin Routine' code from code_2
        if resp == 'n':
             continueRoutine = False
        # keep track of which components have finished
        ResponseComponents = [text_2, key_resp]
        for thisComponent in ResponseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Response" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.2:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['a','b','A','B'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = True
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ResponseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Response" ---
        for thisComponent in ResponseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        Bloc_1.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            Bloc_1.addData('key_resp.rt', key_resp.rt)
        # the Routine "Response" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'Bloc_1'
    
        # --- Prepare to start Routine "MidBreak" ---
    continueRoutine = True
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
        
    key_instruct.keys = []
        
    key_instruct.rt = []
    _key_instruct_allKeys = []
    text_norm_3.setText('Pausa')
    
    # keep track of which components have finished
    instructionsComponents = [text_norm, key_instruct, picload, text_norm_2, text_norm_3, image]
    for thisComponent in instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
        
    # --- Run Routine "Break" ---
    if (Midbreak == "y") :
        continueRoutine = True
    else :
        continueRoutine = False

    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 30:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_norm* updates
        
        # if text_norm is starting this frame...
        if text_norm.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_norm.frameNStart = frameN  # exact frame index
            text_norm.tStart = t  # local t and not account for scr refresh
            text_norm.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_norm, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_norm.status = STARTED
            text_norm.setAutoDraw(True)
        
        # if text_norm is active this frame...
        if text_norm.status == STARTED:
            # update params
            pass
        
        # *key_instruct* updates
        waitOnFlip = False
        
        # if key_instruct is starting this frame...
        if key_instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_instruct.frameNStart = frameN  # exact frame index
            key_instruct.tStart = t  # local t and not account for scr refresh
            key_instruct.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_instruct, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_instruct.started')
            # update status
            key_instruct.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_instruct.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_instruct.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_instruct.status == STARTED and not waitOnFlip:
            theseKeys = key_instruct.getKeys(keyList=['space'], waitRelease=False)
            _key_instruct_allKeys.extend(theseKeys)
            if len(_key_instruct_allKeys):
                key_instruct.keys = _key_instruct_allKeys[0].name  # just the first key pressed
                key_instruct.rt = _key_instruct_allKeys[0].rt
                # a response ends the routine
                continueRoutine = True
        
        # if text_norm_2 is starting this frame...
        if text_norm_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_norm_2.frameNStart = frameN  # exact frame index
            text_norm_2.tStart = t  # local t and not account for scr refresh
            text_norm_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_norm_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_norm_2.started')
            # update status
            text_norm_2.status = STARTED
            text_norm_2.setAutoDraw(True)
        
        # if text_norm_2 is active this frame...
        if text_norm_2.status == STARTED:
            # update params
            pass

        # if text_norm_3 is starting this frame...
        if text_norm_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_norm_3.frameNStart = frameN  # exact frame index
            text_norm_3.tStart = t  # local t and not account for scr refresh
            text_norm_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_norm_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_norm_2.started')
            # update status
            text_norm_3.status = STARTED
            text_norm_3.setAutoDraw(True)
        
        # if text_norm_3 is active this frame...
        if text_norm_3.status == STARTED:
            # update params
            pass
        
        # *image* updates
        
        # if image is starting this frame...
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image.started')
            # update status
            image.status = STARTED
            image.setAutoDraw(True)
        
        # if image is active this frame...
        if image.status == STARTED:
            # update params
            pass
        # *picload* period
        
        # if picload is starting this frame...
        if picload.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            picload.frameNStart = frameN  # exact frame index
            picload.tStart = t  # local t and not account for scr refresh
            picload.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(picload, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('picload.started', t)
            # update status
            picload.status = STARTED
            picload.start(1)
        elif picload.status == STARTED:  # one frame should pass before updating params and completing
            # Component updates done
            picload.complete()  # finish the static period
            picload.tStop = picload.tStart + 1  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions" ---
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
    
    # --- Ending Routine "Response" ---
    
 
thisExp.nextEntry()
# completed 4.0 repeats of 'LoopTask'


# --- Prepare to start Routine "End" ---
continueRoutine = True
# update component parameters for each repeat
key_instruct_3.keys = []
key_instruct_3.rt = []
_key_instruct_3_allKeys = []
# keep track of which components have finished
EndComponents = [TextEnd, key_instruct_3]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "End" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TextEnd* updates
    
    # if TextEnd is starting this frame...
    if TextEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TextEnd.frameNStart = frameN  # exact frame index
        TextEnd.tStart = t  # local t and not account for scr refresh
        TextEnd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TextEnd, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'TextEnd.started')
        # update status
        TextEnd.status = STARTED
        TextEnd.setAutoDraw(True)
    
    # if TextEnd is active this frame...
    if TextEnd.status == STARTED:
        # update params
        pass
    
    # *key_instruct_3* updates
    waitOnFlip = False
    
    # if key_instruct_3 is starting this frame...
    if key_instruct_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_instruct_3.frameNStart = frameN  # exact frame index
        key_instruct_3.tStart = t  # local t and not account for scr refresh
        key_instruct_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_instruct_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_instruct_3.started')
        # update status
        key_instruct_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_instruct_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_instruct_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_instruct_3.status == STARTED and not waitOnFlip:
        theseKeys = key_instruct_3.getKeys(keyList=['space'], waitRelease=False)
        _key_instruct_3_allKeys.extend(theseKeys)
        if len(_key_instruct_3_allKeys):
            key_instruct_3.keys = _key_instruct_3_allKeys[0].name  # just the first key pressed
            key_instruct_3.rt = _key_instruct_3_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "End" ---
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_instruct_3.keys in ['', [], None]:  # No response was made
    key_instruct_3.keys = None
thisExp.addData('key_instruct_3.keys',key_instruct_3.keys)
if key_instruct_3.keys != None:  # we had a response
    thisExp.addData('key_instruct_3.rt', key_instruct_3.rt)
thisExp.nextEntry()
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down

thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

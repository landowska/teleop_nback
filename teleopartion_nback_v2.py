#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.2),
    on May 23, 2023, at 12:17
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'pygame'
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

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.2'
expName = 'n-back teleoperation'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\NIRS-PC\\Desktop\\teleoperation_experiment_v1\\teleopartion_nback_v2.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1366, 768], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = True
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
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "welcome" ---
text_welcome = visual.TextStim(win=win, name='text_welcome',
    text='Press S to stat experiment',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_start = keyboard.Keyboard()

# --- Initialize components for Routine "block_break" ---
przerwa = visual.TextStim(win=win, name='przerwa',
    text='Baseline',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "inst_one" ---
inst1 = sound.Sound('sounds/oneback.wav', secs=1.0, stereo=True, hamming=True,
    name='inst1')
inst1.setVolume(1.0)

# --- Initialize components for Routine "trial" ---
sound_stim1 = sound.Sound('A', secs=1, stereo=True, hamming=True,
    name='sound_stim1')
sound_stim1.setVolume(1.0)

# --- Initialize components for Routine "rest" ---
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "block_break" ---
przerwa = visual.TextStim(win=win, name='przerwa',
    text='Baseline',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "inst_three" ---
inst_3 = sound.Sound('sounds/threeback.wav', secs=1.0, stereo=True, hamming=True,
    name='inst_3')
inst_3.setVolume(1.0)

# --- Initialize components for Routine "trial" ---
sound_stim1 = sound.Sound('A', secs=1, stereo=True, hamming=True,
    name='sound_stim1')
sound_stim1.setVolume(1.0)

# --- Initialize components for Routine "rest" ---
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "bye" ---
text = visual.TextStim(win=win, name='text',
    text='Finished',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "welcome" ---
continueRoutine = True
# update component parameters for each repeat
key_start.keys = []
key_start.rt = []
_key_start_allKeys = []
# keep track of which components have finished
welcomeComponents = [text_welcome, key_start]
for thisComponent in welcomeComponents:
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

# --- Run Routine "welcome" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_welcome* updates
    
    # if text_welcome is starting this frame...
    if text_welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_welcome.frameNStart = frameN  # exact frame index
        text_welcome.tStart = t  # local t and not account for scr refresh
        text_welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_welcome, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_welcome.started')
        # update status
        text_welcome.status = STARTED
        text_welcome.setAutoDraw(True)
    
    # if text_welcome is active this frame...
    if text_welcome.status == STARTED:
        # update params
        pass
    
    # *key_start* updates
    waitOnFlip = False
    
    # if key_start is starting this frame...
    if key_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_start.frameNStart = frameN  # exact frame index
        key_start.tStart = t  # local t and not account for scr refresh
        key_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_start, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_start.started')
        # update status
        key_start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_start.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_start.status == STARTED and not waitOnFlip:
        theseKeys = key_start.getKeys(keyList=['s'], waitRelease=False)
        _key_start_allKeys.extend(theseKeys)
        if len(_key_start_allKeys):
            key_start.keys = _key_start_allKeys[-1].name  # just the last key pressed
            key_start.rt = _key_start_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "welcome" ---
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_start.keys in ['', [], None]:  # No response was made
    key_start.keys = None
thisExp.addData('key_start.keys',key_start.keys)
if key_start.keys != None:  # we had a response
    thisExp.addData('key_start.rt', key_start.rt)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx'),
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "block_break" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    block_breakComponents = [przerwa]
    for thisComponent in block_breakComponents:
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
    
    # --- Run Routine "block_break" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 20.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *przerwa* updates
        
        # if przerwa is starting this frame...
        if przerwa.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            przerwa.frameNStart = frameN  # exact frame index
            przerwa.tStart = t  # local t and not account for scr refresh
            przerwa.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(przerwa, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'przerwa.started')
            # update status
            przerwa.status = STARTED
            przerwa.setAutoDraw(True)
        
        # if przerwa is active this frame...
        if przerwa.status == STARTED:
            # update params
            pass
        
        # if przerwa is stopping this frame...
        if przerwa.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > przerwa.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                przerwa.tStop = t  # not accounting for scr refresh
                przerwa.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'przerwa.stopped')
                # update status
                przerwa.status = FINISHED
                przerwa.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block_breakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "block_break" ---
    for thisComponent in block_breakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-20.000000)
    
    # set up handler to look after randomisation of conditions etc
    meta_oneback = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='meta_oneback')
    thisExp.addLoop(meta_oneback)  # add the loop to the experiment
    thisMeta_oneback = meta_oneback.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMeta_oneback.rgb)
    if thisMeta_oneback != None:
        for paramName in thisMeta_oneback:
            exec('{} = thisMeta_oneback[paramName]'.format(paramName))
    
    for thisMeta_oneback in meta_oneback:
        currentLoop = meta_oneback
        # abbreviate parameter names if possible (e.g. rgb = thisMeta_oneback.rgb)
        if thisMeta_oneback != None:
            for paramName in thisMeta_oneback:
                exec('{} = thisMeta_oneback[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "inst_one" ---
        continueRoutine = True
        # update component parameters for each repeat
        inst1.setSound('sounds/oneback.wav', secs=1.0, hamming=True)
        inst1.setVolume(1.0, log=False)
        # keep track of which components have finished
        inst_oneComponents = [inst1]
        for thisComponent in inst_oneComponents:
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
        
        # --- Run Routine "inst_one" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # if inst1 is starting this frame...
            if inst1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inst1.frameNStart = frameN  # exact frame index
                inst1.tStart = t  # local t and not account for scr refresh
                inst1.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('inst1.started', tThisFlipGlobal)
                # update status
                inst1.status = STARTED
                inst1.play(when=win)  # sync with win flip
            
            # if inst1 is stopping this frame...
            if inst1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > inst1.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    inst1.tStop = t  # not accounting for scr refresh
                    inst1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'inst1.stopped')
                    # update status
                    inst1.status = FINISHED
                    inst1.stop()
            # update inst1 status according to whether it's playing
            if inst1.isPlaying:
                inst1.status = STARTED
            elif inst1.isFinished:
                inst1.status = FINISHED
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in inst_oneComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "inst_one" ---
        for thisComponent in inst_oneComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        inst1.stop()  # ensure sound has stopped at end of routine
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # set up handler to look after randomisation of conditions etc
        one_back = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('teleoperation_oneback.xlsx'),
            seed=None, name='one_back')
        thisExp.addLoop(one_back)  # add the loop to the experiment
        thisOne_back = one_back.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisOne_back.rgb)
        if thisOne_back != None:
            for paramName in thisOne_back:
                exec('{} = thisOne_back[paramName]'.format(paramName))
        
        for thisOne_back in one_back:
            currentLoop = one_back
            # abbreviate parameter names if possible (e.g. rgb = thisOne_back.rgb)
            if thisOne_back != None:
                for paramName in thisOne_back:
                    exec('{} = thisOne_back[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "trial" ---
            continueRoutine = True
            # update component parameters for each repeat
            sound_stim1.setSound(number_audio_sound, secs=1, hamming=True)
            sound_stim1.setVolume(1.0, log=False)
            # keep track of which components have finished
            trialComponents = [sound_stim1]
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
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # if sound_stim1 is starting this frame...
                if sound_stim1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    sound_stim1.frameNStart = frameN  # exact frame index
                    sound_stim1.tStart = t  # local t and not account for scr refresh
                    sound_stim1.tStartRefresh = tThisFlipGlobal  # on global time
                    # add timestamp to datafile
                    thisExp.addData('sound_stim1.started', tThisFlipGlobal)
                    # update status
                    sound_stim1.status = STARTED
                    sound_stim1.play(when=win)  # sync with win flip
                
                # if sound_stim1 is stopping this frame...
                if sound_stim1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > sound_stim1.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        sound_stim1.tStop = t  # not accounting for scr refresh
                        sound_stim1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'sound_stim1.stopped')
                        # update status
                        sound_stim1.status = FINISHED
                        sound_stim1.stop()
                # update sound_stim1 status according to whether it's playing
                if sound_stim1.isPlaying:
                    sound_stim1.status = STARTED
                elif sound_stim1.isFinished:
                    sound_stim1.status = FINISHED
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                    if eyetracker:
                        eyetracker.setConnectionState(False)
                
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
            sound_stim1.stop()  # ensure sound has stopped at end of routine
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            
            # --- Prepare to start Routine "rest" ---
            continueRoutine = True
            # update component parameters for each repeat
            # keep track of which components have finished
            restComponents = [fixation]
            for thisComponent in restComponents:
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
            
            # --- Run Routine "rest" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation* updates
                
                # if fixation is starting this frame...
                if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation.frameNStart = frameN  # exact frame index
                    fixation.tStart = t  # local t and not account for scr refresh
                    fixation.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation.started')
                    # update status
                    fixation.status = STARTED
                    fixation.setAutoDraw(True)
                
                # if fixation is active this frame...
                if fixation.status == STARTED:
                    # update params
                    pass
                
                # if fixation is stopping this frame...
                if fixation.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation.tStop = t  # not accounting for scr refresh
                        fixation.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation.stopped')
                        # update status
                        fixation.status = FINISHED
                        fixation.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                    if eyetracker:
                        eyetracker.setConnectionState(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in restComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "rest" ---
            for thisComponent in restComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'one_back'
        
        # get names of stimulus parameters
        if one_back.trialList in ([], [None], None):
            params = []
        else:
            params = one_back.trialList[0].keys()
        # save data for this loop
        one_back.saveAsExcel(filename + '.xlsx', sheetName='one_back',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        one_back.saveAsText(filename + 'one_back.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'meta_oneback'
    
    # get names of stimulus parameters
    if meta_oneback.trialList in ([], [None], None):
        params = []
    else:
        params = meta_oneback.trialList[0].keys()
    # save data for this loop
    meta_oneback.saveAsExcel(filename + '.xlsx', sheetName='meta_oneback',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    meta_oneback.saveAsText(filename + 'meta_oneback.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "block_break" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    block_breakComponents = [przerwa]
    for thisComponent in block_breakComponents:
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
    
    # --- Run Routine "block_break" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 20.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *przerwa* updates
        
        # if przerwa is starting this frame...
        if przerwa.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            przerwa.frameNStart = frameN  # exact frame index
            przerwa.tStart = t  # local t and not account for scr refresh
            przerwa.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(przerwa, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'przerwa.started')
            # update status
            przerwa.status = STARTED
            przerwa.setAutoDraw(True)
        
        # if przerwa is active this frame...
        if przerwa.status == STARTED:
            # update params
            pass
        
        # if przerwa is stopping this frame...
        if przerwa.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > przerwa.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                przerwa.tStop = t  # not accounting for scr refresh
                przerwa.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'przerwa.stopped')
                # update status
                przerwa.status = FINISHED
                przerwa.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block_breakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "block_break" ---
    for thisComponent in block_breakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-20.000000)
    
    # set up handler to look after randomisation of conditions etc
    meta_threeback = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='meta_threeback')
    thisExp.addLoop(meta_threeback)  # add the loop to the experiment
    thisMeta_threeback = meta_threeback.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMeta_threeback.rgb)
    if thisMeta_threeback != None:
        for paramName in thisMeta_threeback:
            exec('{} = thisMeta_threeback[paramName]'.format(paramName))
    
    for thisMeta_threeback in meta_threeback:
        currentLoop = meta_threeback
        # abbreviate parameter names if possible (e.g. rgb = thisMeta_threeback.rgb)
        if thisMeta_threeback != None:
            for paramName in thisMeta_threeback:
                exec('{} = thisMeta_threeback[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "inst_three" ---
        continueRoutine = True
        # update component parameters for each repeat
        inst_3.setSound('sounds/threeback.wav', secs=1.0, hamming=True)
        inst_3.setVolume(1.0, log=False)
        # keep track of which components have finished
        inst_threeComponents = [inst_3]
        for thisComponent in inst_threeComponents:
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
        
        # --- Run Routine "inst_three" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # if inst_3 is starting this frame...
            if inst_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inst_3.frameNStart = frameN  # exact frame index
                inst_3.tStart = t  # local t and not account for scr refresh
                inst_3.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('inst_3.started', tThisFlipGlobal)
                # update status
                inst_3.status = STARTED
                inst_3.play(when=win)  # sync with win flip
            
            # if inst_3 is stopping this frame...
            if inst_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > inst_3.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    inst_3.tStop = t  # not accounting for scr refresh
                    inst_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'inst_3.stopped')
                    # update status
                    inst_3.status = FINISHED
                    inst_3.stop()
            # update inst_3 status according to whether it's playing
            if inst_3.isPlaying:
                inst_3.status = STARTED
            elif inst_3.isFinished:
                inst_3.status = FINISHED
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in inst_threeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "inst_three" ---
        for thisComponent in inst_threeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        inst_3.stop()  # ensure sound has stopped at end of routine
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # set up handler to look after randomisation of conditions etc
        three_back = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('teleoperation_threeback .xlsx'),
            seed=None, name='three_back')
        thisExp.addLoop(three_back)  # add the loop to the experiment
        thisThree_back = three_back.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisThree_back.rgb)
        if thisThree_back != None:
            for paramName in thisThree_back:
                exec('{} = thisThree_back[paramName]'.format(paramName))
        
        for thisThree_back in three_back:
            currentLoop = three_back
            # abbreviate parameter names if possible (e.g. rgb = thisThree_back.rgb)
            if thisThree_back != None:
                for paramName in thisThree_back:
                    exec('{} = thisThree_back[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "trial" ---
            continueRoutine = True
            # update component parameters for each repeat
            sound_stim1.setSound(number_audio_sound, secs=1, hamming=True)
            sound_stim1.setVolume(1.0, log=False)
            # keep track of which components have finished
            trialComponents = [sound_stim1]
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
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # if sound_stim1 is starting this frame...
                if sound_stim1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    sound_stim1.frameNStart = frameN  # exact frame index
                    sound_stim1.tStart = t  # local t and not account for scr refresh
                    sound_stim1.tStartRefresh = tThisFlipGlobal  # on global time
                    # add timestamp to datafile
                    thisExp.addData('sound_stim1.started', tThisFlipGlobal)
                    # update status
                    sound_stim1.status = STARTED
                    sound_stim1.play(when=win)  # sync with win flip
                
                # if sound_stim1 is stopping this frame...
                if sound_stim1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > sound_stim1.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        sound_stim1.tStop = t  # not accounting for scr refresh
                        sound_stim1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'sound_stim1.stopped')
                        # update status
                        sound_stim1.status = FINISHED
                        sound_stim1.stop()
                # update sound_stim1 status according to whether it's playing
                if sound_stim1.isPlaying:
                    sound_stim1.status = STARTED
                elif sound_stim1.isFinished:
                    sound_stim1.status = FINISHED
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                    if eyetracker:
                        eyetracker.setConnectionState(False)
                
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
            sound_stim1.stop()  # ensure sound has stopped at end of routine
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            
            # --- Prepare to start Routine "rest" ---
            continueRoutine = True
            # update component parameters for each repeat
            # keep track of which components have finished
            restComponents = [fixation]
            for thisComponent in restComponents:
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
            
            # --- Run Routine "rest" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation* updates
                
                # if fixation is starting this frame...
                if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation.frameNStart = frameN  # exact frame index
                    fixation.tStart = t  # local t and not account for scr refresh
                    fixation.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation.started')
                    # update status
                    fixation.status = STARTED
                    fixation.setAutoDraw(True)
                
                # if fixation is active this frame...
                if fixation.status == STARTED:
                    # update params
                    pass
                
                # if fixation is stopping this frame...
                if fixation.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation.tStop = t  # not accounting for scr refresh
                        fixation.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation.stopped')
                        # update status
                        fixation.status = FINISHED
                        fixation.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                    if eyetracker:
                        eyetracker.setConnectionState(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in restComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "rest" ---
            for thisComponent in restComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'three_back'
        
        # get names of stimulus parameters
        if three_back.trialList in ([], [None], None):
            params = []
        else:
            params = three_back.trialList[0].keys()
        # save data for this loop
        three_back.saveAsExcel(filename + '.xlsx', sheetName='three_back',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        three_back.saveAsText(filename + 'three_back.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'meta_threeback'
    
    # get names of stimulus parameters
    if meta_threeback.trialList in ([], [None], None):
        params = []
    else:
        params = meta_threeback.trialList[0].keys()
    # save data for this loop
    meta_threeback.saveAsExcel(filename + '.xlsx', sheetName='meta_threeback',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    meta_threeback.saveAsText(filename + 'meta_threeback.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
# completed 3.0 repeats of 'blocks'


# --- Prepare to start Routine "bye" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
byeComponents = [text]
for thisComponent in byeComponents:
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

# --- Run Routine "bye" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 2.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    
    # if text is starting this frame...
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        # update status
        text.status = STARTED
        text.setAutoDraw(True)
    
    # if text is active this frame...
    if text.status == STARTED:
        # update params
        pass
    
    # if text is stopping this frame...
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.stopped')
            # update status
            text.status = FINISHED
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in byeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "bye" ---
for thisComponent in byeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-2.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

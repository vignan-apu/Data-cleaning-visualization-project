#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.1.1),
    on November 20, 2025, at 17:23
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
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2025.1.1'
expName = 'Final sub'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1536, 864]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\anupm\\Desktop\\New stroop task\\Psycohpy\\Final sub_lastrun.py',
        savePickle=True, saveWideText=False,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('', )
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    if deviceManager.getDevice('Space1') is None:
        # initialise Space1
        Space1 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Space1',
        )
    if deviceManager.getDevice('Spaec2') is None:
        # initialise Spaec2
        Spaec2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Spaec2',
        )
    if deviceManager.getDevice('key_resp_practice') is None:
        # initialise key_resp_practice
        key_resp_practice = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_practice',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('key_resp_NoTimer') is None:
        # initialise key_resp_NoTimer
        key_resp_NoTimer = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_NoTimer',
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
        )
    if deviceManager.getDevice('key_resp_timer') is None:
        # initialise key_resp_timer
        key_resp_timer = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_timer',
        )
    if deviceManager.getDevice('Thanks') is None:
        # initialise Thanks
        Thanks = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Thanks',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Welcome" ---
    Welcome__text = visual.TextStim(win=win, name='Welcome__text',
        text='Welcome to the Stroop Task Study!\n\nYou will be completing a short attention task.\n\nPress SPACE to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Space1 = keyboard.Keyboard(deviceName='Space1')
    
    # --- Initialize components for Routine "Instruction" ---
    Instruction_text = visual.TextStim(win=win, name='Instruction_text',
        text='You will see the names of colours on the screen, one at a time.\n\nYour task is to press the key that matches the INK COLOUR of the word,\nnot the word meaning.\n\nFor example, if the word BLUE is written in red colour,\nthe correct answer is RED.\n\nKey responses:\nR = Red\nG = Green\nB = Blue\nY = Yellow\n\nPress SPACE to start a short practice round.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Spaec2 = keyboard.Keyboard(deviceName='Spaec2')
    
    # --- Initialize components for Routine "Preactice" ---
    Word_ = visual.TextStim(win=win, name='Word_',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_practice = keyboard.Keyboard(deviceName='key_resp_practice')
    
    # --- Initialize components for Routine "Feedback" ---
    Feedback_text = visual.TextStim(win=win, name='Feedback_text',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "instruction_beforemain" ---
    text = visual.TextStim(win=win, name='text',
        text='Practice session complete!\n\n\n\nThere are two tasks in this study :\n- \nTask 1: Without Timer \n.\nTask 2: With timer\n\n\n\nPress SPACE to start Task 1.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "Main_NoTimer" ---
    Word_NoTimer = visual.TextStim(win=win, name='Word_NoTimer',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_NoTimer = keyboard.Keyboard(deviceName='key_resp_NoTimer')
    
    # --- Initialize components for Routine "Task2" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text='Task 1 complete!\n\n\n\nNext is Task 2,  You have 15 sec to complete this task.\n\n\n\nPress SPACE to start Task 2.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    
    # --- Initialize components for Routine "Main_Timer" ---
    # Run 'Begin Experiment' code from TimerCode
    from psychopy import core
    
    
    TimerText = visual.TextStim(win=win, name='TimerText',
        text=None,
        font='Arial',
        pos=(0.3, 0.2), draggable=False, height=0.08, wrapWidth=None, ori=0.0, 
        color=[0.3961, -0.7333, -0.7333], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_timer = keyboard.Keyboard(deviceName='key_resp_timer')
    word_timer = visual.TextStim(win=win, name='word_timer',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "Thanks_Screen_" ---
    Thanks = keyboard.Keyboard(deviceName='Thanks')
    text_3 = visual.TextStim(win=win, name='text_3',
        text='You have completed the study.\n\n\n\nThank you for your time and participation!\n\nYour responses have been recorded.\n\n\n\nYou may press SPACE close the Study.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Welcome" ---
    # create an object to store info about Routine Welcome
    Welcome = data.Routine(
        name='Welcome',
        components=[Welcome__text, Space1],
    )
    Welcome.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Space1
    Space1.keys = []
    Space1.rt = []
    _Space1_allKeys = []
    # store start times for Welcome
    Welcome.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Welcome.tStart = globalClock.getTime(format='float')
    Welcome.status = STARTED
    thisExp.addData('Welcome.started', Welcome.tStart)
    Welcome.maxDuration = None
    # keep track of which components have finished
    WelcomeComponents = Welcome.components
    for thisComponent in Welcome.components:
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
    
    # --- Run Routine "Welcome" ---
    Welcome.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Welcome__text* updates
        
        # if Welcome__text is starting this frame...
        if Welcome__text.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Welcome__text.frameNStart = frameN  # exact frame index
            Welcome__text.tStart = t  # local t and not account for scr refresh
            Welcome__text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Welcome__text, 'tStartRefresh')  # time at next scr refresh
            # update status
            Welcome__text.status = STARTED
            Welcome__text.setAutoDraw(True)
        
        # if Welcome__text is active this frame...
        if Welcome__text.status == STARTED:
            # update params
            pass
        
        # *Space1* updates
        
        # if Space1 is starting this frame...
        if Space1.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Space1.frameNStart = frameN  # exact frame index
            Space1.tStart = t  # local t and not account for scr refresh
            Space1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Space1, 'tStartRefresh')  # time at next scr refresh
            # update status
            Space1.status = STARTED
            # keyboard checking is just starting
            Space1.clock.reset()  # now t=0
        if Space1.status == STARTED:
            theseKeys = Space1.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _Space1_allKeys.extend(theseKeys)
            if len(_Space1_allKeys):
                Space1.keys = _Space1_allKeys[-1].name  # just the last key pressed
                Space1.rt = _Space1_allKeys[-1].rt
                Space1.duration = _Space1_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=Welcome,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Welcome.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Welcome.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Welcome" ---
    for thisComponent in Welcome.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Welcome
    Welcome.tStop = globalClock.getTime(format='float')
    Welcome.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Welcome.stopped', Welcome.tStop)
    thisExp.nextEntry()
    # the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instruction" ---
    # create an object to store info about Routine Instruction
    Instruction = data.Routine(
        name='Instruction',
        components=[Instruction_text, Spaec2],
    )
    Instruction.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Spaec2
    Spaec2.keys = []
    Spaec2.rt = []
    _Spaec2_allKeys = []
    # store start times for Instruction
    Instruction.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instruction.tStart = globalClock.getTime(format='float')
    Instruction.status = STARTED
    thisExp.addData('Instruction.started', Instruction.tStart)
    Instruction.maxDuration = None
    # keep track of which components have finished
    InstructionComponents = Instruction.components
    for thisComponent in Instruction.components:
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
    
    # --- Run Routine "Instruction" ---
    Instruction.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instruction_text* updates
        
        # if Instruction_text is starting this frame...
        if Instruction_text.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instruction_text.frameNStart = frameN  # exact frame index
            Instruction_text.tStart = t  # local t and not account for scr refresh
            Instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instruction_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            Instruction_text.status = STARTED
            Instruction_text.setAutoDraw(True)
        
        # if Instruction_text is active this frame...
        if Instruction_text.status == STARTED:
            # update params
            pass
        
        # *Spaec2* updates
        
        # if Spaec2 is starting this frame...
        if Spaec2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Spaec2.frameNStart = frameN  # exact frame index
            Spaec2.tStart = t  # local t and not account for scr refresh
            Spaec2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Spaec2, 'tStartRefresh')  # time at next scr refresh
            # update status
            Spaec2.status = STARTED
            # keyboard checking is just starting
            Spaec2.clock.reset()  # now t=0
        if Spaec2.status == STARTED:
            theseKeys = Spaec2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _Spaec2_allKeys.extend(theseKeys)
            if len(_Spaec2_allKeys):
                Spaec2.keys = _Spaec2_allKeys[-1].name  # just the last key pressed
                Spaec2.rt = _Spaec2_allKeys[-1].rt
                Spaec2.duration = _Spaec2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=Instruction,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instruction.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instruction.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instruction" ---
    for thisComponent in Instruction.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instruction
    Instruction.tStop = globalClock.getTime(format='float')
    Instruction.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instruction.stopped', Instruction.tStop)
    thisExp.nextEntry()
    # the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practice_loop = data.TrialHandler2(
        name='practice_loop',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('C:/Users/anupm/Desktop/New stroop task/Practice.csv'), 
        seed=None, 
    )
    thisExp.addLoop(practice_loop)  # add the loop to the experiment
    thisPractice_loop = practice_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
    if thisPractice_loop != None:
        for paramName in thisPractice_loop:
            globals()[paramName] = thisPractice_loop[paramName]
    
    for thisPractice_loop in practice_loop:
        practice_loop.status = STARTED
        if hasattr(thisPractice_loop, 'status'):
            thisPractice_loop.status = STARTED
        currentLoop = practice_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
        if thisPractice_loop != None:
            for paramName in thisPractice_loop:
                globals()[paramName] = thisPractice_loop[paramName]
        
        # --- Prepare to start Routine "Preactice" ---
        # create an object to store info about Routine Preactice
        Preactice = data.Routine(
            name='Preactice',
            components=[Word_, key_resp_practice],
        )
        Preactice.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        Word_.setColor(Colour, colorSpace='rgb')
        Word_.setText(Word)
        # create starting attributes for key_resp_practice
        key_resp_practice.keys = []
        key_resp_practice.rt = []
        _key_resp_practice_allKeys = []
        # Run 'Begin Routine' code from code_2
        Word_.colorSpace = 'named'
        Word_.color = Colour
        Word_.text = Word
        # store start times for Preactice
        Preactice.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Preactice.tStart = globalClock.getTime(format='float')
        Preactice.status = STARTED
        thisExp.addData('Preactice.started', Preactice.tStart)
        Preactice.maxDuration = None
        # keep track of which components have finished
        PreacticeComponents = Preactice.components
        for thisComponent in Preactice.components:
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
        
        # --- Run Routine "Preactice" ---
        Preactice.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisPractice_loop, 'status') and thisPractice_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Word_* updates
            
            # if Word_ is starting this frame...
            if Word_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Word_.frameNStart = frameN  # exact frame index
                Word_.tStart = t  # local t and not account for scr refresh
                Word_.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Word_, 'tStartRefresh')  # time at next scr refresh
                # update status
                Word_.status = STARTED
                Word_.setAutoDraw(True)
            
            # if Word_ is active this frame...
            if Word_.status == STARTED:
                # update params
                pass
            
            # *key_resp_practice* updates
            
            # if key_resp_practice is starting this frame...
            if key_resp_practice.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_practice.frameNStart = frameN  # exact frame index
                key_resp_practice.tStart = t  # local t and not account for scr refresh
                key_resp_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_practice, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp_practice.status = STARTED
                # keyboard checking is just starting
                key_resp_practice.clock.reset()  # now t=0
            if key_resp_practice.status == STARTED:
                theseKeys = key_resp_practice.getKeys(keyList=['r','g','y','b'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_practice_allKeys.extend(theseKeys)
                if len(_key_resp_practice_allKeys):
                    key_resp_practice.keys = _key_resp_practice_allKeys[-1].name  # just the last key pressed
                    key_resp_practice.rt = _key_resp_practice_allKeys[-1].rt
                    key_resp_practice.duration = _key_resp_practice_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_practice.keys == str(Correctans)) or (key_resp_practice.keys == Correctans):
                        key_resp_practice.corr = 1
                    else:
                        key_resp_practice.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=Preactice,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Preactice.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Preactice.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Preactice" ---
        for thisComponent in Preactice.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Preactice
        Preactice.tStop = globalClock.getTime(format='float')
        Preactice.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Preactice.stopped', Preactice.tStop)
        # check responses
        if key_resp_practice.keys in ['', [], None]:  # No response was made
            key_resp_practice.keys = None
            # was no response the correct answer?!
            if str(Correctans).lower() == 'none':
               key_resp_practice.corr = 1;  # correct non-response
            else:
               key_resp_practice.corr = 0;  # failed to respond (incorrectly)
        # store data for practice_loop (TrialHandler)
        practice_loop.addData('key_resp_practice.keys',key_resp_practice.keys)
        practice_loop.addData('key_resp_practice.corr', key_resp_practice.corr)
        if key_resp_practice.keys != None:  # we had a response
            practice_loop.addData('key_resp_practice.rt', key_resp_practice.rt)
            practice_loop.addData('key_resp_practice.duration', key_resp_practice.duration)
        # Run 'End Routine' code from code_2
        if key_resp_practice.corr:
            Feedback_text.text = 'Correct!'
        else:
            Feedback_text.text = 'Incorrect'
        
        thisExp.addData('trialWord', Word)
        thisExp.addData('trialColor', Colour)
        thisExp.addData('trialCondition', Condition)
        thisExp.addData('correctAnswer', Correctans)
        thisExp.addData('response', key_resp_practice.keys)
        thisExp.addData('correct', key_resp_practice.corr)
        thisExp.addData('rt', key_resp_practice.rt)
        
        # the Routine "Preactice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Feedback" ---
        # create an object to store info about Routine Feedback
        Feedback = data.Routine(
            name='Feedback',
            components=[Feedback_text],
        )
        Feedback.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for Feedback
        Feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Feedback.tStart = globalClock.getTime(format='float')
        Feedback.status = STARTED
        thisExp.addData('Feedback.started', Feedback.tStart)
        Feedback.maxDuration = None
        # keep track of which components have finished
        FeedbackComponents = Feedback.components
        for thisComponent in Feedback.components:
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
        
        # --- Run Routine "Feedback" ---
        Feedback.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # if trial has changed, end Routine now
            if hasattr(thisPractice_loop, 'status') and thisPractice_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Feedback_text* updates
            
            # if Feedback_text is starting this frame...
            if Feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Feedback_text.frameNStart = frameN  # exact frame index
                Feedback_text.tStart = t  # local t and not account for scr refresh
                Feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Feedback_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                Feedback_text.status = STARTED
                Feedback_text.setAutoDraw(True)
            
            # if Feedback_text is active this frame...
            if Feedback_text.status == STARTED:
                # update params
                pass
            
            # if Feedback_text is stopping this frame...
            if Feedback_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Feedback_text.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Feedback_text.tStop = t  # not accounting for scr refresh
                    Feedback_text.tStopRefresh = tThisFlipGlobal  # on global time
                    Feedback_text.frameNStop = frameN  # exact frame index
                    # update status
                    Feedback_text.status = FINISHED
                    Feedback_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=Feedback,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Feedback.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Feedback.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Feedback" ---
        for thisComponent in Feedback.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Feedback
        Feedback.tStop = globalClock.getTime(format='float')
        Feedback.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Feedback.stopped', Feedback.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Feedback.maxDurationReached:
            routineTimer.addTime(-Feedback.maxDuration)
        elif Feedback.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        # mark thisPractice_loop as finished
        if hasattr(thisPractice_loop, 'status'):
            thisPractice_loop.status = FINISHED
        # if awaiting a pause, pause now
        if practice_loop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            practice_loop.status = STARTED
    # completed 1.0 repeats of 'practice_loop'
    practice_loop.status = FINISHED
    
    
    # --- Prepare to start Routine "instruction_beforemain" ---
    # create an object to store info about Routine instruction_beforemain
    instruction_beforemain = data.Routine(
        name='instruction_beforemain',
        components=[text, key_resp],
    )
    instruction_beforemain.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # store start times for instruction_beforemain
    instruction_beforemain.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instruction_beforemain.tStart = globalClock.getTime(format='float')
    instruction_beforemain.status = STARTED
    thisExp.addData('instruction_beforemain.started', instruction_beforemain.tStart)
    instruction_beforemain.maxDuration = None
    # keep track of which components have finished
    instruction_beforemainComponents = instruction_beforemain.components
    for thisComponent in instruction_beforemain.components:
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
    
    # --- Run Routine "instruction_beforemain" ---
    instruction_beforemain.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
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
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            key_resp.clock.reset()  # now t=0
        if key_resp.status == STARTED:
            theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instruction_beforemain,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instruction_beforemain.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruction_beforemain.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction_beforemain" ---
    for thisComponent in instruction_beforemain.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instruction_beforemain
    instruction_beforemain.tStop = globalClock.getTime(format='float')
    instruction_beforemain.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instruction_beforemain.stopped', instruction_beforemain.tStop)
    thisExp.nextEntry()
    # the Routine "instruction_beforemain" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    Main_NoTimerLoop = data.TrialHandler2(
        name='Main_NoTimerLoop',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('C:/Users/anupm/Desktop/New stroop task/Wordlist for Main task.csv'), 
        seed=None, 
    )
    thisExp.addLoop(Main_NoTimerLoop)  # add the loop to the experiment
    thisMain_NoTimerLoop = Main_NoTimerLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMain_NoTimerLoop.rgb)
    if thisMain_NoTimerLoop != None:
        for paramName in thisMain_NoTimerLoop:
            globals()[paramName] = thisMain_NoTimerLoop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisMain_NoTimerLoop in Main_NoTimerLoop:
        Main_NoTimerLoop.status = STARTED
        if hasattr(thisMain_NoTimerLoop, 'status'):
            thisMain_NoTimerLoop.status = STARTED
        currentLoop = Main_NoTimerLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisMain_NoTimerLoop.rgb)
        if thisMain_NoTimerLoop != None:
            for paramName in thisMain_NoTimerLoop:
                globals()[paramName] = thisMain_NoTimerLoop[paramName]
        
        # --- Prepare to start Routine "Main_NoTimer" ---
        # create an object to store info about Routine Main_NoTimer
        Main_NoTimer = data.Routine(
            name='Main_NoTimer',
            components=[Word_NoTimer, key_resp_NoTimer],
        )
        Main_NoTimer.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        Word_NoTimer.setColor(Colour, colorSpace='rgb')
        Word_NoTimer.setText(Word)
        # create starting attributes for key_resp_NoTimer
        key_resp_NoTimer.keys = []
        key_resp_NoTimer.rt = []
        _key_resp_NoTimer_allKeys = []
        # Run 'Begin Routine' code from code
        Word_NoTimer.colorSpace = 'named'
        Word_NoTimer.setColor(Colour)
        Word_NoTimer.setText(Word)
        # store start times for Main_NoTimer
        Main_NoTimer.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Main_NoTimer.tStart = globalClock.getTime(format='float')
        Main_NoTimer.status = STARTED
        thisExp.addData('Main_NoTimer.started', Main_NoTimer.tStart)
        Main_NoTimer.maxDuration = None
        # keep track of which components have finished
        Main_NoTimerComponents = Main_NoTimer.components
        for thisComponent in Main_NoTimer.components:
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
        
        # --- Run Routine "Main_NoTimer" ---
        Main_NoTimer.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisMain_NoTimerLoop, 'status') and thisMain_NoTimerLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Word_NoTimer* updates
            
            # if Word_NoTimer is starting this frame...
            if Word_NoTimer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Word_NoTimer.frameNStart = frameN  # exact frame index
                Word_NoTimer.tStart = t  # local t and not account for scr refresh
                Word_NoTimer.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Word_NoTimer, 'tStartRefresh')  # time at next scr refresh
                # update status
                Word_NoTimer.status = STARTED
                Word_NoTimer.setAutoDraw(True)
            
            # if Word_NoTimer is active this frame...
            if Word_NoTimer.status == STARTED:
                # update params
                pass
            
            # *key_resp_NoTimer* updates
            
            # if key_resp_NoTimer is starting this frame...
            if key_resp_NoTimer.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_NoTimer.frameNStart = frameN  # exact frame index
                key_resp_NoTimer.tStart = t  # local t and not account for scr refresh
                key_resp_NoTimer.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_NoTimer, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp_NoTimer.status = STARTED
                # keyboard checking is just starting
                key_resp_NoTimer.clock.reset()  # now t=0
            if key_resp_NoTimer.status == STARTED:
                theseKeys = key_resp_NoTimer.getKeys(keyList=['r','g','b','y'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_NoTimer_allKeys.extend(theseKeys)
                if len(_key_resp_NoTimer_allKeys):
                    key_resp_NoTimer.keys = _key_resp_NoTimer_allKeys[-1].name  # just the last key pressed
                    key_resp_NoTimer.rt = _key_resp_NoTimer_allKeys[-1].rt
                    key_resp_NoTimer.duration = _key_resp_NoTimer_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_NoTimer.keys == str(Correctans)) or (key_resp_NoTimer.keys == Correctans):
                        key_resp_NoTimer.corr = 1
                    else:
                        key_resp_NoTimer.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=Main_NoTimer,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Main_NoTimer.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Main_NoTimer.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Main_NoTimer" ---
        for thisComponent in Main_NoTimer.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Main_NoTimer
        Main_NoTimer.tStop = globalClock.getTime(format='float')
        Main_NoTimer.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Main_NoTimer.stopped', Main_NoTimer.tStop)
        # check responses
        if key_resp_NoTimer.keys in ['', [], None]:  # No response was made
            key_resp_NoTimer.keys = None
            # was no response the correct answer?!
            if str(Correctans).lower() == 'none':
               key_resp_NoTimer.corr = 1;  # correct non-response
            else:
               key_resp_NoTimer.corr = 0;  # failed to respond (incorrectly)
        # store data for Main_NoTimerLoop (TrialHandler)
        Main_NoTimerLoop.addData('key_resp_NoTimer.keys',key_resp_NoTimer.keys)
        Main_NoTimerLoop.addData('key_resp_NoTimer.corr', key_resp_NoTimer.corr)
        if key_resp_NoTimer.keys != None:  # we had a response
            Main_NoTimerLoop.addData('key_resp_NoTimer.rt', key_resp_NoTimer.rt)
            Main_NoTimerLoop.addData('key_resp_NoTimer.duration', key_resp_NoTimer.duration)
        # Run 'End Routine' code from code
        
        thisExp.addData('Word', Word)
        thisExp.addData('Colour', Colour)
        thisExp.addData('Condition', Condition)
        thisExp.addData('CorrectAns', Correctans)
        
        thisExp.addData('KeyPressed', key_resp_NoTimer.keys)
        thisExp.addData('RT', key_resp_NoTimer.rt)
        thisExp.addData('Correct', key_resp_NoTimer.corr)
        
        # the Routine "Main_NoTimer" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisMain_NoTimerLoop as finished
        if hasattr(thisMain_NoTimerLoop, 'status'):
            thisMain_NoTimerLoop.status = FINISHED
        # if awaiting a pause, pause now
        if Main_NoTimerLoop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            Main_NoTimerLoop.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'Main_NoTimerLoop'
    Main_NoTimerLoop.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    # get names of stimulus parameters
    if Main_NoTimerLoop.trialList in ([], [None], None):
        params = []
    else:
        params = Main_NoTimerLoop.trialList[0].keys()
    # save data for this loop
    Main_NoTimerLoop.saveAsExcel(filename + '.xlsx', sheetName='Main_NoTimerLoop',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "Task2" ---
    # create an object to store info about Routine Task2
    Task2 = data.Routine(
        name='Task2',
        components=[text_2, key_resp_2],
    )
    Task2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_2
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # store start times for Task2
    Task2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Task2.tStart = globalClock.getTime(format='float')
    Task2.status = STARTED
    thisExp.addData('Task2.started', Task2.tStart)
    Task2.maxDuration = None
    # keep track of which components have finished
    Task2Components = Task2.components
    for thisComponent in Task2.components:
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
    
    # --- Run Routine "Task2" ---
    Task2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
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
            # update status
            text_2.status = STARTED
            text_2.setAutoDraw(True)
        
        # if text_2 is active this frame...
        if text_2.status == STARTED:
            # update params
            pass
        
        # *key_resp_2* updates
        
        # if key_resp_2 is starting this frame...
        if key_resp_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            key_resp_2.clock.reset()  # now t=0
        if key_resp_2.status == STARTED:
            theseKeys = key_resp_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=Task2,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Task2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Task2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Task2" ---
    for thisComponent in Task2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Task2
    Task2.tStop = globalClock.getTime(format='float')
    Task2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Task2.stopped', Task2.tStop)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.addData('key_resp_2.duration', key_resp_2.duration)
    thisExp.nextEntry()
    # the Routine "Task2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    Timerloop = data.TrialHandler2(
        name='Timerloop',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('C:/Users/anupm/Desktop/New stroop task/Wordlist for Main task.csv'), 
        seed=None, 
    )
    thisExp.addLoop(Timerloop)  # add the loop to the experiment
    thisTimerloop = Timerloop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTimerloop.rgb)
    if thisTimerloop != None:
        for paramName in thisTimerloop:
            globals()[paramName] = thisTimerloop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTimerloop in Timerloop:
        Timerloop.status = STARTED
        if hasattr(thisTimerloop, 'status'):
            thisTimerloop.status = STARTED
        currentLoop = Timerloop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTimerloop.rgb)
        if thisTimerloop != None:
            for paramName in thisTimerloop:
                globals()[paramName] = thisTimerloop[paramName]
        
        # --- Prepare to start Routine "Main_Timer" ---
        # create an object to store info about Routine Main_Timer
        Main_Timer = data.Routine(
            name='Main_Timer',
            components=[TimerText, key_resp_timer, word_timer],
        )
        Main_Timer.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from TimerCode
        if not hasattr(thisExp, "timerClock"):
            thisExp.timerClock = core.Clock()       # starts at 0
            thisExp.timerDuration = 15.0            # total allowed time
        
        TimerText.setText('')
        # create starting attributes for key_resp_timer
        key_resp_timer.keys = []
        key_resp_timer.rt = []
        _key_resp_timer_allKeys = []
        word_timer.setColor(Colour, colorSpace='rgb')
        word_timer.setText(Word)
        # store start times for Main_Timer
        Main_Timer.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Main_Timer.tStart = globalClock.getTime(format='float')
        Main_Timer.status = STARTED
        thisExp.addData('Main_Timer.started', Main_Timer.tStart)
        Main_Timer.maxDuration = None
        # keep track of which components have finished
        Main_TimerComponents = Main_Timer.components
        for thisComponent in Main_Timer.components:
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
        
        # --- Run Routine "Main_Timer" ---
        Main_Timer.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTimerloop, 'status') and thisTimerloop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from TimerCode
            elapsed = thisExp.timerClock.getTime()
            remaining = thisExp.timerDuration - elapsed
            
            sign = "-" if remaining < 0 else ""
            seconds = int(abs(remaining))
            hundredths = int(abs((remaining - int(remaining)) * 100))
            TimerText.setText(f"{sign}{seconds:02d}:{hundredths:02d}")
            if remaining <= 5 and remaining >= 0:
                TimerText.color = "red"
            else:
                TimerText.color = "white"
            
            # *TimerText* updates
            
            # if TimerText is starting this frame...
            if TimerText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TimerText.frameNStart = frameN  # exact frame index
                TimerText.tStart = t  # local t and not account for scr refresh
                TimerText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TimerText, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TimerText.started')
                # update status
                TimerText.status = STARTED
                TimerText.setAutoDraw(True)
            
            # if TimerText is active this frame...
            if TimerText.status == STARTED:
                # update params
                pass
            
            # *key_resp_timer* updates
            waitOnFlip = False
            
            # if key_resp_timer is starting this frame...
            if key_resp_timer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_timer.frameNStart = frameN  # exact frame index
                key_resp_timer.tStart = t  # local t and not account for scr refresh
                key_resp_timer.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_timer, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_timer.started')
                # update status
                key_resp_timer.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_timer.clock.reset)  # t=0 on next screen flip
            if key_resp_timer.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_timer.getKeys(keyList=['r','g','b','y'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_timer_allKeys.extend(theseKeys)
                if len(_key_resp_timer_allKeys):
                    key_resp_timer.keys = _key_resp_timer_allKeys[-1].name  # just the last key pressed
                    key_resp_timer.rt = _key_resp_timer_allKeys[-1].rt
                    key_resp_timer.duration = _key_resp_timer_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_timer.keys == str(Correctans)) or (key_resp_timer.keys == Correctans):
                        key_resp_timer.corr = 1
                    else:
                        key_resp_timer.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *word_timer* updates
            
            # if word_timer is starting this frame...
            if word_timer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                word_timer.frameNStart = frameN  # exact frame index
                word_timer.tStart = t  # local t and not account for scr refresh
                word_timer.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(word_timer, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'word_timer.started')
                # update status
                word_timer.status = STARTED
                word_timer.setAutoDraw(True)
            
            # if word_timer is active this frame...
            if word_timer.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=Main_Timer,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Main_Timer.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Main_Timer.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Main_Timer" ---
        for thisComponent in Main_Timer.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Main_Timer
        Main_Timer.tStop = globalClock.getTime(format='float')
        Main_Timer.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Main_Timer.stopped', Main_Timer.tStop)
        # Run 'End Routine' code from TimerCode
        thisExp.addData('Word', Word)
        thisExp.addData('Colour', Colour)
        thisExp.addData('Condition', Condition)
        thisExp.addData('CorrectAns', Correctans)
        thisExp.addData('KeyPressed', key_resp_timer.keys)
        thisExp.addData('RT', key_resp_timer.rt)
        thisExp.addData('Correct', key_resp_timer.corr)
        
        # check responses
        if key_resp_timer.keys in ['', [], None]:  # No response was made
            key_resp_timer.keys = None
            # was no response the correct answer?!
            if str(Correctans).lower() == 'none':
               key_resp_timer.corr = 1;  # correct non-response
            else:
               key_resp_timer.corr = 0;  # failed to respond (incorrectly)
        # store data for Timerloop (TrialHandler)
        Timerloop.addData('key_resp_timer.keys',key_resp_timer.keys)
        Timerloop.addData('key_resp_timer.corr', key_resp_timer.corr)
        if key_resp_timer.keys != None:  # we had a response
            Timerloop.addData('key_resp_timer.rt', key_resp_timer.rt)
            Timerloop.addData('key_resp_timer.duration', key_resp_timer.duration)
        # the Routine "Main_Timer" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisTimerloop as finished
        if hasattr(thisTimerloop, 'status'):
            thisTimerloop.status = FINISHED
        # if awaiting a pause, pause now
        if Timerloop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            Timerloop.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'Timerloop'
    Timerloop.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    # get names of stimulus parameters
    if Timerloop.trialList in ([], [None], None):
        params = []
    else:
        params = Timerloop.trialList[0].keys()
    # save data for this loop
    Timerloop.saveAsExcel(filename + '.xlsx', sheetName='Timerloop',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "Thanks_Screen_" ---
    # create an object to store info about Routine Thanks_Screen_
    Thanks_Screen_ = data.Routine(
        name='Thanks_Screen_',
        components=[Thanks, text_3],
    )
    Thanks_Screen_.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Thanks
    Thanks.keys = []
    Thanks.rt = []
    _Thanks_allKeys = []
    # store start times for Thanks_Screen_
    Thanks_Screen_.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Thanks_Screen_.tStart = globalClock.getTime(format='float')
    Thanks_Screen_.status = STARTED
    thisExp.addData('Thanks_Screen_.started', Thanks_Screen_.tStart)
    Thanks_Screen_.maxDuration = None
    # keep track of which components have finished
    Thanks_Screen_Components = Thanks_Screen_.components
    for thisComponent in Thanks_Screen_.components:
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
    
    # --- Run Routine "Thanks_Screen_" ---
    Thanks_Screen_.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Thanks* updates
        waitOnFlip = False
        
        # if Thanks is starting this frame...
        if Thanks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Thanks.frameNStart = frameN  # exact frame index
            Thanks.tStart = t  # local t and not account for scr refresh
            Thanks.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Thanks, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Thanks.started')
            # update status
            Thanks.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Thanks.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Thanks.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Thanks.status == STARTED and not waitOnFlip:
            theseKeys = Thanks.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _Thanks_allKeys.extend(theseKeys)
            if len(_Thanks_allKeys):
                Thanks.keys = _Thanks_allKeys[-1].name  # just the last key pressed
                Thanks.rt = _Thanks_allKeys[-1].rt
                Thanks.duration = _Thanks_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=Thanks_Screen_,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Thanks_Screen_.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Thanks_Screen_.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Thanks_Screen_" ---
    for thisComponent in Thanks_Screen_.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Thanks_Screen_
    Thanks_Screen_.tStop = globalClock.getTime(format='float')
    Thanks_Screen_.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Thanks_Screen_.stopped', Thanks_Screen_.tStop)
    # check responses
    if Thanks.keys in ['', [], None]:  # No response was made
        Thanks.keys = None
    thisExp.addData('Thanks.keys',Thanks.keys)
    if Thanks.keys != None:  # we had a response
        thisExp.addData('Thanks.rt', Thanks.rt)
        thisExp.addData('Thanks.duration', Thanks.duration)
    thisExp.nextEntry()
    # the Routine "Thanks_Screen_" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)

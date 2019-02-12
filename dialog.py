# -*- coding: utf-8 -*-
import FSM
import JuliusProxy
import subprocess
from google.cloud import translate



#def callFirefox(inp):
#    path = "/home/harkuser/document/html/hark-document-ja/subsec"
#    node = inp[1]["WORD"]
#    cmd = "firefox %s%s.html" % (path, node)
#    subprocess.Popen(cmd.split())


def translate_text(inp):
    text = inp[1]["WORD"]
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language='ja')
    return result['translatedText']


def getClassID(inp):
    return inp[1]["CLASSID"]

def getClassID2(inp):
    return inp[1]["CLASSID"]

def pmgFunc(inp):
    i = 0
    while i != len(inp):
        if inp[i]["CLASSID"] == 3:
	    return inp[i]["CLASSID"]
	else:
	    i = i + 1
    return 0

def noAnswer(inp):
    i = 0
    while i != len(inp):
        if inp[i]["CLASSID"] == 22:
	    return inp[i]["CLASSID"]
	else:
	    i = i + 1
    return 0


def yesAnswer(inp):
    i = 0
    while i != len(inp):
        if inp[i]["CLASSID"] == 23:
	    return inp[i]["CLASSID"]
	else:
	    i = i + 1
    return 0

def plasticFunc(inp):
    i = 0
    while i != len(inp):
        if inp[i]["CLASSID"] == 10:
	    return inp[i]["CLASSID"]
	else:
	    i = i + 1
    return 0

def circleFunc(inp):
    i = 0
    while i != len(inp):
        if inp[i]["CLASSID"] == 25:
	    return inp[i]["CLASSID"]
	else:
	    i = i + 1
    return 0

def triangleFunc(inp):
    i = 0
    while i != len(inp):
        if inp[i]["CLASSID"] == 26:
	    return inp[i]["CLASSID"]
	else:
	    i = i + 1
    return 0

def squareFunc(inp):
    i = 0
    while i != len(inp):
        if inp[i]["CLASSID"] == 27:
	    return inp[i]["CLASSID"]
	else:
	    i = i + 1
    return 0

def unsureFunc(inp):
    i = 0
    while i != len(inp):
        if inp[i]["CLASSID"] == 14:
	    return inp[i]["CLASSID"]
	else:
	    i = i + 1
    return 0

def metalFunc(inp):
    i = 0
    while i != len(inp):
        if inp[i]["CLASSID"] == 11:
	    return inp[i]["CLASSID"]
	else:
	    i = i + 1
    return 0

def alumFunc(inp):
    i = 0
    while i != len(inp):
        if inp[i]["CLASSID"] == 26:
	    return inp[i]["CLASSID"]
	else:
	    i = i + 1
    return 0


def steelFunc(inp):
    i = 0
    while i != len(inp):
        if inp[i]["CLASSID"] == 25:
	    return inp[i]["CLASSID"]
	else:
	    i = i + 1
    return 0

def glassFunc(inp):
    i = 0
    while i != len(inp):
        if inp[i]["CLASSID"] == 12:
	    return inp[i]["CLASSID"]
	else:
	    i = i + 1
    return 0

def pathMFunc(inp):
    i = 0
    while i != len(inp):
        if inp[i]["CLASSID"] == 4:
	    return inp[i]["CLASSID"]
	else:
	    i = i + 1
    return 0

def paperFunc(inp):
    i = 0
    while i != len(inp):
        if inp[i]["CLASSID"] == 5:
	    return inp[i]["CLASSID"]
	else:
	    i = i + 1
    return 0

def paperFunc2(inp):
    i = 0
    while i != len(inp):
        if inp[i]["CLASSID"] == 13:
	    return inp[i]["CLASSID"]
	else:
	    i = i + 1
    return 0

def newsFunc(inp):
    i = 0
    while i != len(inp):
        if inp[i]["CLASSID"] == 6:
	    return inp[i]["CLASSID"]
	else:
	    i = i + 1
    return 0

def ppFunc(inp):
    i = 0
    while i != len(inp):
        if inp[i]["CLASSID"] == 7:
	    return inp[i]["CLASSID"]
	else:
	    i = i + 1
    return 0

def plasticFunc2(inp):
    i = 0
    while i != len(inp):
        if inp[i]["CLASSID"] == 10:
	    return inp[i]["CLASSID"]
	else:
	    i = i + 1
    return 0

def plasticFunc3(inp):
    i = 0
    while i != len(inp):
        if inp[i]["CLASSID"] == 8:
	    return inp[i]["CLASSID"]
	else:
	    i = i + 1
    return 0

def batteryFunc(inp):
    i = 0
    while i != len(inp):
        if inp[i]["CLASSID"] == 9:
	    return inp[i]["CLASSID"]
	else:
	    i = i + 1
    return 0


def getWord(inp):
    return inp[1]["WORD"]

def stop(inp):
    print "This test script is defined until here.  Terminated."
    sys.exit()


# construct and add transition rules
greet = FSM.State()
regreet = FSM.State()
endChoose = FSM.State()
pathChoose = FSM.State()
pathPMG = FSM.State()
pathPlPET = FSM.State()
pathM = FSM.State()
pathPa = FSM.State()
pathPP = FSM.State()
pathPl = FSM.State()
pathGl = FSM.State()
askMore = FSM.State()
end = FSM.State()

#set FST transitions

greet.setTransition("", [], pathChoose, "Hi, I’ll be helping you with recycling. What would you like to recycle first?")
regreet.setTransition("",[], pathChoose, "What else would you like to recycle?")
#SODA
pathChoose.setTransition(pmgFunc,[3,],pathPMG,"Alright. And is it made of plastic, metal, or glass?")
#plasticRoute
pathPMG.setTransition(plasticFunc, [10,], pathPlPET, "Sure. Turn it around. There should be a recycling shaped label with arrows. Which one of these do you see, a triangle or a square?")
#PET
pathPlPET.setTransition(triangleFunc, [26,], endChoose, "Good job, were almost done. Just remove the cap and the plastic around the bottle. Dispose of these in the recyclable plastics garbage and dispose of the bottle in the PET bottles garbage. Is there anything else you need to recycle?")
#Plastic
pathPlPET.setTransition(squareFunc, [27,], endChoose, "Were done! Just dispose of it in a plastics bin. Is there anything else you need to recycle?")
#Other
pathPlPET.setTransition(unsureFunc,[14,], endChoose, "Thats ok. The city of Ibaraki has a special bin for other waste, simply dispose of it there. Is there anything else you need to recycle?")
#metalRoute
pathPMG.setTransition(metalFunc,[11,],pathM,"Ok, turn it around to the nutritional information. There should be a recycling shaped label with arrows. Which one of these do you see, a circle or a triangle?")
#glassRoute
pathPMG.setTransition(glassFunc,[12,],endChoose,"Just remove the cap and dispose of it in the metals bin. Dispose the bottle in the glass bin. And thats it! Is there anything else you need to recycle?")
#CAN
pathChoose.setTransition(pathMFunc,[4,],pathM,"Ok, turn it around to the nutritional information. There should be a recycling shaped label with arrows. Which one of these do you see, a circle or a triangle?")
#steel
pathM.setTransition(circleFunc,[25,],endChoose,"Perfect, just throw it away in a steel garbage bin. Is there anything else you need to recycle?")
#aluminum
pathM.setTransition(triangleFunc,[26,],endChoose,"Perfect, just throw it away in a aluminum garbage bin. Is there anything else you need to recycle?")
#other
pathM.setTransition(unsureFunc,[14,], endChoose, "Thats ok. The city of Ibaraki has a special bin for other waste, simply dispose of it there. Is there anything else you need to recycle?")
#PAPER
pathChoose.setTransition(paperFunc,[5,], pathPa, "Great. And is there any plastic on it?")
#impure
pathPa.setTransition(yesAnswer,[23,], endChoose, "Thats ok. The city of Ibaraki has a special bin for other waste, simply dispose of it there. Is there anything else you need to recycle?")
#pure
pathPa.setTransition(noAnswer,[22,], endChoose, "Perfect, just throw it in the paper bin. Is there anything else you need to recycle?")
#NEWSPAPER
pathChoose.setTransition(newsFunc,[6,],endChoose, "Simply put it in a newspaper recycling bin. Is there anything else you need to recycle?")
#WRAPPER
pathChoose.setTransition(ppFunc,[7,],pathPP, "Got it, is it made mainly of plastic or paper?")
#paper
pathPP.setTransition(paperFunc2, [13,], pathPa, "Great. And is there any plastic on it?")
#plastic10
pathPP.setTransition(plasticFunc2, [10,], pathPl, "Ok, do you see a square shaped label with arrows?")
#pure
pathPl.setTransition(yesAnswer,[23,], endChoose, "Perfect, just throw it in the plastic bin. Is there anything else you need to recycle?")
#impure
pathPl.setTransition(noAnswer,[22,], endChoose, "Thats ok. The city of Ibaraki has a special bin for other waste, simply dispose of it there. Is there anything else you need to recycle?")
#SUNSCREENBOTTLE(PLASTIC)
pathChoose.setTransition(plasticFunc3,[8,],pathPl, "Got it. Turn it around. Do you see a square shaped label with arrows?")
#BATTERY
pathChoose.setTransition(batteryFunc,[9,],endChoose,"Simply put it in a battery recycling bin. Is there anything else you need to recycle?")
endChoose.setTransition(noAnswer,[22,],end,"Thank you for helping the planet.")
endChoose.setTransition(yesAnswer,[23,],regreet,"No worries. Are you ready?")
end.setTransition("", [], None, stop)
#askMore.setTransition(getClassID, [3,], askMore,"Anything else?")
#askMore.setTransition(getClassID, [5,], askMore, translate_text)
#askMore.setTransition(getClassID, [7,], askMore,translate_text)


# construct Finite State Machine and register the states.
fsm = FSM.FSM()
fsm.setState(greet)
fsm.setState(askMore)
fsm.setState(regreet)
fsm.setState(endChoose)
fsm.setState(pathChoose)
fsm.setState(pathPMG)
fsm.setState(pathPlPET)
fsm.setState(pathM)
fsm.setState(pathPa)
fsm.setState(pathPP)
fsm.setState(pathPl)
fsm.setState(pathGl)
fsm.setState(end)

# connect to julius
proxy = JuliusProxy.JuliusProxy()
while 1:
    proxy.getResult()  # get ASR result
    result = proxy.parseResult() # parse ASR result
    if result == []: continue
    print result

    # give the result to FSM
    fsm.feed(result)



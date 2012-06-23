#!/usr/bin/env python
import pyttsx
import random
import time
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-i', '--interval', dest='interval', default=3, type=int,
                help='Number of seconds between twister commands. Default is 3.')
parser.add_option('-p', '--probe', dest='probe', default=100, type=int,
                help='Amount of twister commands to be generated before speech engine init.')
parser.add_option('-s', '--silent', action='store_true', dest='silent', default=False,
                help='Don\'t use speech engine, just output text messages.')

(options, args) = parser.parse_args()

def getRandomTwisterCommand():
    limbs = [
        'left hand',
        'left foot',
        'right hand',
        'right foot',
    ]
    colors = [
        'yellow',
        'blue',
        'green',
        'red',
    ]
    random.seed(time.time())
    limb = limbs[random.randint(0,len(limbs)-1)]
    color = colors[random.randint(0,len(colors)-1)]
    return 'Next move: {0} to {1}'.format(limb, color)

def onWord(name, location, length):
    time.sleep(options.interval)

def endProgram(engine=None):
    if engine:
        engine.stop()
    print '\nBye bye..'
    exit()

if not options.silent:
    engine = pyttsx.init()
    engine.connect('started-word',onWord)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-70)

for x in range(600):
    if (options.silent):
        print getRandomTwisterCommand()
        time.sleep(options.interval)
    else:
        engine.say(getRandomTwisterCommand())

if not options.silent:
    try:
        engine.runAndWait()
    except KeyboardInterrupt, e:
        endProgram(engine)
    except Exception, e:
        endProgram(engine)
    endProgram(engine)
else:
    endProgram()

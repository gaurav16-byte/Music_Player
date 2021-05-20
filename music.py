import subprocess
import sys
import os

def prereq():
    test = subprocess.run(['pip', 'list'],capture_output=True, text=True).stdout
    while 'pygame' not in test:
        subprocess.run(['pip', 'install', 'pygame']) #, capture_output=True, text=True).stdout
    else:
        pass

prereq()

from pygame import mixer
print('\n')
print('CONTROLS:')
print('PLAY - P/p   PAUSE - spacebar   RESUME - R/r   STOP - S/s   NEXT - N/n   EXIT - E/e')
print('\n')
location = input('Enter the path to music folder Ex. C:\\\Documents\\\Music\\\ ')
files = os.listdir(location)

mixer.init()
i=0
while True:
    a = input('> ')
    while a not in 'SsPp RrNnEe':
        print('Invalid Option')
        print('CONTROLS:')
        print('PLAY - P/p   PAUSE - spacebar   RESUME - R/r   STOP - S/s   NEXT - N/n   EXIT - E/e')
        a = input('> ')
    else:
        if a in 'Pp':
            mixer.music.load(location + files[i])
            print('NOW PLAYING',files[i][:-4])
            mixer.music.play()
        elif a in ' ':
            mixer.music.pause()
            print('PLAYBACK PAUSED')
        elif a in "Ss":
            mixer.music.stop()
            print('PLAYBACK STOPPED')
        elif a in 'Rr':
            mixer.music.unpause()
            print('PLAYBACK RESUMED.')
        elif a in 'Nn':
            if i < len(files)-1:
                i += 1
                mixer.music.stop()
                mixer.music.load(location + files[i])
                print('NOW PLAYING',files[i][:-4])
                mixer.music.play()
            else:
                i = 0
                mixer.music.stop()
                mixer.music.load(location + files[i])
                print('NOW PLAYING',files[i][:-4])
                mixer.music.play()
        elif a in 'Ee':
            mixer.music.stop()
            sys.exit()

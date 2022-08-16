import time 
from playsound import playsound

seconds=int( input("Enter the time in seconds "))

def countdown_timer(seconds):
    while seconds>0:
        mins=int(seconds/60)
        secs=int(seconds%60)
        timer=f'{mins}:{secs}'
        print(timer)
        time.sleep(1)
        seconds-=1
    print("time's up!")
    #playsound("mixkit-sound.wav")
        
   

countdown_timer(seconds)
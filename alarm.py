from threading import Thread
from datetime import datetime
import time as t
from plyer import notification
import winsound

def send_notification(msg:str):
    notification.notify(
        title="Python Alram by Sachin Shrivastav",
        message=msg,
        app_icon="alram_icon.ico",  
        timeout=5
    )

def play_sound():

# Play the sound
    sound_file = "alram_tone.wav"
    winsound.PlaySound(sound_file, winsound.SND_FILENAME)


def alarm(time:str, msg:str):
    while True:
        current_time = datetime.now().time().strftime("%H:%M")
        if current_time == time:
            send_notification(msg)
            play_sound()
            break
        t.sleep(30)


set_time = input(f"Set alram with like 18:05: ")
msg = input("Enter alram description: ")
Thread(target=alarm, args=(set_time,msg)).start()

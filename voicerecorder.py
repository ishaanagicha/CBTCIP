#importing all the required modules for the 
from tkinter import *
from tkinter import messagebox
import sounddevice as sdv
import wavio as wvi
from tkinter.filedialog import askdirectory

#asking for the duration of how much the user wants to record
time = int(input("enter the duration in seconds for the recording"))
#entering the frequency for the sound to be recorded
freq = 44100
sec=time

#creating a function for the program to execute 
def savefile():
    print("recording in process .......")
    recording = sdv.rec(sec*freq , samplerate=freq , channels=2)
    sdv.wait()
    wvi.write("recording.wav",recording, freq , sampwidth=2)
    print("recoding done and saved with the name 'recording.wav' in your desired location'")
    
#calling the function for the code to be executed 
savefile()

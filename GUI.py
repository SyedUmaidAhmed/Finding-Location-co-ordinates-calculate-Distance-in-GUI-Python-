from tkinter import *
from math import radians, cos, sin, asin, sqrt

import os
import geocoder
from os import path
import sys
import tkinter.font
import tkinter.messagebox
import subprocess
import tkinter as tk

from subprocess import Popen
from time import sleep
import PIL.Image

# Admin can exit the app by pressing ctrl + C on keyboard

g = geocoder.ip('me')



def haversine(lon1, lat1, lon2, lat2):
    lon1 = radians(lon1)
    lat1 = radians(lat1)
    lon2 = radians(lon2)
    lat2 = radians(lat2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1


    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = distance = 2 * asin(sqrt(a))
    r = 6371
    z= c * r
    print(z)




def run():
    try:
        main()
    except:
        os.system('killall omxplayer.bin')
        sys.exit()
        root.destroy()
            
            


def main():


    def quit(event):
        
        print("Ended the Program")
        root.destroy()
        root.quit()
        sys.exit()
        os.system('killall omxplayer.bin')

    
    root =Tk()
    frame = Frame(root)
    bottomframe = Frame(root)
    root.title('[LOCATION-TRACKER]')



    #the below two lines are two modes of full screen (enjoy what youy want !)

    #root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    #root.attributes("-fullscreen", True)








    root.focus_set()


    def Video_One():
        global a
        global b
        a=(g.lng)
        b=(g.lat)
        print(a)
        print(b)       
        

    def Video_two():

        global c
        global d
        c=(g.lng)
        d=(g.lat)
        print(c)
        print(d)

        
       

    def image_file():
        
        
        
        haversine(a,b,c,d)


        



        

##
##    def Text_box():
##        image = Image.open('tes1.jpg')
##        image.show()
##        sleep(3)
##        sys.exit()
####
##
##
##    def Video_Five():
##        tkinter.messagebox.showinfo( "Hello", "How are you ? Sir !!!")
##
##    def Video_Six():
##        tkinter.messagebox.showinfo( "Project", "Hey man, It's Party Time !!!")
##
##    def Video_Seven():
##        movie_path = '/home/pi/echi.mp4'
##        omxp = Popen(['omxplayer',movie_path])
##
##    def Video_Eight():
##        movie_path = '/home/pi/cloud.mp4'
##        omxp = Popen(['omxplayer',movie_path])
##
##    def Video_Nine():
##        image = Image.open('Test1.png')
##        image.show()
##        
##    def Video_Ten():
##        movie_path = '/home/pi/nig.mp4'
##        omxp = Popen(['omxplayer',movie_path







    redbutton=Button(text="First-Location", command = Video_One)
    redbutton.config(bg='dark red', width='10', bd='4', relief='groove', fg='white')
    redbutton.config(font=('helvetica',20,'bold italic'))
    redbutton.grid(row=2, column=2, padx=70, pady=70)



    # If you want the button to disabled, please uncomment the following line
    # and also delete the second line in upper pair of 4 lines
    # redbutton.config(bg='dark red', width='10', bd='4', relief='groove', fg='white', state = 'disabled')





    redbutton =Button(text="Destination", command = Video_two)
    redbutton.config(bg='dark red', width='10', bd='4', relief='groove', fg='white')
    redbutton.config(font=('helvetica',20,'bold italic'))
    redbutton.grid(row=3, column=2, padx=70, pady=70)

    redbutton =Button(text="Displacement", command = image_file)
    redbutton.config(bg='dark red', width='10', bd='4', relief='groove', fg='white')
    redbutton.config(font=('helvetica',20,'bold italic'))
    redbutton.grid(row=4, column=2, padx=70, pady=70)


##    redbutton =Button(text="Send Text", command =Text_box)
##    redbutton.config(bg='dark red', width='10', bd='4', relief='groove', fg='white')
##    redbutton.config(font=('helvetica',20,'bold italic'))
##    redbutton.grid(row=2, column=3, padx=40, pady=40)
##
##
##    redbutton =Button(text="Video Five", command = Video_Five)
##    redbutton.config(bg='dark red', width='10', bd='4', relief='groove', fg='white')
##    redbutton.config(font=('helvetica',20,'bold italic'))
##    redbutton.grid(row=4, column=2, padx=40, pady=40)
##
##
##
##    redbutton =Button(text="Video Six", command =Video_Six)
##    redbutton.config(bg='dark red', width='10', bd='4', relief='groove', fg='white')
##    redbutton.config(font=('helvetica',20,'bold italic'))
##    redbutton.grid(row=4, column=3, padx=40, pady=40)
##
##
##
##    redbutton =Button(text="Video Seven", command = Video_Seven)
##    redbutton.config(bg='dark red', width='10', bd='4', relief='groove', fg='white')
##    redbutton.config(font=('helvetica',20,'bold italic'))
##    redbutton.grid(row=6, column=2, padx=40, pady=40)
##
##
##    redbutton =Button(text="Video Eight", command = Video_Eight)
##    redbutton.config(bg='dark red', width='10', bd='4', relief='groove', fg='white')
##    redbutton.config(font=('helvetica',20,'bold italic'))
##    redbutton.grid(row=6, column=3, padx=40, pady=40)
##
##
##
##    redbutton =Button(text="Image Two", command = Video_Nine)
##    redbutton.config(bg='dark red', width='10', bd='4', relief='groove', fg='white')
##    redbutton.config(font=('helvetica',20,'bold italic'))
##    redbutton.grid(row=8, column=2, padx=40, pady=40)
##
##
##
##    redbutton =Button(text="Video Ten", command = Video_Ten)
##    redbutton.config(bg='dark red', width='10', bd='4', relief='groove', fg='white')
##    redbutton.config(font=('helvetica',20,'bold italic'))
##    redbutton.grid(row=8, column=3, padx=40, pady=40)

    root.bind('<Control-c>', quit)
    root.mainloop()



if __name__ == '__main__':
    run()

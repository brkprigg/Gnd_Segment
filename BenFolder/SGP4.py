# ------------------------------
# Determine Doppler Shift for PolarCube's Uplink and Downlink Frequencies Using SGP4 Model.
# ------------------------------
# Author: Benjamin K. Hagenau
# Created: 7/10/17
# Edited: 7/12/17
# ------------------------------

from sgp4.earth_gravity import wgs72
from sgp4.io import twoline2rv

import math
import datetime
import urllib
import time

from tkinter import *
from tkinter.ttk import *

# FUNCTION: calculate doppler shift using special general perturbations model
def dopplerCalc():
    # Define Base Frequency
    f0_uplink = 145.975 * 10**6     #Hz
    f0_downlink =145.975 * 10**6    #Hz

    # Define Constants
    w_earth = .00417  # Earth's angular rate [deg/s]
    c = 2.998*10**8   # Speed of light [m/s]

    # Allocate
    V_ECEF = [None]*3 # Velocity of s/c in ECEF

    # Determine current data and time
    time = datetime.datetime.now()


    # Extract 2 line elements from CelesTrak
    # http://celestrak.com/NORAD/elements/ has links to other satellite types
    #link = 'http://celestrak.com/NORAD/elements/amateur.txt' #amature satellites
    #f = urllib.urlopen(link)
    satname = "OSCAR 7 (AO-7)" #f.readline()
    line1 = "1 07530U 74089B   17193.22744222 -.00000036  00000-0  50100-4 0  9999" #f.readline()
    line2 = "2 07530 101.6320 161.4204 0011595 274.6255 201.3315 12.53627701951767" #f.readline()
    #print(satname)
    #print(line1)
    #print(line2)

    # Transfer two 2-line elements to object
    satellite = twoline2rv(line1, line2, wgs72)
    # Propogate model to determine velocity and positon relative to Earth's center given time
    position, velocity = satellite.propagate(time.year, time.month, time.day, time.hour, time.minute, time.second)

    # Determine velocity magnitude
    Vmag_ECI = math.sqrt(velocity[0]**2 + velocity[1]**2 + velocity[2]**2)

    # Determine total number of seconds passed
    seconds = time.hour*3600 + time.minute*60 + time.second

    # Determine total number of degrees rotated
    theta = w_earth * seconds

    # Transfer s/c velocity from ECI to ECEF (Boulder velocity = 0 in ECEF)
    V_ECEF[0] = Vmag_ECI*math.cos(theta*math.pi/180)
    V_ECEF[1] = Vmag_ECI*math.sin(theta*math.pi/180)
    V_ECEF[2] = velocity[2]

    # Determine velocity magnitude
    Vmag_ECEF = math.sqrt(V_ECEF[0]**2 + V_ECEF[1]**2 + V_ECEF[2]**2)

    # Determine doppler shift
    doppler_uplink = (Vmag_ECEF*(10**3)/c) * f0_uplink #[Hz]
    doppler_downlink = (Vmag_ECEF*(10**3)/c) * f0_downlink #[Hz]

    return doppler_uplink*10**(-3), doppler_downlink*10**(-3)

# FUNCTION: create timer function for GUI update
def clock():
    current = datetime.datetime.now()                                            # draw current time
    date = str(current.year) + "-" + str(current.month) + "-" + str(current.day) # create date string
    time = datetime.datetime.now().strftime("Time: %H:%M:%S")                    # create time string

    # Call doppler shift calculation function
    doppler_up, doppler_down = dopplerCalc()
    # Define the preset label
    dateLabel.config(text = date)                                      # date
    timeLabel.config(text = time)                                      # time
    titleLabel.config(text = "\n--- Doppler Shift [kHz] ---")          # title
    dopUpLabel.config(text = "Uplink: " + str(round(doppler_up,4)))                      # uplink doppler
    dopDownLabel.config(text = "Downlink: " + str(round(doppler_down,4)))                  # downlink doppler

    # Run itself again after 1000 ms
    root.after(1000, clock)


# Create GUI
root = Tk()
#------------------------------------------------------
# Place blank label in GUI
dateLabel = Label(root)      # date
dateLabel.pack(side = 'top')

timeLabel = Label(root)      # time
timeLabel.pack(side = 'top')

titleLabel = Label(root)     # title
titleLabel.pack(side = 'top')

dopUpLabel = Label(root)     # uplink doppler
dopUpLabel.pack(side = 'top')

dopDownLabel = Label(root)   # downling doppler
dopDownLabel.pack(side = 'top')

# run first time
clock()
#------------------------------------------------------
root.mainloop()

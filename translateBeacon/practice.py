from tkinter import *

root = Tk()

leftFrame = Frame(root)
leftFrame.pack(side = LEFT)

rightFrame = Frame(root)
rightFrame.pack(side = LEFT)


satTimelabelFrame = LabelFrame(leftFrame, text="Satellite Time")
satTimelabelFrame.pack(anchor = 'w')

if (display_name == "satTime")
  satTimeLabel = Label(satTimelabelFrame, text="satTime:  " + data)
  satTimeLabel.pack(anchor = 'w')

GPSlabelFrame = LabelFrame(leftFrame, text="GPS")
GPSlabelFrame.pack(side = TOP, anchor = 'w')

elif (display_name == "GPSWeek")
  GPSWeekLabel = Label(GPSlabelFrame, text="GPSWeek:  " + data)
  GPSWeekLabel.pack(anchor = 'w')

elif (display_name == "GPSSec")
  GPSSecLabel = Label(GPSlabelFrame, text="GPSSec:  " + data)
  GPSSecLabel.pack(side = TOP, anchor = 'w')

Random1labelFrame = LabelFrame(leftFrame, text="Random1")
Random1labelFrame.pack(side = TOP, anchor = 'w')

elif (display_name == "systemMode")
  systemModeLabel = Label(Random1labelFrame, text="systemMode:  " + data)
  systemModeLabel.pack(anchor = 'w')

elif (display_name == "subpowerStates")
  subpowerStatesLabel = Label(Random1labelFrame, text="subpowerStates:  " + data)
  subpowerStatesLabel.pack(side = TOP, anchor = 'w')

elif (display_name == "epochNumber")
  epochNumberLabel = Label(Random1labelFrame, text="epochNumber:  " + data)
  epochNumberLabel.pack(side = TOP, anchor = 'w')

elif (display_name == "radNumber")
  radNumberLabel = Label(Random1labelFrame, text="radNumber:  " + data)
  radNumberLabel.pack(side = TOP, anchor = 'w')

Random2labelFrame = LabelFrame(leftFrame, text="Random2")
Random2labelFrame.pack(side = TOP, anchor = 'w')

elif (display_name == "batteryCap")
  batteryCapLabel = Label(Random2labelFrame, text="batteryCap:  " + data)
  batteryCapLabel.pack(anchor = 'w')

elif (display_name == "acsMode")
  acsModeLabel = Label(Random2labelFrame, text="acsMode:  " + data)
  acsModeLabel.pack(side = TOP, anchor = 'w')

elif (display_name == "memory")
  memoryLabel = Label(Random2labelFrame, text="memory:  " + data)
  memoryLabel.pack(side = TOP, anchor = 'w')

elif (display_name == "cpu15")
  cpu15Label = Label(Random2labelFrame, text="cpu15:  " + data)
  cpu15Label.pack(side = TOP, anchor = 'w')

positionlabelFrame = LabelFrame(rightFrame, text="Position Vectors")
positionlabelFrame.pack(anchor = 'w')

elif (display_name == "xPosition")
  xPositionLabel = Label(positionlabelFrame, text="xPosition:  " + data)
  xPositionLabel.pack(anchor = 'w')

elif (display_name == "yPosition")
  yPositionLabel = Label(positionlabelFrame, text="yPosition:  " + data)
  yPositionLabel.pack(side = TOP, anchor = 'w')

elif (display_name == "zPosition")
  zPositionLabel = Label(positionlabelFrame, text="zPosition:  " + data)
  zPositionLabel.pack(side = TOP, anchor = 'w')

velocitylabelFrame = LabelFrame(rightFrame, text="Velocity Vectors")
velocitylabelFrame.pack(side = TOP, anchor = 'w')

elif (display_name == "xVelocity")
  xVelocityLabel = Label(velocitylabelFrame, text="xVelocity:  " + data)
  xVelocityLabel.pack(anchor = 'w')

elif (display_name == "yVelocity")
  yVelocityLabel = Label(velocitylabelFrame, text="yVelocity:  " + data)
  yVelocityLabel.pack(side = TOP, anchor = 'w')

elif (display_name == "zVelocity")
  zVelocityLabel = Label(velocitylabelFrame, text="zVelocity:  " + data)
  zVelocityLabel.pack(side = TOP, anchor = 'w')

spilabelFrame = LabelFrame(rightFrame, text="SPI")
spilabelFrame.pack(side = TOP, anchor = 'w')

elif (display_name == "spiSent")
  spiSentLabel = Label(spilabelFrame, text="spiSent:  " + data)
  spiSentLabel.pack(anchor = 'w')

elif (display_name == "spiDrpped")
  spiDroppedLabel = Label(spilabelFrame, text="spiDropped:  " + data)
  spiDroppedLabel.pack(side = TOP, anchor = 'w')



root.mainloop()

print("complete")

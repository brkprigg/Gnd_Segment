#Brooke Prigg


import re
import sys
import struct

if len(sys.argv) != 5:
  print ("Usage:  python data_displayer.py data_map.txt CDHStatus downlinked_file output_file")
  quit()

data_map_filename = sys.argv[1]
subsystem_name = sys.argv[2]
downlinked_filename = sys.argv[3]
output_filename = sys.argv[4]

from tkinter import *
from tkinter.ttk import *

root = Tk()


guiTitle = Label(root, text = "Sample GUI")
guiTitle.grid(row = 0, column = 0)

from datetime import datetime
zuluYear = datetime.utcnow().strftime("%Y")
zuluMonth = datetime.utcnow().strftime("%m")
zuluDay = datetime.utcnow().strftime("%d")
zuluHour = datetime.utcnow().strftime("%H")
zuluMinute = datetime.utcnow().strftime("%M")
zuluSecond = datetime.utcnow().strftime("%S")


zuluTime = Label(root, relief = GROOVE, text =  zuluDay + "/" + zuluMonth + "/" + zuluYear)
zuluTime.grid(row = 1, columnspan = 2)

zuluTime = Label(root, relief = GROOVE, text = zuluHour + ":" + zuluMinute + ":" + zuluSecond)
zuluTime.grid(row = 2, columnspan = 2)

leftFrame = Frame(root)
leftFrame.grid(row = 3, column = 0)

rightFrame = Frame(root)
rightFrame.grid(row = 3, column = 1)

handsFrame = Frame(root)
handsFrame.grid(row = 4, columnspan = 2)

satTimelabelFrame = LabelFrame(leftFrame, text="Satellite Time", height = 20, width = 100)
satTimelabelFrame.pack(anchor = 'w')

GPSlabelFrame = LabelFrame(leftFrame, text="GPS")
GPSlabelFrame.pack(side = TOP, anchor = 'w')

Random1labelFrame = LabelFrame(leftFrame, text="Random1")
Random1labelFrame.pack(side = TOP, anchor = 'w')

Random2labelFrame = LabelFrame(leftFrame, text="Random2")
Random2labelFrame.pack(side = TOP, anchor = 'w')

positionlabelFrame = LabelFrame(rightFrame, text="Position Vectors")
positionlabelFrame.pack(side = TOP, anchor = 'w')

velocitylabelFrame = LabelFrame(rightFrame, text="Velocity Vectors")
velocitylabelFrame.pack(side = TOP, anchor = 'w')

spilabelFrame = LabelFrame(rightFrame, text="SPI")
spilabelFrame.pack(side = TOP, anchor = 'w')

handsLabelFrame = LabelFrame(handsFrame, text="Health and Status")
handsLabelFrame.pack(side = LEFT, anchor = 'w')


labelTop = Label(root, text = "Example")

notebook = Notebook(root)
timeMemoryPane = Frame(notebook)
hotswapsPane = Frame(notebook)
tempSensorsPane = Frame(notebook)

notebook.add(timeMemoryPane, text = "Time CPU1, CPU 5, CPU 15, and Memory")
notebook.add(hotswapsPane, text = "Hotswaps 1 Through 32")
notebook.add(tempSensorsPane, text = "Temperature Sensors 1 Through 64")

tmFrameLeft = Frame(timeMemoryPane)
tmFrameLeft.pack(side = LEFT)

tmFrameCenter = Frame(timeMemoryPane)
tmFrameCenter.pack(side = LEFT)

tmFrameRight = Frame(timeMemoryPane)
tmFrameRight.pack(side = LEFT)

hsFrameLeft = Frame(hotswapsPane)
hsFrameLeft.pack(side = LEFT)

hsFrameCenter = Frame(hotswapsPane)
hsFrameCenter.pack(side = LEFT)

hsFrameRight = Frame(hotswapsPane)
hsFrameRight.pack(side = LEFT)

tsFrameLeft = Frame(tempSensorsPane)
tsFrameLeft.pack(side = LEFT)

tsFrameCenter = Frame(tempSensorsPane)
tsFrameCenter.pack(side = LEFT)

tsFrameCenter2 = Frame(tempSensorsPane)
tsFrameCenter2.pack(side = LEFT)

tsFrameRight = Frame(tempSensorsPane)
tsFrameRight.pack(side = LEFT)


notebook.grid(row = 3, column = 2)



def beacon_displayer():

  #Command Line: python beacon_displayer.py beacon_struct.txt BeaconStruct beacon.bin output_file


  def remove_line_whitespace(line_from_file):
    line_from_file = line_from_file.rstrip()
    line_from_file = line_from_file.lstrip('\t')
    line_from_file = line_from_file.lstrip(' ')
    return line_from_file

############################################################################################################

  if len(sys.argv) != 5:
    print ("Usage:  python data_displayer.py data_map.txt CDHStatus downlinked_file output_file")
    quit()

  data_map_filename = sys.argv[1]
  subsystem_name = sys.argv[2]
  downlinked_filename = sys.argv[3]
  output_filename = sys.argv[4]
  datatype = []
  names = []
  num_iterations = []
  tot_num_bytes = []
  data = dict()

  f = open(data_map_filename, 'r')



  # if (subsystem_name == "BeaconStruct"):
  #   tot_num_bytes = 103

  if (subsystem_name == "BeaconStruct"):
    downlink_file = open(downlinked_filename, 'rb')
    byte_str = open(downlinked_filename, 'rb')
    file_contents = byte_str.read()
    print ("size of file = " + (str)(len(file_contents)))

  j = 0
  header = '4b4530414141'
  while (j < len(file_contents) or output_str != header):
    beaconBodyHex = ''
    output_str = ''
    byteChunk = file_contents[j:j+6]
    output_str = output_str + ''.join('{:02x}'.format(x) for x in byteChunk)
    #print(output_str)
    if (header == output_str):
      bytes_in_line = 1
      parse_subsystem_lines = "false"
      with open(data_map_filename, 'r') as f:
        tok = 0
        for line_from_file in f:
          line = remove_line_whitespace(line_from_file)
          if (subsystem_name == line):
            print ("Found subsystem", subsystem_name)
            parse_subsystem_lines = "true"
            continue

          if (parse_subsystem_lines == "true"):
            tokens = re.split(" ", line)
            if (len(tokens) == 1):
              parse_subsystem_lines = "false"
            else:
              datatype.append(tokens[0])
              #print ("datatype found:", tokens[0])
              #print ("name found:", tokens[1])
              if "[" in tokens[1] and "]" in tokens[1]:
                num_iterations = num_iterations + ['']
                for c in tokens[1]:
                  if c.isdigit():
                    num_iterations[tok]=num_iterations[tok]+c
                square_bracket_location = tokens[1].index('[');
                if (square_bracket_location > 0):
                  tokens[1] = tokens[1][0:square_bracket_location]
              else:
                num_iterations = num_iterations + ['1']

              names.append(tokens[1])
              tok = tok + 1

      if subsystem_name == "CDHStatus":
        tot_num_bytes = 404
      elif subsystem_name == "BeaconStruct":
        tot_num_bytes = 103
      elif subsystem_name == "ACSStatus":
        tot_num_bytes = 32
      elif subsystem_name == "PLDStatus":
        tot_num_bytes = 12
      elif subsystem_name == "EPSStatus":
        tot_num_bytes = 40
      elif subsystem_name == "ACSConfig":
        tot_num_bytes = 4
      elif subsystem_name == "CDHConfig":
        tot_num_bytes = 4
      elif subsystem_name == "CMDConfig":
        tot_num_bytes = 20
      elif subsystem_name == "COMConfig":
        tot_num_bytes = 4
      elif subsystem_name == "EPSConfig":
        tot_num_bytes = 6
      elif subsystem_name == "FMGConfig":
        tot_num_bytes = 4
      elif subsystem_name == "PLDConfig":
        tot_num_bytes = 4
      elif subsystem_name == "SCHItem":
        tot_num_bytes = 34


  #    print ("Total Number of Bits in Subsystem:" + str(tot_num_bytes))
      num_iterations = [int(n) for n in num_iterations]
#      print ("Number of Iterations:" + str(num_iterations))
      #print(j)
      beaconBodyNoneHex = file_contents[j+6:j+91]
      beaconBodyHex = beaconBodyHex + ''.join('{:02x}'.format(x) for x in beaconBodyNoneHex)

      #print(beaconBodyHex)

      number_of_elements = len(datatype)
      i = 0
      start_byte = j+6
      while (i < number_of_elements):
        data = dict()
        label = dict()
        if ((datatype[i] == "int8") or (datatype[i] == "uint8")):
          num_bytes = 1
        elif ((datatype[i] == "int16") or (datatype[i] == "uint16")):
          num_bytes = 2
        elif ((datatype[i] == "int32") or (datatype[i] == "uint32") or (datatype[i] == "float")):
          num_bytes = 4
        elif (datatype[i] == "double"):
          num_bytes = 8
        else:
          print ("Unknown datatype:  " + datatype[i])
          continue;
     # print (tot_num_bytes)
   #   print ("Start byte is ", (str)(start_byte), " and end_byte is " , (str)(end_byte-1))

        j=0
        while j<num_iterations[i]:
          end_byte = start_byte + num_bytes
          byte_str = file_contents[start_byte:end_byte]
          display_name = ''
          if num_iterations[i]==1:
            display_name = names[i]
          else:
            display_name = names[i] + '[' + str(j) + ']'
          if (datatype[i] == "uint8"):
            unsigned_integer_val = struct.unpack('>B', byte_str)
            print ("Field", display_name, "of type", datatype[i], "has a value of", (str)(unsigned_integer_val[0]))
            data = unsigned_integer_val[0]
          elif (datatype[i] == "int8"):
            signed_integer_val = struct.unpack('>b', byte_str)
            print ("Field", display_name, "of type", datatype[i], "has a value of", (str)(signed_integer_val[0]))
            data = signed_integer_val[0]
          elif (datatype[i] == "int16"):
            signed_integer_val = struct.unpack('>h', byte_str)
            print ("Field", display_name, "of type", datatype[i], "has a value of", (str)(signed_integer_val[0]))
            data = signed_integer_val[0]
          elif (datatype[i] == "uint16"):
            unsigned_integer_val = struct.unpack('>H', byte_str)
            print ("Field", display_name, "of type", datatype[i], "has a value of", (str)(unsigned_integer_val[0]))
            data = unsigned_integer_val[0]
          elif (datatype[i] == "uint32"):
            unsigned_integer_val = struct.unpack('>I', byte_str)
            print ("Field", display_name, "of type", datatype[i], "has a value of", (str)(unsigned_integer_val[0]))
            data = unsigned_integer_val[0]
          elif (datatype[i] == "int32"):
            signed_integer_val = struct.unpack('>i', byte_str)
            print ("Field", display_name, "of type", datatype[i], "has a value of", (str)(signed_integer_val[0]))
            data = signed_integer_val[0]
          elif (datatype[i] == "float"):
            float_val = struct.unpack('>f', byte_str)
            print ("Field", display_name, "of type", datatype[i], "has a value of", (str)(float_val[0]))
            data = float_val[0]
          elif (datatype[i] == "double"):
            double_val = struct.unpack('>d', byte_str)
            print ("Field", display_name, "of type", datatype[i], "has a value of", (str)(double_val[0]))
            data = double_val[0]

          j=j+1
          start_byte = end_byte
          #export data to GUI
#################################################################################################################

          if (display_name == "satTime"):
            satTimeLabel = Label(satTimelabelFrame, text="satTime:  " + str(data))
            satTimeLabel.pack(anchor = 'w')

          elif (display_name == "GPSWeek"):
            GPSWeekLabel = Label(GPSlabelFrame, text="GPSWeek:  " + str(data))
            GPSWeekLabel.pack(anchor = 'w')

          elif (display_name == "GPSSec"):
            GPSSecLabel = Label(GPSlabelFrame, text="GPSSec:  " + str(data))
            GPSSecLabel.pack(side = TOP, anchor = 'w')

          elif (display_name == "systemMode"):
            systemModeLabel = Label(Random1labelFrame, text="systemMode:  " + str(data))
            systemModeLabel.pack(anchor = 'w')

          elif (display_name == "subpowerStates"):
            subpowerStatesLabel = Label(Random1labelFrame, text="subpowerStates:  " + str(data))
            subpowerStatesLabel.pack(side = TOP, anchor = 'w')

          elif (display_name == "epochNumber"):
            epochNumberLabel = Label(Random1labelFrame, text="epochNumber:  " + str(data))
            epochNumberLabel.pack(side = TOP, anchor = 'w')

          elif (display_name == "radNumber"):
            radNumberLabel = Label(Random1labelFrame, text="radNumber:  " + str(data))
            radNumberLabel.pack(side = TOP, anchor = 'w')

          elif (display_name == "batteryCap"):
            batteryCapLabel = Label(Random2labelFrame, text="batteryCap:  " + str(data))
            batteryCapLabel.pack(anchor = 'w')

          elif (display_name == "acsMode"):
            acsModeLabel = Label(Random2labelFrame, text="acsMode:  " + str(data))
            acsModeLabel.pack(side = TOP, anchor = 'w')

          elif (display_name == "memory"):
            memoryLabel = Label(Random2labelFrame, text="memory:  " + str(data))
            memoryLabel.pack(side = TOP, anchor = 'w')

          elif (display_name == "cpu15"):
            cpu15Label = Label(Random2labelFrame, text="cpu15:  " + str(data))
            cpu15Label.pack(side = TOP, anchor = 'w')

          elif (display_name == "xPosition"):
            xPositionLabel = Label(positionlabelFrame, text="xPosition:  " + str(data))
            xPositionLabel.pack(anchor = 'w')

          elif (display_name == "yPosition"):
            yPositionLabel = Label(positionlabelFrame, text="yPosition:  " + str(data))
            yPositionLabel.pack(side = TOP, anchor = 'w')

          elif (display_name == "zPosition"):
            zPositionLabel = Label(positionlabelFrame, text="zPosition:  " + str(data))
            zPositionLabel.pack(side = TOP, anchor = 'w')

          elif (display_name == "xVelocity"):
            xVelocityLabel = Label(velocitylabelFrame, text="xVelocity:  " + str(data))
            xVelocityLabel.pack(anchor = 'w')

          elif (display_name == "yVelocity"):
            yVelocityLabel = Label(velocitylabelFrame, text="yVelocity:  " + str(data))
            yVelocityLabel.pack(side = TOP, anchor = 'w')

          elif (display_name == "zVelocity"):
            zVelocityLabel = Label(velocitylabelFrame, text="zVelocity:  " + str(data))
            zVelocityLabel.pack(side = TOP, anchor = 'w')

          elif (display_name == "spiSent"):
            spiSentLabel = Label(spilabelFrame, text="spiSent:  " + str(data))
            spiSentLabel.pack(anchor = 'w')

          elif (display_name == "spiDrpped"):
            spiDroppedLabel = Label(spilabelFrame, text="spiDropped:  " + str(data))
            spiDroppedLabel.pack(side = TOP, anchor = 'w')

        i = i + 1
      break;
    j = j + 1
#Buttons that request verbose Health and Status

print ("Done")

##################################################################################################################



def OnClick ():
  newsubsytemName = subsystemEntry.get()
  print (newsubsytemName)
  if (newsubsytemName == "CDHStatus"):
    data_displayer()

def data_displayer():

  data_map_filename = "Struct.txt"
  subsystem_name = "CDHStatus"
  downlinked_filename = "CDH_test_data.bin"
  output_filename = "output_file"


  def remove_line_whitespace(line_from_file):
    line_from_file = line_from_file.rstrip()
    line_from_file = line_from_file.lstrip('\t')
    line_from_file = line_from_file.lstrip(' ')
    return line_from_file

  def byte_calculator_no_print ():
    number_of_elements = len(datatype)
    i = 0
    start_byte = 0
    cal_num_bytes = 0
    while (i < number_of_elements):
      if (datatype[i] == "uint8"):
        num_bytes = 1
      elif (datatype[i] == "uint16"):
        num_bytes = 2
      elif ((datatype[i] == "int32") or (datatype[i] == "uint32") or (datatype[i] == "float")):
        num_bytes = 4
      elif (datatype[i] == "double"):
        num_bytes = 8
      else:
        print ("Unknown datatype:  " + datatype[i])
        continue;
     # print (tot_num_bytes)
     # print ("Start byte is ", (str)(start_byte), " and end_byte is " , (str)(end_byte-1))

      j=0
      while j<num_iterations[i]:
        end_byte = start_byte + num_bytes
        byte_str = file_contents[start_byte:end_byte]
        display_name = ''
        if num_iterations[i]==1:
          display_name = names[i]
        else:
          display_name = names[i] + '[' + str(j) + ']'
        if (datatype[i] == "uint8"):
          unsigned_integer_val = struct.unpack('>B', byte_str)
        elif (datatype[i] == "uint16"):
          unsigned_integer_val = struct.unpack('>H', byte_str)
        elif (datatype[i] == "uint32"):
          unsigned_integer_val = struct.unpack('>I', byte_str)
        elif (datatype[i] == "int32"):
          signed_integer_val = struct.unpack('>i', byte_str)
        elif (datatype[i] == "float"):
          float_val = struct.unpack('>f', byte_str)
        elif (datatype[i] == "double"):
          double_val = struct.unpack('>d', byte_str)
        j=j+1
        start_byte = end_byte
        cal_num_bytes = cal_num_bytes + (num_bytes)
      i = i + 1
    return cal_num_bytes

  # if len(sys.argv) != 5:
  #   print ("Usage:  python data_displayer.py data_map.txt CDHStatus downlinked_file output_file")
  #   quit()
  #
  # data_map_filename = sys.argv[1]
  # subsystem_name = sys.argv[2]
  # downlinked_filename = sys.argv[3]
  # output_filename = sys.argv[4]
  datatype = []
  names = []
  num_iterations = []

  f = open(data_map_filename, 'r')

  bytes_in_line = 1

  parse_subsystem_lines = "false"
  with open(data_map_filename, 'r') as f:
    tok = 0
    for line_from_file in f:
      line = remove_line_whitespace(line_from_file)
      if (subsystem_name == line):
        print ("Found subsystem", subsystem_name)
        parse_subsystem_lines = "true"
        continue

      if (parse_subsystem_lines == "true"):
        tokens = re.split(" ", line)
        if (len(tokens) == 1):
          parse_subsystem_lines = "false"
        else:
          datatype.append(tokens[0])
          # print ("datatype found:", tokens[0])
          # print ("name found:", tokens[1])
          if "[" in tokens[1] and "]" in tokens[1]:
            num_iterations = num_iterations + ['']
            for c in tokens[1]:
              if c.isdigit():
                num_iterations[tok]=num_iterations[tok]+c
            square_bracket_location = tokens[1].index('[');
            if (square_bracket_location > 0):
              tokens[1] = tokens[1][0:square_bracket_location]
          else:
            num_iterations = num_iterations + ['1']

          names.append(tokens[1])
          tok = tok + 1

  if subsystem_name == "CDHStatus":
    tot_num_bytes = 404
  elif subsystem_name == "ACSStatus":
    tot_num_bytes = 32
  elif subsystem_name == "PLDStatus":
    tot_num_bytes = 12
  elif subsystem_name == "EPSStatus":
    tot_num_bytes = 40
  elif subsystem_name == "ACSConfig":
    tot_num_bytes = 4
  elif subsystem_name == "CDHConfig":
    tot_num_bytes = 4
  elif subsystem_name == "CMDConfig":
    tot_num_bytes = 20
  elif subsystem_name == "COMConfig":
    tot_num_bytes = 4
  elif subsystem_name == "EPSConfig":
    tot_num_bytes = 6
  elif subsystem_name == "FMGConfig":
    tot_num_bytes = 4
  elif subsystem_name == "PLDConfig":
    tot_num_bytes = 4
  elif subsystem_name == "SCHItem":
    tot_num_bytes = 34



  num_iterations = [int(n) for n in num_iterations]
  #print (num_iterations)


  downlink_file = open(downlinked_filename, 'rb')
  file_contents = downlink_file.read()
  #print ("size of file = " + (str)(len(file_contents)))

  cal_num_bytes = str(byte_calculator_no_print())

  if len(file_contents) % tot_num_bytes == 0 and len(file_contents) % int(cal_num_bytes) == 0:
    print ("Good Data Map")
    number_of_elements = len(datatype)
    i = 0
    start_byte = 0
    while (i < number_of_elements):
      if (datatype[i] == "uint8"):
        num_bytes = 1
      elif (datatype[i] == "uint16"):
        num_bytes = 2
      elif ((datatype[i] == "int32") or (datatype[i] == "uint32") or (datatype[i] == "float")):
        num_bytes = 4
      elif (datatype[i] == "double"):
        num_bytes = 8
      else:
        print ("Unknown datatype:  " + datatype[i])
        continue;
   # print (tot_num_bytes)
   # print ("Start byte is ", (str)(start_byte), " and end_byte is " , (str)(end_byte-1))

      j=0
      while j<num_iterations[i]:
        end_byte = start_byte + num_bytes
        byte_str = file_contents[start_byte:end_byte]
        display_name = ''
        if num_iterations[i]==1:
          display_name = names[i]
        else:
          display_name = names[i] + '[' + str(j) + ']'
        if (datatype[i] == "uint8"):
          unsigned_integer_val = struct.unpack('>B', byte_str)
          print ("Field", display_name, "of type", datatype[i], "has a value of", (str)(unsigned_integer_val[0]))
          data = unsigned_integer_val[0]
        elif (datatype[i] == "uint16"):
          unsigned_integer_val = struct.unpack('>H', byte_str)
          print ("Field", display_name, "of type", datatype[i], "has a value of", (str)(unsigned_integer_val[0]))
          data = unsigned_integer_val[0]
        elif (datatype[i] == "uint32"):
          unsigned_integer_val = struct.unpack('>I', byte_str)
          print ("Field", display_name, "of type", datatype[i], "has a value of", (str)(unsigned_integer_val[0]))
          data = unsigned_integer_val[0]
        elif (datatype[i] == "int32"):
          signed_integer_val = struct.unpack('>i', byte_str)
          print ("Field", display_name, "of type", datatype[i], "has a value of", (str)(signed_integer_val[0]))
          data = signed_integer_val[0]
        elif (datatype[i] == "float"):
          float_val = struct.unpack('>f', byte_str)
          print ("Field", display_name, "of type", datatype[i], "has a value of", (str)(float_val[0]))
          data = float_val[0]
        elif (datatype[i] == "double"):
          double_val = struct.unpack('>d', byte_str)
          print ("Field", display_name, "of type", datatype[i], "has a value of", (str)(double_val[0]))
          data = double_val[0]



        if (display_name == "time"):
          satTimeLabel = Label(timeMemoryPane, text="Time:  " + str(data))
          satTimeLabel.pack(anchor = 'w')

        elif (display_name == "cpu1"):
          GPSWeekLabel = Label(timeMemoryPane, text="CPU 1:  " + str(data))
          GPSWeekLabel.pack(anchor = 'w')

        elif (display_name == "cpu5"):
          GPSSecLabel = Label(timeMemoryPane, text="CPU 5:  " + str(data))
          GPSSecLabel.pack(side = TOP, anchor = 'w')

        elif (display_name == "cpu15"):
          systemModeLabel = Label(timeMemoryPane, text="CPU 15:  " + str(data))
          systemModeLabel.pack(anchor = 'w')

        elif (display_name == "memory"):
          subpowerStatesLabel = Label(timeMemoryPane, text="Memory:  " + str(data))
          subpowerStatesLabel.pack(side = TOP, anchor = 'w')

        elif (display_name == "hotswaps[" + str(j) + "]"):
          if (j < 20):
            epochNumberLabel = Label(hsFrameLeft, text="Hotswaps[" + str(j) + "]:  " + str(data))
            epochNumberLabel.pack(side = TOP, anchor = 'w')
          elif (20 <= j < 40):
            epochNumberLabel = Label(hsFrameCenter, text="Hotswaps[" + str(j) + "]:  " + str(data))
            epochNumberLabel.pack(side = TOP, anchor = 'w')

        elif (display_name == "tempSensors[" + str(j) + "]"):
          if (j < 20):
            epochNumberLabel = Label(tsFrameLeft, text="Temperature of Sensor[" + str(j) + "]:  " + str(data))
            epochNumberLabel.pack(side = TOP, anchor = 'w')
          elif (20 <= j < 40):
            epochNumberLabel = Label(tsFrameCenter, text="Temperature of Sensor[" + str(j) + "]:  " + str(data))
            epochNumberLabel.pack(side = TOP, anchor = 'w')
          elif (40 <= j < 60):
            epochNumberLabel = Label(tsFrameCenter2, text="Temperature of Sensor[" + str(j) + "]:  " + str(data))
            epochNumberLabel.pack(side = TOP, anchor = 'w')
          elif (60 <= j):
            epochNumberLabel = Label(tsFrameRight, text="Temperature of Sensor[" + str(j) + "]:  " + str(data))
            epochNumberLabel.pack(side = TOP, anchor = 'w')


        j=j+1
        start_byte = end_byte
      i = i + 1

  else:
    remander = len(file_contents) % int(cal_num_bytes)
    print(" Check Dat Map, Byte Remander:  " + str(remander))






newsubsytemName = ''

if (subsystem_name == 'BeaconStruct'):
  beacon_displayer()


requestHandSButton = Button(handsLabelFrame, text = 'Request Health and Status', command = OnClick)
requestHandSButton.grid(row = 0, column = 0)


declineHandSButton = Button(handsLabelFrame, text = 'Decline Health and Status')
declineHandSButton.grid(row = 0, column = 1)

subsystemEntry = Entry(handsLabelFrame)
subsystemEntry.grid(row = 1, column = 0)


root.mainloop()

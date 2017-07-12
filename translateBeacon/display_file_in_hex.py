# Command line:  python display_file_in_hex.py downlinked_file
import re
import sys
import struct

def remove_line_whitespace(line_from_file):
  line_from_file = line_from_file.rstrip()
  line_from_file = line_from_file.lstrip('\t')
  line_from_file = line_from_file.lstrip(' ')
  return line_from_file

if len(sys.argv) != 2:
  print ("Usage:  python display_file_in_hex.py downlinked_file")
  quit()

downlinked_filename = sys.argv[1]
#output_filename = sys.argv[2]
datatype = []
names = []
num_iterations = []

bytes_in_line = 1




byte_str = open(downlinked_filename, 'rb')
file_contents = byte_str.read()
print ("size of file = " + (str)(len(file_contents)))

i = 0
while i<len(file_contents):
  byte_str = file_contents[i:i+10]
  j = 0
  output_str = ''
  if i<10:
    output_str = str(i) + '     '
  elif i<100:
    output_str = str(i) + '    '
  elif i<1000:
    output_str = str(i) + '   '


  while j < len(byte_str):
    single_byte = byte_str[j:j+1]
    output_str = output_str + ''.join('{:02x}'.format(x) for x in single_byte) + ' '
#    print (''.join('{:02x}'.format(x) for x in single_byte), ' ')
    j = j + 1
  print (output_str)
  i=i+10



#number_of_elements = len(datatype)
#i = 0
#start_byte = 0
#while (i < number_of_elements):
#  if (datatype[i] == "uint8"):
#    num_bytes = 1
#  elif (datatype[i] == "uint16"):
#    num_bytes = 2
#  elif ((datatype[i] == "int32") or (datatype[i] == "uint32") or (datatype[i] == "float")):
#    num_bytes = 4
#  elif (datatype[i] == "double"):
#    num_bytes = 8
#  else:
#    print ("Unknown datatype:  " + datatype[i])
#    continue;




#  print ("Start byte is ", (str)(start_byte), " and end byte is " , (str)(end_byte-1))

#  j=0
#  while j<num_iterations[i]:
#    end_byte = start_byte + num_bytes
#    byte_str = file_contents[start_byte:end_byte]
#    if (datatype[i] == "uint8"):
#      unsigned_integer_val = struct.unpack('>B', byte_str)
#      print ("Field", names[i], "of type", datatype[i], "has a value of", (str)(unsigned_integer_val[0]))
#    elif (datatype[i] == "uint16"):
#      unsigned_integer_val = struct.unpack('>H', byte_str)
#      print ("Field", names[i], "of type", datatype[i], "has a value of", (str)(unsigned_integer_val[0]))
#    elif (datatype[i] == "uint32"):
#      unsigned_integer_val = struct.unpack('>I', byte_str)
#      print ("Field", names[i], "of type", datatype[i], "has a value of", (str)(unsigned_integer_val[0]))
#    elif (datatype[i] == "int32"):
#      signed_integer_val = struct.unpack('>i', byte_str)
#      print ("Field", names[i], "of type", datatype[i], "has a value of", (str)(signed_integer_val[0]))
#    elif (datatype[i] == "float"):
#      float_val = struct.unpack('>f', byte_str)
#      print ("Field", names[i], "of type", datatype[i], "has a value of", (str)(float_val[0]))
#    elif (datatype[i] == "double"):
#      double_val = struct.unpack('>d', byte_str)
#      print ("Field", names[i], "of type", datatype[i], "has a value of", (str)(double_val[0]))
#    j=j+1
#    start_byte = end_byte
#  i = i + 1

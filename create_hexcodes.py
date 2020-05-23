import numpy as np
import json
import re
result_binary = '0'
result_binary = result_binary.rjust(32, '0')
with open('C:/Users/Souvick/Desktop/opcode.json') as f:
    data = json.load(f)
while (1):
    command_input = input("Enter: ")
    command = re.split(',\\ |\\ ',command_input)
    if (len(command) is 3):
        opcode = command[0]
        RS = command[1]
        Destination = command[2]
        type_of_opcode = 2

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
    elif (len(command) is 4):
        opcode = command[0]
        RS1 = command[1]
        RS2 = command[2]
        Destination = command[3]
        type_of_opcode = 1
    if (opcode in ['ADD', 'SUB', 'AND', 'OR', 'SLT', 'MUL']):
        temp_RS1 = RS1
        RS1 = RS2
        RS2 = Destination
        Destination = temp_RS1
    elif (opcode in ['ADDI', 'SUBI', 'SLTI']):
        temp_RS1 = RS1
        RS1 = RS2
        RS2 = temp_RS1
    elif (opcode in ['LW']):
        temp_destination = Destination
        temp_RS1 = RS1
        Destination = RS2
        RS1 = temp_destination
        RS2 = temp_RS1
    elif (opcode in ['SW']):
        temp_destination = Destination
        temp_RS1 = RS1
        RS1 = Destination
        Destination = RS2
        RS2 = temp_RS1
    else:
        if (opcode not in ['BNEQZ', 'BEQZ']):
            print("Wrong opcode..")
            continue
    
    result_binary = data[opcode] + result_binary[6:]
    if (type_of_opcode is 2):
        RS = RS[1:]
        RS = "{0:b}".format(int(RS))
        if (len(RS) < 5):
            while(len(RS) != 5):
                RS = '0' + RS
        result_binary = result_binary[:6] + RS + result_binary[11:]
        result_binary = result_binary[:16] + np.binary_repr(int(Destination), width=16)
    if (type_of_opcode is 1):
        RS1 = RS1[1:]
        RS1 = "{0:b}".format(int(RS1))
        if (len(RS1) < 5):
            while(len(RS1) != 5):
                RS1 = '0' + RS1
        result_binary = result_binary[:6] + RS1 + result_binary[11:]
        RS2 = RS2[1:]
        RS2 = "{0:b}".format(int(RS2))
        if (len(RS2) < 5):
            while(len(RS2) != 5):
                RS2 = '0' + RS2
        result_binary = result_binary[:11] + RS2 + result_binary[16:]
        if (Destination[0] is 'R'):
            Destination = Destination[1:]
            Destination = "{0:b}".format(int(Destination))
            if (len(Destination) < 5):
                while(len(Destination) != 5):
                    Destination = '0' + Destination
            result_binary = result_binary[:16] + Destination + result_binary[21:]
        elif (Destination[0] is not 'R'):
            result_binary = result_binary[:16] + np.binary_repr(int(Destination), width=16)
     

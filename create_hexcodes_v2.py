import numpy as np                                              # Need to the conversion among different number bases - 10, 2, 16
import json                                                     # Need to read and access the Json file, where the opcodes are written
import re                                                       # Need to split the input string in different meaningful segments
result_binary = '0'                                             # Initializing the 32 bit string 
result_binary = result_binary.rjust(32, '0')                    # Padding zeros to all 32 places
with open('C:/Users/Souvick/Desktop/opcode.json') as f:
    data = json.load(f)                                         # Reading the Json file
while (1):                                                      # This loop will go on forever
    command_input = input("Enter: ")                            # Asking user to input the string
    command = re.split(',\\ |\\ |\\(',command_input)            # Split the srting by commas, space and brackets
    if (len(command) is 3):                                     # For BEQZ and BNEQZ commands
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
        RS1, RS2, Destination = RS2, Destination, RS1
    elif (opcode in ['ADDI', 'SUBI', 'SLTI']):
        RS1, RS2 = RS2, RS1
    elif (opcode in ['LW', 'SW']):
        if (')' in Destination):
            Destination = Destination[:-1]
        RS1, RS2, Destination = Destination, RS1, RS2
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

    print (result_binary)
    result_hex = hex(int(result_binary, 2))
    result_hex = result_hex[2:]
    if (len(result_hex) in [7, 6]):
        while (len(result_hex) != 8):
            result_hex = '0' + result_hex
    result_hex = "32'h" + result_hex
    print (result_hex)
    result_binary = '0'
    result_binary = result_binary.rjust(32, '0')
            
    

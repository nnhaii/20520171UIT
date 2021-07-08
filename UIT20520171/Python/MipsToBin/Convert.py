from os import name
import re

'''
    Nguyen Nam Hai MSSV 20520171

    Tạo 4 file:
        1 file asm:                  mips.asm
        1 file chuẩn hóa:            Assembler.txt
        1 file xuất ra theo binary:  Assembled_Bina.txt
        1 file xuất ra theo hexa:    Assembled_Hexa.txt
'''


#   Tạo bảng băm chưa các opcode, reg, function, Label, Format

opcode = {
    'add':      '000000',
    'addi':     '001000',
    'addiu':    '001001',
    'addu':     '000000',
    'and':      '000000',
    'andi':     '001100',
    'beq':      '000100',
    'bne':      '000101',
    'j':        '000010',
    'jal':      '000011',
    'jr':       '000000',
    'lbu':      '100100',
    'lhu':      '100101',
    'll':       '110000',
    'lui':      '001111',
    'lw':       '100011',
    'nor':      '000000',
    'or':       '000000',
    'ori':      '001101',
    'slt':      '000000',
    'slti':     '001010',
    'sltiu':    '001011',
    'sltu':     '000000',
    'sll':      '000000',
    'srl':      '000000',
    'sb':       '101000',
    'sc': 		 '111000',
    'sh': 		 '101001',
    'sw': 		 '101011',
    'sub': 		 '000000',
    'subu': 	 '000000',

    # Bổ sung thêm lb, sb, lh
    'lb': 		 '100000',
    'sb': 		 '101000',
    'lh':   	 '100001'
}

reg = {
    '$zero': '00000', '$0': '00000',
    '$at': '00001', '$1': '00001',
    '$v0': '00010', '$2': '00010',
    '$v1': '00011', '$3': '00011',
    '$a0': '00100', '$4': '00100',
    '$a1': '00101', '$5': '00101',
    '$a2': '00110', '$6': '00110',
    '$a3': '00111', '$7': '00111',
    '$t0': '01000', '$8': '01000',
    '$t1': '01001', '$9': '01001',
    '$t2': '01010', '$10': '01010',
    '$t3': '01011', '$11': '01011',
    '$t4': '01100', '$12': '01100',
    '$t5': '01101', '$13': '01101',
    '$t6': '01110', '$14': '01110',
    '$t7': '01111', '$15': '01111',
    '$s0': '10000', '$16': '10000',
    '$s1': '10001', '$17': '10001',
    '$s2': '10010', '$18': '10010',
    '$s3': '10011', '$19': '10011',
    '$s4': '10100', '$20': '10100',
    '$s5': '10101', '$21': '10101',
    '$s6': '10110', '$22': '10110',
    '$s7': '10111', '$23': '10111',
    '$t8': '11000', '$24': '11000',
    '$t9': '11001', '$25': '11001',
    '$k0': '11010', '$26': '11010',
    '$k1': '11011', '$27': '11011',
    '$gp': '11100', '$28': '11100',
    '$sp': '11101', '$29': '11101',
    '$fp': '11110', '$30': '11110',
    '$ra': '11111', '$31': '11111',
}

funct = {
    'add': 	'100000',
    'addu': '100001',
    'and': 	'100100',
    'jr': 	'001000',
    'nor': 	'100111',
    'or': 	'100101',
    'slt': 	'101010',
    'sltu': '101011',
    'sll': 	'000000',
    'srl': 	'000010',
    'sub': 	'100010',
    'subu': '100011'
}

Format = {
    'add': 		'R',
    'addi': 	'I',
    'addiu': 	'I',
    'addu': 	'R',
    'and': 		'R',
    'andi': 	'I',
    'beq': 		'I',
    'bne': 		'I',
    'j': 		'J',
    'jal': 		'J',
    'jr': 		'R',
    'lbu': 		'I',
    'lhu': 		'I',
    'll': 		'I',
    'lui': 		'I',
    'lw': 		'I',
    'nor': 		'R',
    'or': 		'R',
    'ori': 		'I',
    'slt': 		'R',
    'slti': 	'I',
    'sltiu':	'I',
    'sltu': 	'R',
    'sll': 		'R',
    'srl': 		'R',
    'sb': 		'I',
    'sc': 		'I',
    'sh': 		'I',
    'sw': 		'I',
    'sub': 		'R',
    'subu': 	'R',

    # Bổ sung thêm lb, sb, lh
    'lb':       'I',
    'sb':       'I',
    'lh':       'I'
}

Label = {}


# Đọc từ 1 file mips.asm ----------------
fileMIPS = open('mips.asm', 'r')
fileA = open('Assembler.txt', 'w')

value_Label = 0

for i in fileMIPS.readlines():

    match = 0
    match = i.count('#')
    if match > 0:
        Count = 0
        for d in i:
            if i[Count] != '#':
                Count += 1
        i = i[:Count] + '\n'

# Dùng xóa khoảng trắng thừa ở đầu dòng lệnh
    i = re.sub(r'\B[ ]', '', i)
    i = re.sub(r'\B[\t]', '', i)

    match = 0
    match = i.count(':')

    if match > 0:        # Tìm thấy Label

        # Tìm Label -------------------------
        Count = 0
        key_Label = ''

        while i[Count] != ':':
            key_Label += i[Count]
            Count += 1
        i = re.sub(':', '', i)
        key_Label = re.sub('/t', '', key_Label)
        key_Label = re.sub('/n', '', key_Label)
        key_Label = re.sub(' ', '', key_Label)
    # Thêm label vào Hash và xóa Label ---
        if i == key_Label + '\n':
            Label[key_Label] = value_Label
            continue
        else:
            Label[key_Label] = value_Label
            i = re.sub(key_Label, '', i)
            i = re.sub(r'\B[ ]', '', i)

    # Ghi ra file Assembler.txt ----------
    b = 0
    b = i.count('.')
    if i != '' + '\n' and b == 0:
        fileA.write(i)
        value_Label += 4

fileMIPS.close()
fileA.close()
print(Label)


fileA = open('Assembler.txt', 'r')
fileH = open('Assembled_Hexa.txt', 'w')
fileB = open('Assembled_Bina.txt', 'w')
pc = 0

for i in fileA.readlines():
    Count = 0
    key_Opcode = ''
    while i[Count] != ' ':
        key_Opcode += i[Count]
        Count += 1
    i = re.sub(key_Opcode, '', i)
    i = re.sub(' ', '', i)
    j = ''
    match = i.count('(')   # Đếm số lượng ngoặc xuất hiện trong lệnh

    # Định dạng lệnh R type
    if Format[key_Opcode] == 'R':
        if (key_Opcode == 'sll' or key_Opcode == 'srl'):
            rs = '00000'
            Count = 0
            rd = ''
            while i[Count] != ',':
                rd += i[Count]
                Count += 1
            Count += 1
            i = re.sub(rd, '', i)
            i = re.sub(' ', '', i)

            rt = ''
            while i[Count] != ',':
                rt += i[Count]
                Count += 1
            Count += 1

            shamt = i[Count:]

            # Chuyển trường shamt sang nhị phân
            shamt = int(shamt)
            shamt = str(bin(shamt))
            shamt = re.sub('b', '', shamt)
            shamt = re.sub(r'\b[0]', '', shamt)
            n = 5 - len(shamt)
            for k in range(0, n):
                shamt = shamt[:0] + '0' + shamt[0:]
            j += opcode[key_Opcode]+rs+reg[rt]+reg[rd]+shamt+funct[key_Opcode]

        elif key_Opcode == "jr":
            rs = i
            rs = re.sub('\n', '', rs)
            rs = re.sub('\t', '', rs)
            rt = '00000'
            rd = '00000'
            shamt = '00000'
            j += opcode[key_Opcode]+reg[rs]+rt+rd+shamt+funct[key_Opcode]
        else:
            shamt = '00000'
            Count = 0
            rd = ''
            while i[Count] != ',':
                rd += i[Count]
                Count += 1
            Count += 1
            i = re.sub(rd, '', i)
            i = re.sub(' ', '', i)

            rs = ''
            while i[Count] != ',':
                rs += i[Count]
                Count += 1
            Count += 1

            rt = i[Count:]
            rt = re.sub('\n', '', rt)
            rt = re.sub('\t', '', rt)
            j += opcode[key_Opcode]+reg[rs]+reg[rt]+reg[rd]
            j += shamt+funct[key_Opcode]

    # Định dạng lệnh J type
    elif Format[key_Opcode] == 'J':
        if key_Opcode == 'j' or key_Opcode == 'jal':
            key_Label = i
            key_Label = re.sub('\n', '', key_Label)
            key_Label = re.sub('\t', '', key_Label)

            address = Label[key_Label]
            address += 4194304
            bin26 = lambda x:''.join(reversed([str((x >> i) & 1) for i in range(26)]))
            address = bin26(address)
            j += opcode[key_Opcode] + address

    # Định dạng lệnh I type
    else:
        if key_Opcode == 'lui':
            Count = 0
            rs = '00000'
            rt = ''
            while i[Count] != ',':
                rt += i[Count]
                Count += 1
            Count += 1
            i = re.sub(rt, '', i)
            i = re.sub(' ', '', i)

            number = i[Count:]
            number = re.sub('\n', '', number)
            number = re.sub('\t', '', number)

            immediate = int(number)
            bin16 = lambda x:''.join(reversed([str((x >> i) & 1)for i in range(16)]))
            immediate = bin16(immediate)
            j += opcode[key_Opcode] + rs + reg[rt] + immediate

        elif key_Opcode == 'beq' or key_Opcode == 'bne':
            Count = 0
            rs = ''
            while i[Count] != ',':
                rs += i[Count]
                Count += 1
            Count += 1
            i = re.sub(rs, '', i)
            i = re.sub(' ', '', i)

            rt = ''
            while i[Count] != ',':
                rt += i[Count]
                Count += 1
            Count += 1

            key_Label = i[Count:]
            key_Label = re.sub('\n', '', key_Label)
            key_Label = re.sub('\t', '', key_Label)

            immediate = Label[key_Label]
            bin16 = lambda x:''.join(reversed([str((x >> i) & 1) for i in range(16)]))
            immediate = bin16(immediate)
            j += opcode[key_Opcode] + reg[rs] + reg[rt] + immediate

        elif key_Opcode == 'ori' or key_Opcode == 'andi':
            Count = 0
            rt = ''
            while i[Count] != ',':
                rt += i[Count]
                Count += 1
            Count += 1
            i = re.sub(rt, '', i)
            i = re.sub(' ', '', i)

            rs = ''
            while i[Count] != ',':
                rs += i[Count]
                Count += 1
            Count += 1
            ZeroExtImm = i[Count:]
            ZeroExtImm = re.sub('\n', '', ZeroExtImm)
            ZeroExtImm = re.sub('\t', '', ZeroExtImm)
            dec = int(ZeroExtImm, 16)
            bin16 = lambda x:''.join(reversed([str((x >> i) & 1) for i in range(16)]))
            ZeroExtImm = bin16(dec)
            j += opcode[key_Opcode] + reg[rs] + reg[rt] + ZeroExtImm

        elif match != 0:
            Count = 0
            rt = ''
            while i[Count] != ',':
                rt += i[Count]
                Count += 1
            Count += 1
            i = re.sub(rt, '', i)
            i = re.sub(' ', '', i)

            SignExtImm = ''
            while i[Count] != '(':
                SignExtImm += i[Count]
                Count += 1
            Count += 1

            rs = i[Count:]
            rs = re.sub('\n', '', rs)
            rs = re.sub('\t', '', rs)
            rs = re.sub(' ', '', rs)
            rs = rs[:-1]

            SignExtImm = int(SignExtImm)
            bin16 = lambda x:''.join(reversed([str((x >> i) & 1) for i in range(16)]))
            SignExtImm = bin16(SignExtImm)

            j += opcode[key_Opcode] + reg[rs] + reg[rt] + SignExtImm
        else:
            Count = 0
            rt = ''
            while i[Count] != ',':
                rt += i[Count]
                Count += 1
            Count += 1
            i = re.sub(rt, '', i)
            i = re.sub(' ', '', i)

            rs = ''
            while i[Count] != ',':
                rs += i[Count]
                Count += 1
            Count += 1

            SignExtImm = i[Count:]
            SignExtImm = re.sub('\n', '', SignExtImm)
            SignExtImm = re.sub('\t', '', SignExtImm)
            SignExtImm = int(SignExtImm)
            bin16 = lambda x:''.join(reversed([str((x >> i) & 1) for i in range(16)]))
            SignExtImm = bin16(SignExtImm)

            j += opcode[key_Opcode] + reg[rs] + reg[rt] + SignExtImm
    # Chuyen ma code nhi phan sang thap luc phan
    deca = int(j, 2)
    hexa = hex(deca)

    n = 10-len(hexa)
    for k in range(0, n):
        hexa = hexa[:2] + '0' + hexa[2:]

    fileH.write(hexa+'\n')
    fileB.write(j+'\n')

fileA.close()
fileB.close()
fileH.close()

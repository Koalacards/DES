import binascii

k = "133457799BBCDFF1"

  
# Code to convert hex to binary
def hex_to_bin(hex_str):
    n = int(hex_str, 16) 
    bStr = ''
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1    
    return bStr.zfill(4 * len(hex_str))

k_binary = hex_to_bin(k)
  

PC1_left = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36]
PC1_right = [63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 48, 30, 22, 14, 6, 61, 53, 45, 37, 29, 31, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]


c_0, d_0 = [], []

for num in PC1_left:
    c_0.append(k_binary[num - 1])

for num in PC1_right:
    d_0.append(k_binary[num - 1])

CD_prev= (c_0, d_0)


def shift_left(bin_list, shift_length):
    bin_copy = bin_list.copy()
    for _ in range(shift_length):
        popped = bin_copy.pop(0)
        bin_copy.append(popped)

    return bin_copy

def v(i):
    if i in [1, 2, 9, 16]:
        return 1
    else:
        return 2   

k1 = None

for i in range(1, 17):
    (ciprev, diprev) = CD_prev
    c_i, d_i = shift_left(ciprev, v(i)), shift_left(diprev, v(i))
    CD_prev = (c_i, d_i)

    cd_i = c_i + d_i

    k_i = ""
    for num in PC2:
        k_i += cd_i[num - 1]

    if i == 1:
        k1 = k_i

    #print(f"K{i}: {k_i}")

x = "0123456789ABCDEF"

x_binary = hex_to_bin(x)

E = [31, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23 ,24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

IP_L = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8]

IP_R = [57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

L0, R0 = [], []

E_R0 = ""

for num in IP_L:
    L0.append(x_binary[num - 1])

for num in IP_R:
    R0.append(x_binary[num - 1])

for num in E:
    E_R0 += (R0[num - 1])

#print(f"E(R0): {E_R0}")

R0_str = "".join(R0)
#print(f"L1=R0: {R0_str}")

#R1: = L0 + f(R0 + K1)

#First, get R0 + K1

E_R0_plus_K1 = []
for i in range(len(E_R0)):
    k_bit = k1[i]
    r0_bit = E_R0[i]
    added = (int(k_bit) + int(r0_bit)) % 2
    E_R0_plus_K1.append(str(added))

E_R0_plus_K1_str = "".join(E_R0_plus_K1)
#print(f"R0: {E_R0} + K1 {k1} = {E_R0_plus_K1_str}")

#Split up this addition into 8 blocks of length 6

blocks = []
for i in range(0, len(E_R0_plus_K1), 6):
    blocks.append(E_R0_plus_K1[i: i + 6])
    


S1= [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

S2= [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]

S3= [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]

S4= [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
[13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
[10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]

S5= [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]

S6= [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
[10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]

S7= [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
[13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]

S8= [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
[7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
[2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

S_blocks = [S1, S2, S3, S4, S5, S6, S7, S8]

def S(block_str, i):
    row = block_str[0] + block_str[5]
    column = block_str[1:5]
    
    row_decimal = int(row, 2)
    column_decimal = int(column, 2)

    #print(f"row binary: {row} row decimal: {row_decimal}")
    #print(f"column binary: {column} column decimal: {column_decimal}")

    s_block_value = S_blocks[i][row_decimal][column_decimal]

    #print(f"s block value: {s_block_value}")
    s_block_value_bin = bin(s_block_value)
    s_block_value_bin_str = str(s_block_value_bin)[2:].zfill(4)
    #print(s_block_value_bin_str)

    return s_block_value_bin_str
    
C = ""
for i in range(len(blocks)):
    block = blocks[i]
    block_str = ""
    for bit in block:
        block_str+=str(bit)

    S_value_str = S(block_str, i)
    C+= S_value_str

#print(f"C Value: {C}")

    
#Finally, get the permuation table to get P(C)
  
P = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

P_C = []

for num in P:
    P_C.append(C[num - 1])

#Now that we have P_C, just add that and L_0 together to get R1

#print(P_C)
#print(len(P_C))

R1 = []

for i in range(len(P_C)):
    L0_bit = L0[i]
    P_C_bit = P_C[i]

    added = (int(L0_bit) + int(P_C_bit)) % 2

    R1.append(added)

R1_str = ""
for bit in R1:
    R1_str+=str(bit)

print(f"R1: {R1_str}")



####################################### CONSTANTS ######################################
k = "133457799BBCDFF1"
x = "0123456789ABCDEF"
PC1_left = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36]
PC1_right = [63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 48, 30, 22, 14, 6, 61, 53, 45, 37, 29, 31, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]


E = [31, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23 ,24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

IP_L = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8]

IP_R = [57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

hi = "HIIIIIIIIII"

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

P = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

Inverse_IP= [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]


########################################################################################

  
# Code to convert hex to binary
def hex_to_bin(hex_str):
    n = int(hex_str, 16) 
    bStr = ''
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1    
    return bStr.zfill(4 * len(hex_str))

k_binary = hex_to_bin(k)
  

#With the key, PC1 and PC2, complete the shift to get c0 and d0
c_0, d_0 = [], []

for num in PC1_left:
    c_0.append(k_binary[num - 1])

for num in PC1_right:
    d_0.append(k_binary[num - 1])

CD_prev= (c_0, d_0)


#This is used to shift the c and d to the left
def shift_left(bin_list, shift_length):
    bin_copy = bin_list.copy()
    for _ in range(shift_length):
        popped = bin_copy.pop(0)
        bin_copy.append(popped)

    return bin_copy

#the v value determining the shift
def v(i):
    if i in [1, 2, 9, 16]:
        return 1
    else:
        return 2   

#Now that we have all the tools, loop through c and d 16 times to get the 16 key rounds
keys = []
for i in range(1, 17):
    (ciprev, diprev) = CD_prev
    c_i, d_i = shift_left(ciprev, v(i)), shift_left(diprev, v(i))
    CD_prev = (c_i, d_i)

    cd_i = c_i + d_i

    k_i = ""
    for num in PC2:
        k_i += cd_i[num - 1]

    keys.append(k_i)

    #print(f"K{i}: {k_i}")


#This is the function that references the S blocks to get the new binary bits of length 4
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

#Convert the plaintext to binary
x_binary = hex_to_bin(x)

L0, R0 = [], []


#Using the Initial Permutation, get L0 and R0
for num in IP_L:
    L0.append(x_binary[num - 1])

for num in IP_R:
    R0.append(x_binary[num - 1])

L_prev, R_prev = L0, R0

#Start the loop to get all the L and R values up to L16 and R16
for i in range(1, 17):

    E_Ri = []
    #Using the E table, the E value of the R value
    for num in E:
        E_Ri.append(R_prev[num - 1])



    #R(i) = L(i-1) + f(R(i-1) + K(i))

    #First, get E(R(i-1)) + Ki

    k_i = keys[i - 1]

    E_Ri_plus_Ki = []
    for j in range(len(E_Ri)):
        k_bit = k_i[j]
        r0_bit = E_Ri[j]
        added = (int(k_bit) + int(r0_bit)) % 2
        E_Ri_plus_Ki.append(str(added))


    #Split up this addition into 8 blocks of length 6

    blocks = []
    for i in range(0, len(E_Ri_plus_Ki), 6):
        blocks.append(E_Ri_plus_Ki[i: i + 6])

    #Loop through the blocks to get the S string of length 32 (also called C)
    C = ""
    for j in range(len(blocks)):
        block = blocks[j]
        block_str = ""
        for bit in block:
            block_str+=str(bit)

        S_value_str = S(block_str, j)
        C+= S_value_str

        
    #Finally, use the permutation table to get P(C)

    P_C = []

    for num in P:
        P_C.append(C[num - 1])

    #Now that we have P_C, just add that and L(i-1) together to get R(i)


    R_i = []

    for j in range(len(P_C)):
        Li_bit = L_prev[j]
        P_C_bit = P_C[j]

        added = (int(Li_bit) + int(P_C_bit)) % 2

        R_i.append(added)

    #L(i) = R(i-1)
    L_i = R_prev

    #Set L(i) and R(i) as L(i-1) and R(i-1) for the next iteration of the loop
    L_prev, R_prev = L_i, R_i


#When the loop ends, L_prev and R_prev with be L16 and R16

L16, R16 = L_prev, R_prev

#Now all that is left to do is run the inverse initial permutation with L16 and R16, then convert 
#back to hexadecimal

merged = L16 + R16

IP_L16_R16 = []
for num in Inverse_IP:
    IP_L16_R16.append(merged[num - 1])

IP_L16_R16_str = ""
for byte in IP_L16_R16:
    IP_L16_R16_str+=str(byte)


#This is the binary representation of the ciphertext, now just convert to hexadecimal
def bin_to_hex(bin_str:str):
    return '%0*X' % ((len(bin_str) + 3) // 4, int(bin_str, 2))

y = bin_to_hex(IP_L16_R16_str)

print(f"Ciphertext: {y}")




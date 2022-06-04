cipherText = '' # 암호문
cipherList = [] # 유니코드로 변환시킨 암호문
reXorList = []
plainText = ''
conversionNum = 0
keyString = ''
keyList = []

# ========================= Line =============================

def CipherToUniCode(cipher_t, datalength) :
    c_List = []
    for i in range(0, datalength) :
        c_List.append(ord(cipher_t[i]))

    return c_List

# ========================= Line =============================

def Todigit(uni_d, convert_n, datalength) :
    for i in range(0, datalength) :
        tmpNum = uni_d[i]
        uni_d[i] = int(str(tmpNum), convert_n)

# ========================= Line =============================

def KeyStringToUniCode(key_string, datalength) :
    key_list = []
    for i in range(0, datalength) :
        key_list.append(ord(key_string[i]))

    return key_list

# ========================= Line =============================

def reXorFunc(cipher_list, key_list, datalength) :
    reXor_list = []
    for i in range(0, datalength) :
        reXor_list.append(cipher_list[i] ^ key_list[i])

    return reXor_list
# ========================= Line =============================

cipherText = input("암호문을 입력하세요 >> ")
conversionNum = int(input("변환에 사용된 진법을 입력하세요 >>"))
keyString = input("키 데이터를 입력하세요 >>")

dataLength = len(cipherText)
print("암호문을 변환하는중....")
# 암호문 -> 유니코드(n진법)
for i in range(0, dataLength) :
    cipherList.append(ord(cipherText[i]))

# Test code
# print("유니코드로 변환된 암호문: ", cipherList)

# 유니코드(n진법) -> 유니코드(10진법)
for i in range(0, dataLength) :
    tmpNum = cipherList[i]
    cipherList[i] = int(str(tmpNum), conversionNum)

print("변환 완료.")

print("키 데이터를 변환하는중...")
# key 문자열 -> 유니코드 리스트
for i in range(0, dataLength) :
    keyList.append(ord(keyString[i]))

print("변환 완료.")
# Test Code
# print("변환된 키 데이터: ", keyList)

print("데이터를 복호화 하는중...")
# (암호문 유니코드) XOR (key 유니코드)
for i in range(0, dataLength) :
    reXorList.append(cipherList[i] ^ keyList[i])

# Test Code
# print("다시 XOR연산된 리스트: ", reXorList)

for i in range(0, dataLength) :
    plainText += chr(reXorList[i])

print("복호화된 평문: ", plainText)

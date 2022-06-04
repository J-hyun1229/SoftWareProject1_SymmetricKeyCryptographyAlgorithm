import sys
import random

plainText = "" # 암호화할 데이터
keyString = "" # 암,복호화에 사용할 키
keyList = [] # 연산을 위해 리스트화시킨 키 
conversionNum = 0 # 변환할 진법
XorList = []
ConvertedXorList = []
InputEncodeType = sys.stdin.encoding
OutputEncodeType = sys.stdout.encoding
UniConvertedData = [] # 유니코드로 변환된 데이터
cipherText = "" # 암호화된 데이터
RejectChars = ['\n', '\b', '\r', '\t', '\'', '\"', '#']
IsContainsRC = False

# =========================== Line ===============================

def StringToUniCode(string_d, datalength) :
    uni_d = []
    for i in range(0, datalength) :
        uni_d.append(ord(string_d[i]))
        
    return uni_d
        
# =========================== Line ===============================

def CreateKeyList(datalength) :
    key_li = []
    for i in range(0, datalength) :
        key_li.append(random.randrange(97, 123))

    return key_li

# =========================== Line ===============================

def CreateKeyString(keyList) :
    keyStr = ''
    for i in range(0, len(keyList)) :
        keyStr += chr(keyList[i])

    return keyStr

# =========================== Line ===============================

def CreateXorList(uni_d, keyList, datalength) :
    xorList = []
    for i in range(0, datalength) :
        xorList.append(uni_d[i] ^ keyList[i])
        
    return xorList

# =========================== Line ===============================

def NumConvertFunc(List, convert_n, datalength) :
    convertedList = []
    
    for i in range(0, dataLength) :
        tmpList = [] # 진법변환된 숫자 하나를 저장할 리스트
        tmpStr = ''
        tmpNum = List[i]
        while True :
            tmpList.append(tmpNum % convert_n)
            tmpNum //= convert_n
            if(tmpNum == 0) : break
        tmpList.reverse()
        for i in tmpList :
            tmpStr += str(i)
        convertedList.append(int(tmpStr))

    return convertedList

# =========================== Line ===============================

def CreateChiperText(convertedList, datalength) :
    cipher_Text =''
    for i in range(0, dataLength) :
        cipher_Text += chr(convertedList[i])

    return cipher_Text

# ========================= Main Code =============================

plainText = input("변환할 데이터를 입력하세요: ")
dataLength = len(plainText)

# 원본 데이터 확인
print("\n입력한 데이터 : ", end='')
for i in range(0, len(plainText)) :
    print(plainText[i], end=' ')
print()

print("데이터 암호화 중...")

# 데이터를 유니코드로 변환
UniConvertedData = StringToUniCode(plainText, dataLength)

conversionNum = random.randrange(4, 10)
# print("선택된 진법: ", conversionNum)

while True :
    # 키 생성
    keyList = CreateKeyList(dataLength)

    # 평문과 키를 XOR
    XorList = CreateXorList(UniConvertedData, keyList, dataLength)

    # XorList를 진법변환
    ConvertedXorList = NumConvertFunc(XorList, conversionNum, dataLength)
    
    # 암호문 생성
    for i in range(0, dataLength) :
        cipherText += chr(ConvertedXorList[i])

    # 화이트 스페이스가 있다면 암호문을 다시 생성
    IsContainsRc = False
    for ch in RejectChars :
        if ch in cipherText :
            IsContainsRC = True
            cipherText = ''

    if(IsContainsRC == False) : break
    
keyString = CreateKeyString(keyList)

print("암호화 완료.\n")

print("암호문")
print(cipherText)
print("\n키 데이터")
print(keyString)
print("\n사용된 진법 : ", conversionNum)
print()
print("주의) 키 데이터와 사용된 진법은 안전하게 보관하세요!")

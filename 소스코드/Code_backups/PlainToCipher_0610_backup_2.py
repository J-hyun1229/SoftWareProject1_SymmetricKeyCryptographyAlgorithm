import sys
import random
import os

plainText = "" # 암호화할 데이터
keyString = "" # 암,복호화에 사용할 키
keyList = [] # 연산을 위해 리스트화시킨 키 
conversionNum = 0 # 변환할 진법
XorList = []
ConvertedXorList = []
InputEncodeType = 'UTF-8'
OutputEncodeType = 'UTF-8'
UniConvertedData = [] # 유니코드로 변환된 데이터
cipherText = "" # 암호화된 데이터
RejectChars = ['\n', '\b', '\r', '\t', '\'', '\"', '#']
IsContainsRC = True
infilePath = '' # 암호화할 원본파일 경로
outfilePath = '' # 암호화된 파일을 저장할 경로
inFp = None
outFp = None
inList = ''

# =========================== Line ===============================

def StringToUniCode(string_d, datalength) :
    uni_d = []
    for i in range(0, datalength) :
        uni_d.append(ord(string_d[i]))
        
    return uni_d
        
# =========================== Line ===============================

def CreateKeyList(datalength) :
    print("In CreateKeyList()")
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
    print("In CreateXorList()")
    xorList = []
    for i in range(0, datalength) :
        xorList.append(uni_d[i] ^ keyList[i])
        
    return xorList

# =========================== Line ===============================

def NumConvertFunc(List, convert_n, datalength) :
    print("In NumConvertFunc()")
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

def CreateCipherText(convertedList, datalength) :
    print("In CreateChiperText()")
    cipher_Text =''
    for i in range(0, dataLength) :
        cipher_Text += chr(convertedList[i])

    return cipher_Text

# =========================== Line ===============================

def checkRC(cipher_text) :
    print("In checkRC")
    for ch in RejectChars :
        if ch in cipher_text :
            print("it contains RC\n")
            return True

    return False

# ========================= Main Code =============================

infilePath = input("암호화할 파일의 경로를 입력하세요:")
outfilePath = input("암호파일을 저장할 위치를 입력하세요.(공백 입력시 현재위치에 저장):")
inFp = open(infilePath, "r",  encoding = InputEncodeType)
outFp = open(outfilePath, "w", encoding = OutputEncodeType)

if os.path.exists(infilePath) == False :
    print(infilepath + ": 파일이 없습니다.")
    sys.exit(0)

if os.path.exists(outfilePath) == False :
    print(outfilepath + ": 파일이 없습니다.")
    sys.exit(0)
    

inList = inFp.readlines()

print("데이터 암호화 중...")

conversionNum = random.randrange(4, 10)

for plainStr in inList :

    dataLength = len(plainStr)
    
    # 데이터를 유니코드로 변환
    UniConvertedData = StringToUniCode(plainStr, dataLength)

    # IsContainsRC = True
    # while IsContainsRC :
    # 키 생성
    keyList = CreateKeyList(dataLength)
    keyString += CreateKeyString(keyList)

    # 평문과 키를 XOR
    XorList = CreateXorList(UniConvertedData, keyList, dataLength)

    # XorList를 진법변환
    ConvertedXorList = NumConvertFunc(XorList, conversionNum, dataLength)
    
    # 암호문 생성
    cipherText = CreateCipherText(ConvertedXorList, dataLength)
    
    # 화이트 스페이스가 있다면 암호문을 다시 생성
    # IsContainsRC = checkRC(cipherText) # 있으면 True

    outFp.writelines(cipherText)
    
inFp.close()
outFp.close()
print("암호 파일이 생성되었습니다!\n")

print("키 데이터")
print(keyString)
print("\n사용된 진법")
print(conversionNum)
print()
print("주의) 키 데이터와 사용된 진법은 외부에 노출하지 마세요!")

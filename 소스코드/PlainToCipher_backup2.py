import sys
import random

plainText = "" # 암호화할 데이터
keyString = "" # 암,복호화에 사용할 키
keyList = [] # 연산을 위해 리스트화시킨 키 
ConvertedKeyList = [] # 진법변환된 키
conversionNum = 0 # 변환할 진법
InputEncodeType = sys.stdin.encoding
OutputEncodeType = sys.stdout.encoding

UniConvertedData = [] # 유니코드로 변환된 데이터
NumConvertedData = [] # 진법 변환된 데이터
cipherText = "" # 암호화된 데이터
cipherList = []


plainText = input("변환할 데이터를 입력하세요: ")

# 원본 데이터 확인
print("\n입력한 데이터 : ", end='')
for i in range(0, len(plainText)) :
    print(plainText[i], end='')
print()

# 유니코드로 변환하여 데이터 저장
print("데이터를 유니코드로 변환하는중...")
for i in range(0, len(plainText)) :
    UniConvertedData.append(ord(plainText[i]))
print("변환 완료.\n")

# 변환된 데이터 test code
# print("유니코드로 변환 : ", end='')
# for i in range(0, len(UniConvertedData)) :
#    print(UniConvertedData[i], end=" ")
# print()

# 진법변환 프로세스 1
print("유니코드 데이터를 진법변환 하는중...")
conversionNum = random.randrange(4,10) # 4~9 사이의 진법 중 랜덤으로 결정.
print("선택된 진법: ", conversionNum)

dataLength = len(UniConvertedData) # 변환할 데이터 길이

for i in range(0, dataLength) :
    tmpList = [] # 진법변환된 숫자 하나를 저장할 리스트
    tmpStr = ''
    tmpNum = UniConvertedData[i]
    while True :
        tmpList.append(tmpNum % conversionNum)
        tmpNum //= conversionNum
        if(tmpNum == 0) : break
    tmpList.reverse()
    for i in tmpList :
        tmpStr += str(i)
    NumConvertedData.append(int(tmpStr))

# 유니코드 진법변환 test Code
# print("진법변환된 유니코드 데이터 : ", end="")
# print(NumConvertedData)

print("변환 완료.\n")

print("키를 생성하는중....")
for i in range(0, dataLength) :
    keyList.append(random.randrange(0,50))

print("생성 완료.\n")
# 키 데이터 test Code
# print(keyList)
# print()

# 진법변환 프로세스 2
print("키 데이터를 진법변환 하는중...")
for i in range(0, len(keyList)) :
    tmpList = [] # 진법변환된 숫자 하나를 저장할 리스트
    tmpStr = ''
    tmpNum = keyList[i]
    while True :
        tmpList.append(tmpNum % conversionNum)
        tmpNum //= conversionNum
        if(tmpNum == 0) : break
    tmpList.reverse()
    for i in tmpList :
        tmpStr += str(i)
    ConvertedKeyList.append(int(tmpStr))

print("변환 완료.\n")
for i in range(0, dataLength) :
    keyString += chr(ConvertedKeyList[i])

print("키 데이터 :", end="")
print(keyString)
print()

print("데이터를 암호화 하는중...")
# 유니코드 데이터와 키 데이터를 진법변환해서 XOR연산.
for i in range(0, dataLength) :
    cipherList.append(NumConvertedData[i] ^ ConvertedKeyList[i])

# 암호화된 데이터 테스트 코드
print("XOR연산된 리스트 : " , cipherList)

for i in range(0, dataLength) :
#    print(chr(cipherList[i]), end=', ')
    cipherText += chr(cipherList[i])

print("암호화 완료.")

print("암호화된 데이터:", cipherText)
print("주의) 키 데이터와 사용된 진법은 안전하게 보관하세요!")

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


plainText = input("변환할 데이터를 입력하세요: ")
dataLength = len(plainText)

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

print("데이터 암호화 중...")

conversionNum = random.randrange(4, 10)
print("선택된 진법: ", conversionNum)

print("키를 생성하는중....")
for i in range(0, dataLength) :
    keyList.append(random.randrange(97,123))
    keyString += chr(keyList[i])

print("생성 완료.\n")
# Test Code
# print(keyList)

for i in range(0, dataLength) :
    XorList.append(UniConvertedData[i] ^ keyList[i])

# Test Code
# print("XOR연산된 데이터:", XorList)

for i in range(0, dataLength) :
    tmpList = [] # 진법변환된 숫자 하나를 저장할 리스트
    tmpStr = ''
    tmpNum = XorList[i]
    while True :
        tmpList.append(tmpNum % conversionNum)
        tmpNum //= conversionNum
        if(tmpNum == 0) : break
    tmpList.reverse()
    for i in tmpList :
        tmpStr += str(i)
    ConvertedXorList.append(int(tmpStr))

# Test Code
# print("진법변환된 XOR 데이터:", ConvertedXorList)

print("암호문 생성중...")
for i in range(0, dataLength) :
    cipherText += chr(ConvertedXorList[i])

print("암호화 완료.\n")

print("암호문")
print(cipherText)
print("\n키 데이터")
print(keyString)
print()
print("주의) 키 데이터와 사용된 진법은 안전하게 보관하세요!")

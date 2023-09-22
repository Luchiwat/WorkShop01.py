2. #จงเขียนโปรแกรมPython ของโปรแกรมคำนวณหาค่าเฉลียของคะแนนจากการสอบ 3 ครั้ง 
#โดยรับค่ารหัสนักเรียนชือนักเรียนและคะแนนสอบแต่ละครั้งรวม 3 ครั้งทางแป้นพิมพ์แล้วแสดงผลค่าเฉลียทีคำนวณได้ทางหน้าจอ

def inputData():
    str_name=input('ป้อนชื่อ : ')
    str_pass=input('ป้อนรหัสนักศึกษา : ')
    no1=float(input('โปรดคะแนนครั้งที่ 1 : '))
    no2=float(input('โปรดคะแนนครั้งที่ 2 : '))
    no3=float(input('โปรดคะแนนครั้งที่ 3 : '))
    return str_name,str_pass,no1,no2,no3

def calSumOfNumber(no1,no2,no3) :
    sumOfNumber = no1+no2+no3
    return sumOfNumber

def calAverageOfNumber( no1,no2,no3,) :
    averageOfNumber = ((no1+no2+no3)/3)
    return averageOfNumber

def showDataAndSumAndAverageOfNumber( no1,no2,no3,sumOfNumber,averageOfNumber) :
    print(f'ชื่อ : {str_name}')
    print(f'รหัสนักศึกษา : {str_pass}')
    print(f'คะแนนครั้งที่ 1 is {no1}')
    print(f'คะแนนครั้งที่ 2 is {no2}')
    print(f'คะแนนครั้งที่ 3 is {no3}')
    print('=================================')
    print(f'คะแนนรวม{sumOfNumber}')
    print(f'คะแนนเฉลี่ย {averageOfNumber:.4f}')

print('==========================================')
print('         Program Average 3 Number         ')
print('==========================================')
str_name,str_pass,no1,no2,no3 = inputData( )
sumOfNumber = calSumOfNumber(no1,no2,no3)
averageOfNumber = calAverageOfNumber( no1,no2,no3)
print('==========================================')
showDataAndSumAndAverageOfNumber(no1,no2,no3,sumOfNumber,averageOfNumber)
print('==========================================')
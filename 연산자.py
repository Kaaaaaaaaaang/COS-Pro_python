# 산술 연산자
# (1) 증감 연산자
a = 1
# a++
print(a)
# ** 파이썬에서 증감 연산자는 지원하지 않는다.

# (2) 나누기의 결과는 실수
num1 = 10
num2 = 2
print(type(num1), type(num2)) # int, int
result1 = num1/num2
print(type(result1)) # float

lf = 1074/100
num = int(lf)
print(num, type(num)) # 10, int
print(lf, type(lf)) # 10.74, float

a, b = 23, 4
c = a/b
print(c, type(c)) # 5.75, float
d = int(a/b)
print(d, type(d)) # 5, int
e = a/b
print(e, type(e)) # 5.75, float

# 관계 연산자
a, b = 20, 20
print(a is b) # True
c, d = [10], [10]
print(c is d) # False
print(c==d) # True
# is => 참조 영역, == => 값

# 논리 연산자
# x 변수의 값이 0 이상 100 미만
if 0<=x and x<100:
if 0 <= x < 100

# 조건식의 결과 판단하기
a = 10
if a>=0 :
  # a가 0 이상일 때 실행할 코드
  
while 조건식 :
  #조건식이 참일 동안 반복 실행

for 변수명 in 리스트 :
  # 리스트의 각 요소의 처리

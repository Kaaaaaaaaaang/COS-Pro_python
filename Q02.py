# A쇼핑몰에서는 회원 등급에 따라 할인 서비스를 제공합니다. 회원 등급에 따른 할인율은 다음과 같습니다. (S=실버, G=골드, V=VIP)
# S => 5% G => 10% V => 15%
# 상품의 가격 price와 구매자의 회원 등급을 나타내는 문자열 grade가 매개변수로 주어질 때, 할인 서비스를 적용한 가격을 return 하도록 solution 함수를 완성해주세요.
# price는 100이상 100,000이하의 100단위 자연수

def solution(price, grade):
  answer=0
  if grade=="S":
    answer = int(price*0.95)
  elif grade=="G":
    answer=int(price*0.9)
  elif grade=="V":
    answer=int(price*0.85)
  return answer

solution(300, 'G')

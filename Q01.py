# A학교에서는 단체 티셔츠를 주문하기 위해 학생 별로 원하는 티셔츠를 조사했다. 선택할 수 있는 티셔츠 사이즈는 작은 순서대로 "XS", "S", "M", "L", "XL", "XXL" 총 6종류가 있습니다. 
# 학생 별로 원하는 티셔츠 사이즈를 조사한 결과가 들어있는 리스트 shirt_size가 매개변수로 주어질 때, 사이즈 별로 티셔츠가 몇 벌씩 필요한지 가장 작은 사이즈부터 순서대로 리스트에 담아
# return 하도록 solution 함수를 완성해주세요.

def solution(shirt_size):
  answer=[0, 0, 0, 0, 0, 0]
  for size in shirt_size:
    if size == "XS":
      answer[0] = answer[0]+1
    elif size == "S":
      answer[1] = answer[1]+1
    elif size == "M":
      answer[2] = answer[2]+1
    elif size == "L":
      answer[3] = answer[3]+1
    elif size == "XL":
      answer[4] = answer[4]+1
    elif size == "XXL":
      answer[5] = answer[5]+1
  return anwer
  
  shirt_size = ["XS", "S", "M", "L", "XL", "XXL", "L"]
  solution(shirt_size)

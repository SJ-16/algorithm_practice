stack = []

stack.append(5) # 삽입()
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop() # 삭제() / 가장 마지막에 들어온 자료가 삭제

print(stack[::-1]) # 최상단 원소부터 출력
print(stack) # 최하단 원소부터 출력
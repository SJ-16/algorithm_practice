from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
# (list자료형 이용해서 구현가능하나 시간복잡도가 높아서 비효율적으로 동작할 수 있으므로 꼭, deque 라이브러리 이용)
queue = deque( )

queue.append(5) # 삽입()  / 우입
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() # 삭제() / 좌출
queue.append(1)
queue.append(4)
queue.popleft() # 삭제() / 좌출

print(queue) # 먼저 들어온 순서대로 출력 3 7 1 4
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력 4 1 7 3
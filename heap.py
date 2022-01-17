import sys
import heapq # 라이브러리마다 minheap인지 maxheap인지 다름 python의 경우 minheap
input = sys.stdin.readline

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

n = int(input()) # 크기 설정
arr = []

for i in range(n):
    arr.append(int(input())) # 숫자 입력

res = heapsort(arr) # 힙 정렬

for i in range(n):
    print(res[i]) # 작은수부터 차례대로 출력(minheap)
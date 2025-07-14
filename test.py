# 깃 체험중 
# #함수정의
def LS(search,dataList): #search,datalist를 인자로 받는 함수 LS를 정의함
  i=0  #인덱스 번호 초기환
  flag=False #검색성공여부를 저장하는 변수 -> 초기값:거짓(False)
  while i<len(dataList): #리스트의 길이만큼 반복
    if search==dataList[i]: #현재 인덱스의 값이 찾고자 하는 값과 같은 경우의 조건문
      flag=True #검색 성공이기 때문에 flag를 true로 설정함
      break # 반복문을 종료
    else: i=i+1 #현재 인덱스의 값이 찾고자 하는 값과 다른 경우, 인덱스를 1 증가시켜 다음 인덱스를 확인
  if flag==True: print(f'{search}는(/은) 리스트에 있어요.') #검색 성공시, 성공했다고 출력함
  else: print('찾는 데이터가 없어요.') #검색에 실패한 경우, 리스트에 없다고 출력함

def BS(search,dataList): #search.dataList를 인자로 받는 함수 BS를 정의함
  dataList.sort()  #이진 검색을 위해서는 리스트가 정렬되어있어야함, 따라서 리스트를 정렬함
  low,high=0,len(dataList)-1 #검색 범위를 초기화함, 시작, 끝 인덱스 값
  flag=False #검색성공여부를 저장하는 변수 -> 초기값:거짓(False)
  while low<=high: # 검색 범위가 유효한 동안 반복하도록 함
    min=(low+high)//2 #이진 검색을 위한 중앙 값을 찾기 위해 중앙 인덱스를 계산하여 min에 저장함
    if dataList[min]==search: #중앙값이 찾고자 하는 값이라면
      flag=True #검색성공임으로 flag를 true로 설정함
      break #반복문을 종료
    elif dataList[min]<search: low=min+1 #찾는 값이 중앙값보다 크다면,검색 범위를 중앙에서 오른쪽 부분으로 변경
    else: high=min-1 #찾는 값이 중앙값보다 작다면, 검색범위를 중앙에서 왼쪽 부분으로 변경
  if flag==True: print(f'{search}는(/은) 리스트에 있어요.') #검색 성공시, 성공했다고 출력함
  else: print('찾는 데이터가 없어요.') #검색에 실패한 경우, 리스트에 없다고 출력함

#main 및 함수호출
import random #난수값 발생을 위한 모듈 추가함
dataList=list()  #빈 리스트, dataList=[], 랜덤으로 뽑은 30개의 데이터를 저장받을 공간
for i in random.sample(range(60,100),30): # random.sample()을 사용하여 60부터 99까지의 수 중 중복 없이 30개를 무작위로 선택
  dataList.append(i) # 선택한 숫자를 리스트에 추가
print('[1]선형검색\n[2]이진검색\n[0]종료') # 검색 방법 선택 메뉴 출력
while True: # 무한 루프를 통해 반복적으로 검색 기능 제공
  select=int(input('검색할 방법: '))  # 사용자에게 검색 방법 입력받음
  if select==0: # 0을 입력한 경우
    print('검색종료') # 종료 메시지 출력
    break # 반복문 종료
  else:#0이 아닌 수를 입력한 경우
    search=int(input('검색할 데이터: ')) # 검색할 값을 사용자로부터 입력받음
    if select==1: LS(search,dataList)  #선형검색함수호출
    elif select==2: BS(search,dataList)  #이진검색함수호출

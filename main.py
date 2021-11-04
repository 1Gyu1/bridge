import random

print("오징어 게임에 참가하셨습니다")
print("이번 게임은 다리 건너기 입니다")

#오른쪽일까? 왼쪽일까?
print("오른쪽 왼쪽 중에 선택하세요")
#1번은 왼쪽 2번은 오른쪽
print("1번은 왼쪽 2번은 오른쪽")

#총 10칸의 다리가 있다
glass = [1,1,1,1,1,1,1,1,1,1]
for i in range(1,10):
    glass[i] = random.randint(1,2)
    #print(glass[i])

i=0
while i!=10:
    print(glass[i])
    try:
#오른쪽인지 왼쪽인지 맞추면 살 수 있고
        if glass[i] == int(input("선택하세요 1 or 2 :")):
            i+=1
            print("통과 {}번째칸 성공".format(i))

#틀리면 죽는다
        else:
            print("으아ㅏㅏ...")
            break
    
    except:
        print("1 또는 2만 입력하세요")


#최종 10칸까지 다가면 승리
if i==9:
    print("축하드립니다 당신은 생존하였습니다")
#중간에 틀리면 게임 오버
else:
    print("탈락...")
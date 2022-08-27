#스킬:중국인의 나머지 정리
#딱보고 풀땐:완전 탐색 브루트포스
e,s,m=map(int,input().split())

year=1
while True:
    if year%15==e%15:
        if year%28==s%28:
            if year%19==m%19:
                break

    year+=1
print(year)
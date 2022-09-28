n, k = map(int, input().split())            #n:동전종류 , k:가치의 합
c = []                                      #빈 리스트
dp = [0 for i in range(k + 1)]              #0제외 k개까지
for i in range(n):
    c.append(int(input()))                  #동전 가치 입력
for i in range(1, k + 1):                   #1부터 k까지
    a = []                                  #빈 리스트
    for j in c:                             #동전 가치 리스트 안에 있을 때
        if j <= i and dp[i - j] != -1:      #뒤에 있거나 만들수 있을 때
            a.append(dp[i - j])             #추가
    if not a:                               #안되면
        dp[i] = -1                          #-1
    else:
        dp[i] = min(a) + 1                  #작은걸로 들어감
print(dp[k])
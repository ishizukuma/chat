#三項演算子：<条件式> ? <真式> : <偽式>
N, L, H = map(int, input().split())
print("Yes") if H - L + 1 < N else print("No")

#index error 対策
#i = (i + 1) % N
#i = 0 if i == N-1 else i + 1
#j += (B[j] == 0)
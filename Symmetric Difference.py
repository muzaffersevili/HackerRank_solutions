m,m_val=int(input()),set(map(int,input().split()))
n,n_val=int(input()),set(map(int,input().split()))

a=sorted(m_val.symmetric_difference(n_val))

for i in range(len(a)):
    print(a[i])
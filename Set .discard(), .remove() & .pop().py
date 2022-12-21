n = int(input())
s = set(map(int, input().split()))

pr=int(input())

process=""
for i in range(pr):
    process=input().split()
    if(process[0]=='pop'):
        s.pop()
    elif(process[0]=='remove'):
        s.remove(int(process[1]))
    elif(process[0]=='discard'):
        s.discard(int(process[1]))

print(sum(s))
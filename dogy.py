num,mam=map(int,input().split())
lit=[]
for _ in range(num):
	lit.append(sorted(list(map(int,input().split()))))
for i in range(num-1):
	for j in range(mam):
		for k in range(num-i):
			if(lit[i][j]>lit[i+k][j]):
				lit[i][j],lit[i+k][j]=lit[i+k][j],lit[i][j]
for i in lit:
	print(*i,sep=' ')   

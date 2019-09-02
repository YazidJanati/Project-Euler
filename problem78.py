
import matplotlib.pyplot as plt
'''decompDicts = [{0: 1},{1:1},{2:1,1:1},{3:1,2:2,1:1}]


for num in range(4,2000):
    dict = {n: sum([decompDicts[num-n][k] for k in list(decompDicts[num-n].keys()) if k<=n]) for n in range(num,0,-1)}
    decompDicts.append(dict)'''


decompsList = [[0],[0,1],[0,1,1],[0,1,1,1]]
cumulativeDecomps = [[0],[0,1],[0,1,2],[0,1,2,3]]

def cumulativeList(list):
    cumul = [0]
    for x in list[1:]:
        cumul.append(cumul[-1]+x)
    return cumul
    #return [0]+[sum(list[:k+1]) for k in range(1,len(list))]

for num in range(4,200):
    decomp = [0]+[cumulativeDecomps[num-k][k] if k <= num//2  \
                else cumulativeDecomps[num-k][num-k] for k in range(1,num)] + [1]
    cumulativeDecomps.append(cumulativeList(decomp))

#print(cumulativeDecomps)
plt.plot([cumulativeDecomps[x][-1] for x in range(4,200)])
plt.show()

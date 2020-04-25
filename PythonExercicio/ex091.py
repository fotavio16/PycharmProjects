from random import randint
import time

def quickSortDict(arr):
   if len(arr) <= 1: return arr
   m = arr[0]['valor']
   return quickSortDict([i for i in arr if i['valor'] > m]) + \
          [i for i in arr if i['valor'] == m] + \
          quickSortDict([i for i in arr if i['valor'] < m])


ranking = list()
print("Valores sorteados:")
for i in range(6):
    sorteio = dict()
    sorteio['jogador'] = i + 1
    sorteio['valor'] = randint(1,6)
    print(f'O jogador{sorteio["jogador"]} tirou ',end='')
    time.sleep(2)
    print(sorteio['valor'])
    ranking.append(sorteio.copy())

time.sleep(1)
print("Ranking dos Jogadores:")
novorank = quickSortDict(ranking)
for i in range(6):
    time.sleep(1)
    print(f"{i+1}º lugar: jogador{novorank[i]['jogador']} com {novorank[i]['valor']}")


'''
def quicksort(list, start, end):
    if start < end:
        split = partition(list, start, end)
        quicksort(list, start, split-1)
        quicksort(list, split+1, end)
    else:
        return



def quicksort(l):
    if l:
        left = [x for x in l if x < l[0]]
        right = [x for x in l if x > l[0]]
        if len(left) > 1:
            left = quicksort(left)
        if len(right) > 1:
            right = quicksort(right)
        return left + [l[0]] * l.count(l[0]) + right
    return []

def quicksort(arr):
   if len(arr) <= 1: return arr
   m = arr[0]
   return quicksort(filter(lambda i,j=m: i<j, arr)) + \
          filter(lambda i,j=m: i==j, arr) + \
          quicksort(filter(lambda i,j=m: i>j, arr))

def quicksort2(arr):
   if len(arr) <= 1: return arr
   m = arr[0]
   return quicksort2([i for i in arr if i > m]) + \
          [i for i in arr if i == m] + \
          quicksort2([i for i in arr if i < m])

'''


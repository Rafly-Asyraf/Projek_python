from collections import deque

print("_____________ QUEUE ___________\n")
print("")
antrian=deque([1,2,3,4,5])
print(antrian)
print("")
antrian.append(6)
print("data masuk :",6)
print("data sekarang adalah",antrian)
print("")
keluar = antrian.popleft()
print("data keluar :",keluar)
print("data sekarang adalah :",antrian)
print("")
keluar = antrian.popleft()
print("data keluar :",keluar)
print("data sekarang adalah :",antrian)


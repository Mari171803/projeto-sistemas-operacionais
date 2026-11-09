import fcfs

linhas = [] 
with open('teste.txt') as l:
    linhas = l.readlines()

count = 0
for linha in linhas:
    count += 1
    print(f'linha {count}: {linha}')

int_linha = int(linha)





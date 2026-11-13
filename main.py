import fcfs
import rr
import sjf


# Leitura do arquivo .txt, retirando espaços em branco e "\n", além de converter de string para inteiro
linhas = [] 
with open('arquivo-processos.txt', encoding= "utf-8") as l:
    linhas = [int(valor) for valor in l.read().split()] 



# Loop que cria uma matriz contendo, em ordem, o id dos processos, o tempo de chegada e a duração dos processos
processos = []
quantia_processos = int((len(linhas) / 2))
i = j = c = 0

for i in range(quantia_processos):
    linha_processos = [i]

    for j in range(2):
        info = linhas[c]
        linha_processos.append(info)
        c += 1

    processos.append(linha_processos)
    


# Chamada das funções passando a matriz processos como atribuição em um for
print("------FCFS------")
fcfs.processes = []
for i in range(len(processos)):
    fcfs.processes.append({
        'pid': f'P{processos[i][0]}',
        'arrival': processos[i][1],
        'burst': processos[i][2]
    })
fcfs.result = fcfs.fcfs(fcfs.processes)
fcfs.print_results(fcfs.result)
print("----------------\n\n")


print("------SJF------")
sjf.processes = []
for i in range(len(processos)):
    sjf.processes.append({
        'pid': f'P{processos[i][0]}',
        'arrival': processos[i][1],
        'burst': processos[i][2]
    })
sjf.result = sjf.sjf(sjf.processes)
sjf.print_results(sjf.result)
print("---------------\n\n")


print("-------RR-------")
rr.processes = []
for i in range(len(processos)):
    rr.processes.append({
        'pid': f'P{processos[i][0]}',
        'arrival': processos[i][1],
        'burst': processos[i][2]
    })
rr.result = rr.round_robin(rr.processes, quantum=2)
rr.print_results(rr.result)
print("----------------")
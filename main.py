import fcfs
import sjf
import rr

import sys
from pathlib import Path



# Leitura do arquivo .txt para retirada das informações dos processos
    ## o arquivo resultado.txt é ignorado e as seguintes revisões são feitas: 
        ### se não existe um arquivo de entrada dos dados, se existe mais de um arquivo de entrada
        ### se os valores no arquivo são inteiros, se existe quantidades incorretas de entradas
pasta = Path(__file__).resolve().parent
arquivos_entrada = [
    arquivo for arquivo in pasta.glob("*.txt")
    if arquivo.is_file() and arquivo.name.casefold() != "resultado.txt"
]

if not arquivos_entrada:
    raise FileNotFoundError(f"Nenhum arquivo .txt de entrada encontrado na pasta: {pasta}")
if len(arquivos_entrada) > 1:
    nomes = ", ".join(sorted(arquivo.name for arquivo in arquivos_entrada))
    raise ValueError(f"Há mais de um arquivo .txt de entrada na pasta: {nomes}. Insira um de cada vez.")

arquivo_entrada = arquivos_entrada[0]
try:
    linhas = [int(valor) for valor in arquivo_entrada.read_text(encoding="utf-8").split()]
except ValueError as erro:
    raise ValueError(f"O arquivo {arquivo_entrada.name} deve conter apenas valores inteiros.") from erro

if not linhas or len(linhas) % 2 != 0:
    raise ValueError("Valores incorretos. O programa exige 2 valores: o tempo de chegada e tempo de duração de cada processo. Insira-os corretamente.")



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


#começo trecho antigo
# Chamada das funções passando a matriz processos como atribuição em um for
# print("------FCFS------")
# fcfs.processes = []
# for i in range(len(processos)):
#     fcfs.processes.append({
#         'pid': f'P{processos[i][0]}',
#         'arrival': processos[i][1],
#         'burst': processos[i][2]
#     })
# fcfs.result = fcfs.fcfs(fcfs.processes)
# fcfs.print_results(fcfs.result)
# print("----------------\n\n")


# print("------SJF------")
# sjf.processes = []
# for i in range(len(processos)):
#     sjf.processes.append({
#         'pid': f'P{processos[i][0]}',
#         'arrival': processos[i][1],
#         'burst': processos[i][2]
#     })
# sjf.result = sjf.sjf(sjf.processes)
# sjf.print_results(sjf.result)
# print("---------------\n\n")


# print("-------RR-------")
# rr.processes = []
# for i in range(len(processos)):
#     rr.processes.append({
#         'pid': f'P{processos[i][0]}',
#         'arrival': processos[i][1],
#         'burst': processos[i][2]
#     })
# rr.result = rr.round_robin(rr.processes, quantum=2)
# rr.print_results(rr.result)
# print("----------------")

# paragrafos = [
#     {'FCFS',},
#     {'SJF', },
#     {'RR', }
# ]
#fim trecho antigo

#trecho novo

#sugestão de mudança esse trecho substitui a parte acima
def criarProcessos(matriz):
    return [
        {
            'pid': f'P{p[0]}',
            'arrival': p[1],
            'burst': p[2]
            }
        for p in matriz
        ]


# Função pra calcular as médias
def calcularMedias(processos): 
    quantidade = len(processos)

    if quantidade == 0:
        raise ValueError("Não existem processos para calcular") #tratamento de excessão pq sempre é bom né

    mediaRetorno = sum(p['turnaround'] for p in processos) / quantidade
    mediaResposta = sum(p['response'] for p in processos) / quantidade
    mediaEspera = sum(p['wait'] for p in processos) / quantidade

    return mediaRetorno, mediaResposta, mediaEspera

def formatarResultado(nome, medias):
    retorno, resposta, espera = medias

    valores = f"{retorno:.1f}{resposta:.1f}{espera:.if}" #limita a uma casa decimal
    valores = valores.replace('.',',') #troca o . do inglês pra , br

    return f"{nome} {valores}"

#executando só q bonito
resultadoFCFS = fcfs.fcfs(criarProcessos(processos))
resultadoSJF = sjf.sjf(criarProcessos(processos))
resultadoRR = rr.round_robin(criarProcessos(processos), quantum=2)

#medias
mediaFCFS = calcularMedias(resultadoFCFS)
mediaSJF = calcularMedias(resultadoSJF)
mediaRR = calcularMedias(resultadoRR)

#imprimir na tela
print(formatarResultado("FCFS"), mediaFCFS)
print(formatarResultado("SJF", mediaSJF))
print(formatarResultado("RR", mediaRR))

#aqui tbm foi alterado pelo novo funcionamento
# Criação do arquivo "resultado.txt" com os resultados das médias conforme pedido na especificação do projeto
# with open("resultado.txt", "w", encoding= "utf-8") as p:
#     for i in range(len(paragrafos)):
#         p.writelines(f"{paragrafos[i]}")
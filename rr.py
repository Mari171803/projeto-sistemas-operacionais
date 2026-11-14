def round_robin(processes, quantum):

    processes.sort(key=lambda p: p ['arrival'])

    for p in processes:
        p['remaining'] = p['burst']
        p['start'] = None

    queue = []
    current_time = 0
    completed = []

    while processes or queue:

        if not queue: #avança o relogio até a proxima chegada se não tiverm processos disponiveis
            current_time = max(
                current_time,
                processes[0]['arrival']
            )

        while processes and processes[0]['arrival'] <= current_time: #adiciona os processos q ja chegaram
            queue.append(processes.pop(0))

        current = queue.pop(0) #seleciona o próximo processo

        if current['start'] is None:
            current['start'] = current_time  # Primeira vez que executa

            current['response'] = current['start'] - current['arrival']

        executionTime = min(quantum, current['remaining']) #executa por um quantum ou pelo q falta pra o processo acabar, o q for menor

        current_time += executionTime
        current['remaining'] -= executionTime

        while processes and processes[0]['arrival'] <= current_time: #adiciona os que chegam durante a execução, eu sei q ta repetido, é assim mesmo
            queue.append(processes.pop(0))

        if current['remaining'] == 0:
            current['finish'] = current_time 

            current['turnaround'] = current['finish'] - current['arrival']
            
            current['wait'] = current['turnaround'] - current['burst']

            completed.append(current)
        else:
            queue.append(current) #não terminou volta pra fila querido

    return completed

def print_results(processes):
    total_wait = 0
    total_turnaround = 0
    resposta = 0

    print("\n{:^7} {:^10} {:^12} {:^10} {:^10} {:^10} {:^10}".format(
        "PID", "Chegada", "Execução", "Response", "Término", "Espera", "Retorno"
    ))
    print("-" * 70)

    for p in processes:
        print("{:^7} {:^10} {:^12} {:^10} {:^10} {:^10} {:^10}".format(
            p['pid'],
            p['arrival'],
            p['burst'],
            p['response'],  # NABO PRA TODO MUNDO!!! PEGUE JA SEU NABO!!
            p['finish'],
            p['wait'],
            p['turnaround']
        ))
        total_wait += p['wait']
        total_turnaround += p['turnaround']
        resposta += p['response']
        
    print("\nMédia Retorno: {:.2f}".format(resposta / len(processes)))
    print("Média Resposta: {:.2f}".format(total_wait / len(processes)))
    print("Média Espera: {:.2f}".format(total_wait / len(processes)))

# Exemplo de uso
if __name__ == "__main__":
    processes = [
        {'pid': 'P1', 'arrival': 0, 'burst': 5},
        {'pid': 'P2', 'arrival': 1, 'burst': 3},
        {'pid': 'P3', 'arrival': 2, 'burst': 8}
    ]
    result = round_robin(processes, quantum=2)
    print_results(result)
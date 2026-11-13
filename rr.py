def round_robin(processes, quantum):

    inputArray = [] #criar um array separado de processes pode ser desnecessário mas pelo menos vc trouxe o bode né? o premiado la
    inputArray = processes.sort(key=lambda p: p ['arrival'])

    for p in inputArray:
        p['remaining'] = p['burst']
        p['start'] = None

    queue = []
    current_time = 0
    completed = []

    while inputArray or queue:

        if not queue: #avança o relogio até a proxima chegada se não tiverm processos disponiveis
            current_time = max(
                current_time,
                inputArray[0]['arrival']
            )

        while inputArray and inputArray[0]['arrival'] <= current_time: #adiciona os processos q ja chegaram
            queue.append(inputArray.pop(0))

        current = queue.pop(0) #seleciona o próximo processo

        if current['start'] is None:
            current['start'] = current_time  # Primeira vez que executa

            current['response'] = current['start'] - current['arrival']

        if current['remaining'] > quantum:
            current_time += quantum
            current['remaining'] -= quantum
            queue.append(current)
        else:
            current_time += current['remaining']
            current['finish'] = current_time
            current['turnaround'] = current_time - current['arrival']
            current['wait'] = current['turnaround'] - current['burst']
            completed.append(current)

    return completed

def print_results(processes):
    total_wait = 0
    total_turnaround = 0

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

    print("\nMédia Espera: {:.2f}".format(total_wait / len(processes)))
    print("Média Retorno: {:.2f}".format(total_turnaround / len(processes)))

# Exemplo de uso
if __name__ == "__main__":
    processes = [
        {'pid': 'P1', 'arrival': 0, 'burst': 5},
        {'pid': 'P2', 'arrival': 1, 'burst': 3},
        {'pid': 'P3', 'arrival': 2, 'burst': 8}
    ]
    result = round_robin(processes, quantum=2)
    print_results(result)
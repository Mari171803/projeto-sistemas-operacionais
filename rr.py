def round_robin(processes, quantum):
    for p in processes:
        p['remaining'] = p['burst']
        p['start'] = None
    queue = processes.copy()
    current_time = 0
    completed = []

    while queue:
        current = queue.pop(0)
        if current['start'] is None:
            current['start'] = current_time  # Primeira vez que executa

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
        "PID", "Chegada", "Execução", "Prioridade", "Término", "Espera", "Retorno"
    ))
    print("-" * 70)

    for p in processes:
        print("{:^7} {:^10} {:^12} {:^10} {:^10} {:^10} {:^10}".format(
            p['pid'],
            p['arrival'],
            p['burst'],
            "-",  # Prioridade não se aplica ao RR
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
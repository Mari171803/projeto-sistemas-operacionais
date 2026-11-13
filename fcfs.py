def fcfs(processes):
    # Ordena por tempo de chegada
    processes.sort(key=lambda x: x['arrival'])

    current_time = 0
    for p in processes: #tratamento de cada processo
        if current_time < p['arrival']:
            current_time = p['arrival']

        p['start'] = current_time
        p['response'] = p['start'] - p['arrival'] # O mel ta acabando!
        p['finish'] = current_time + p['burst']
        p['wait'] = current_time - p['arrival']
        p['turnaround'] = p['finish'] - p['arrival']
        current_time = p['finish']

    return processes

def print_results(processes): #função para para printar resultados de testes, não usada na criação do arquivo resposta
    total_wait = 0
    total_turnaround = 0

    print("\n{:^7} {:^10} {:^12} {:^10} {:^10} {:^10} {:^10} {:^10}".format(
        "PID", "Chegada", "Execução", "Resposta", "Início", "Término", "Espera", "Retorno"
    ))
    print("-" * 80)

    for p in processes:
        print("{:^7} {:^10} {:^12} {:^10} {:^10} {:^10} {:^10} {:^10}".format(
            p['pid'],
            p['arrival'],
            p['burst'],
            p['response'],  # e o mel? eu acho q ta acabando ein... # mesmo o algoritimo n usando prioridade, vale a pena mostrar tudo 
            p['start'],
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
    result = fcfs(processes)
    print_results(result)
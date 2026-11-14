def sjf(processes):
    processes.sort(key=lambda x: x['arrival']) #organização por ordem de chegada

    current_time = 0
    completed = []
    ready_queue = []
    
    while processes or ready_queue: #loop principal, funciona enquanto tiverem processos que n chegaram ou aguardando execução
        while processes and processes[0]['arrival'] <= current_time: #inserção de projetos na fila de prontos
            ready_queue.append(processes.pop(0))
        
        if ready_queue: #seleção e tratamento do menor processo

            ready_queue.sort(key=lambda x: x['burst'])
            current = ready_queue.pop(0)

            current['start'] = current_time

            current['response'] = current['start'] - current['arrival']
            current['finish'] = current_time + current['burst']
            current['wait'] = current_time - current['arrival']
            current['turnaround'] = current['finish'] - current['arrival']
            current_time = current['finish']
            completed.append(current)
        else: #tratamento do caso CPU desocupada
            current_time = processes[0]['arrival'] #na teoria pula pra o começo do proximo processo, isso deixa o código mais eficiente porém menos fidedigno, fica ou n fica?
            #current_time += 1 #vc viu se ela tava com um bode? um bem branquinho... bonitinho... :)
    
    return completed

def print_results(processes): #função para colher dados e identificar erros, não usada na criação do resultado final
    total_wait = 0
    total_turnaround = 0

    print("\n{:^7} {:^10} {:^12} {:^10} {:^10} {:^10} {:^10} {:^10}".format(
        "PID", "Chegada", "Execução", "Prioridade", "Início", "Término", "Espera", "Retorno"
    ))
    print("-" * 80)

    for p in processes:
        print("{:^7} {:^10} {:^12} {:^10} {:^10} {:^10} {:^10} {:^10}".format(
            p['pid'],
            p['arrival'],
            p['burst'],
            "-",  # Prioridade não se aplica ao SJF
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
    result = sjf(processes)
    print_results(result)
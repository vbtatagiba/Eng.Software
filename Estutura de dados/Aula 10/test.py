import heapq

def dijkstra(graph, start, end):
    # Inicializa o dicionário de distâncias com valores infinitos para todos os nós
    distances = {node: float('inf') for node in graph}
    # A distância do nó inicial é zero
    distances[start] = 0
    # Inicializa a fila de prioridade com o nó inicial
    pq = [(0, start)]
    
    while pq:
        # Remove o nó com a menor distância da fila de prioridade
        current_distance, current_node = heapq.heappop(pq)
        
        # Se chegamos ao nó final, retornamos a distância correspondente
        if current_node == end:
            return current_distance
        
        # Itera sobre os vizinhos do nó atual
        for neighbor, weight in graph[current_node].items():
            # Calcula a nova distância para o vizinho
            distance = current_distance + weight
            # Se a nova distância for menor do que a distância atual, atualizamos a distância e adicionamos o vizinho na fila de prioridade
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    # Se não encontramos um caminho entre os nós, retorna None
    return None

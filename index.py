import json

# Carrega o JSON com as distâncias entre as cidades
with open("cidadesSCDistâncias (1).json", 'r', encoding='utf-8') as f:
    mapa_cidades = json.load(f)

def guloso_menor_caminho(mapa, origem, destino):
    caminho = [origem]
    cidade_atual = origem
    cidades_visitadas = {origem}  # Conjunto para armazenar cidades já percorridas
    
    while cidade_atual != destino:
        if cidade_atual not in mapa:
            print(f"❌ Cidade inválida: {cidade_atual}")
            return None
        
        vizinhos = mapa[cidade_atual].copy()  # Cópia para evitar modificar o JSON original
        
        # Remove cidades já visitadas
        vizinhos = {cidade: distancia for cidade, distancia in vizinhos.items() if cidade not in cidades_visitadas}

        if not vizinhos:  # Se não houver vizinhos disponíveis, não há caminho possível
            print(f"🚧 O caminho tentado foi:", caminho)
            print(f"🚧 Sem saída a partir de {cidade_atual}. Caminho interrompido.")
            return None

        # Escolhe o vizinho com a menor distância
        proxima_cidade = min(vizinhos, key=vizinhos.get)
        caminho.append(proxima_cidade)
        cidades_visitadas.add(proxima_cidade)  # Marca a cidade como visitada
        cidade_atual = proxima_cidade
    
    return caminho

# Testar o algoritmo
origem = "Ilhota"
destino = "Imaruí"
caminho_encontrado = guloso_menor_caminho(mapa_cidades, origem, destino)

print("🗺️ Caminho encontrado:", caminho_encontrado)

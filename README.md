﻿# Algoritmo Guloso para Menor Caminho entre Cidades

Este repositório contém um algoritmo guloso que encontra o menor caminho entre duas cidades usando um mapa de distâncias armazenado em um arquivo JSON.

## Como funciona

O algoritmo segue uma abordagem gulosa, escolhendo sempre a cidade vizinha com a menor distância até o destino. Ele funciona da seguinte forma:

1. **Inicia na cidade de origem** e adiciona ela ao caminho.
2. **Verifica os vizinhos** da cidade atual e remove aqueles que já foram visitados.
3. **Seleciona o vizinho mais próximo** (com a menor distância) e move-se para essa cidade.
4. **Repete o processo** até alcançar o destino ou ficar sem opções de caminho.
5. **Retorna o caminho encontrado** ou informa que não há caminho possível.

## Requisitos

- Python 3.x
- Um arquivo JSON contendo o mapa de cidades e suas distâncias.

## Como usar

1. Certifique-se de ter o arquivo `cidadesSCDistâncias (1).json` no mesmo diretório do script.
2. Execute o script Python:

   ```sh
   python script.py
   ```

3. O código imprimirá o caminho encontrado, se houver um caminho válido entre as cidades escolhidas.

## Exemplo de Entrada/Saída

**Entrada:**

```python
origem = "Ilhota"
destino = "Imaruí"
caminho_encontrado = guloso_menor_caminho(mapa_cidades, origem, destino)
print("🗺️ Caminho encontrado:", caminho_encontrado)
```

**Saída esperada:**

```
🗺️ Caminho encontrado: ['Ilhota', 'CidadeX', 'CidadeY', 'Imaruí']
```

Se não houver um caminho possível, o programa avisará e interromperá a busca.

## Limitações

- O algoritmo pode não encontrar o caminho ótimo, pois sempre escolhe o vizinho mais próximo sem considerar o destino final globalmente.
- Se houver ciclos ou cidades sem saída, o algoritmo pode falhar em encontrar um caminho.

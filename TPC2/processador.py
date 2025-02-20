import re

def processar_obras(filename):
    compositores = set()
    distribuicao_periodo = {}
    obras_por_periodo = {}

    padrao = r';(?=(?:[^"]*"[^"]*")*[^"]*$)'

    with open(filename, 'r', encoding='utf-8') as file:
        next(file)
        linha_completa = ""
        
        for line in file:
            linha_completa += line.strip()
            
            if linha_completa.count(";") >= 6:
                campos = re.split(padrao, linha_completa)
                linha_completa = ""

                nome_obra = campos[0].strip()
                periodo = campos[3].strip()
                compositor = campos[4].strip()


                compositores.add(compositor)

                distribuicao_periodo[periodo] = distribuicao_periodo.get(periodo, 0) + 1

                if periodo not in obras_por_periodo:
                    obras_por_periodo[periodo] = []
                obras_por_periodo[periodo].append(nome_obra)

    compositores_ordenados = sorted(compositores)

    for periodo in obras_por_periodo:
        obras_por_periodo[periodo].sort()

    return compositores_ordenados, distribuicao_periodo, obras_por_periodo

def escrever_resultados(filename, compositores, distribuicao, obras_por_periodo):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("Lista ordenada alfabeticamente dos compositores:\n")
        for compositor in compositores:
            file.write(compositor + "\n")

        file.write("\nDistribuição das obras por período:\n")
        for periodo, quantidade in distribuicao.items():
            file.write(f"{periodo}: {quantidade} obras\n")

        file.write("\nDicionário com listas alfabéticas dos títulos das obras por período:\n")
        for periodo, obras in obras_por_periodo.items():
            file.write(f"{periodo}:\n")
            for obra in obras:
                file.write(f"  - {obra}\n")
            file.write("\n")

file_path = "obras.csv"
output_path = "resultados.txt"

compositores_ordenados, distribuicao_periodo, obras_por_periodo = processar_obras(file_path)

escrever_resultados(output_path, compositores_ordenados, distribuicao_periodo, obras_por_periodo)

print(f"Resultados gravados em {output_path}")

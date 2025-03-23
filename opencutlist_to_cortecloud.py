import csv
import sys

if len(sys.argv) <= 2:
    print("Utilitário de conversão do OpenCutList do SketchUp para o padrão do CorteCloud")
    print("Uso: python opencutlist_to_cortecloud.py csv_input csv_output")
    print("Por: Fernando Birck (Fergo) - 2025")
else:
    entrada = sys.argv[1]
    saida = sys.argv[2]

    with open(entrada) as csv_entrada:
        csv_reader = csv.reader(csv_entrada, delimiter=';')

        # nem seria necessario todo esse dicionario, mas criei pensando em funcionalidades futuras
        pecas = []
        for row in csv_reader:
            if row[9] == "Sheet Goods":
                pecas.append({
                    'quantidade' : row[0],
                    'comprimento'  : row[1].replace("mm", ""),
                    'largura'  : row[2].replace("mm", ""),
                    'funcao'  : row[3],
                    'c1'  : row[4],
                    'c2'  : row[5],
                    'l1'  : row[6],
                    'l2'  : row[7],
                    'material'  : row[8],
                    'complemento'  : row[3],
                    'girar': ""
                })

    with open(saida, 'w') as csv_saida:
        saida_formatada = []
        saida_formatada += ["\t".join(str(coluna) for coluna in peca.values()) for peca in pecas]  
        csv_saida.write("\n".join(saida_formatada))

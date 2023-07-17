# ====================================================================================================

import json
import csv

# ====================================================================================================


# FUNÇÕES:


def calcula_indices_ano(arquivos, indices):

    violentos = {} 
    nao_violentos = {}
    indice_violento = 0
    indice_nao_violento = 0

    for tabela in arquivos:

        leitor = csv.DictReader(tabela, delimiter=";")

        for linha in leitor:

            if linha["Municipios"] == "ACEGUA":

                if indice_violento > 0 and indice_nao_violento > 0:

                    indice_violento = 0
                    indice_nao_violento = 0

                    for crime in indices["violentos"]:

                        indice_violento += int(linha[crime]) * int(indices["violentos"][crime])
                    
                    for crime in indices["nao_violentos"]:

                        indice_nao_violento += int(linha[crime]) * int(indices["nao_violentos"][crime])
            
            else:

                for crime in indices["violentos"]:

                    indice_violento += int(linha[crime]) * int(indices["violentos"][crime])
                
                for crime in indices["nao_violentos"]:

                    indice_nao_violento += int(linha[crime]) * int(indices["nao_violentos"][crime])
                    
            if tabela == csv_21:

                violentos["2021"] = indice_violento
                nao_violentos["2021"] = indice_nao_violento

            elif tabela == csv_22:

                violentos["2022"] = indice_violento
                nao_violentos["2022"] = indice_nao_violento
                
            elif tabela == csv_23:

                violentos["2023"] = indice_violento
                nao_violentos["2023"] = indice_nao_violento

    return violentos, nao_violentos


def print_indicaores_globais_ano(violentos, nao_violentos):

    print()
    print("---------------------------------------------------------") 
    print("              Indicadores globais por ano              ") 
    print("---------------------------------------------------------")
    print()
    print("Crimes violentos")

    for ano in violentos:

        print(f"- {ano}: {violentos[ano]}")

    print("\nCrimes não violentos")

    for ano in nao_violentos:

        print(f"- {ano}: {nao_violentos[ano]}")


def calcula_indices_acidades(arquivos, indices):

    violentos = {}
    nao_violentos = {}

    for tabela in arquivos:

        i = 1

        leitor = csv.DictReader(tabela, delimiter=";")

        for linha in leitor:

            indice_violento = 0
            indice_nao_violento = 0

            municipio = linha["Municipios"]

            for crime in indices["violentos"]:

                indice_violento += int(linha[crime]) * int(indices["violentos"][crime])

            if tabela != csv_21:

                violentos[municipio] += indice_violento

            else:

                violentos[municipio] = indice_violento

            for crime in indices["nao_violentos"]:

                indice_nao_violento += int(linha[crime]) * int(indices["nao_violentos"][crime])

            if tabela != csv_21:

                nao_violentos[municipio] += indice_nao_violento
            
            else:

                nao_violentos[municipio] = indice_nao_violento
                

    return violentos, nao_violentos
            
        
def ranking(dicionario, n, crescente=True):

    # dec = decrescente
    # cre = crescente
    
    if crescente:
        
        print("\n---------------------------------------------------------")
        
        if dicionario == crimes_violentos_cidades:

            print(f"Top {n} cidade(s) com menor indice de crimes violentos")
        
        else:

            print(f"Top {n} cidade(s) com menor indice de crimes não violentos")

        print("---------------------------------------------------------")

        rank = sorted(dicionario, key=dicionario.get)
    
    else:
        
        print("\n---------------------------------------------------------")
        
        if dicionario == crimes_violentos_cidades:

            print(f"Top {n} cidade(s) com maior indice de crimes violentos")
        
        else:

            print(f"Top {n} cidade(s) com maior indice de crimes não violentos")

        print("---------------------------------------------------------")
        
        rank = sorted(dicionario, key=dicionario.get, reverse=True)

    for i in range(n):

        print(f"{i + 1:02} - {rank[i]}: {dicionario[rank[i]]}")

    print()


def salvar_json(dicionario, arquivo_json):

    try: 

        with open(arquivo_json, 'w') as arquivo:

            json.dump(dicionario, arquivo, indent=6)

        print("Arquivo '.json' salvo com sucesso")

    except OSError:

        print("Erro ao salvar arquivo")


# ====================================================================================================


# VARIÁVEIS E CONSTANTES:


src_21 = "/home/eduardo/Documents/ATITUS/python-atitus/trab_avaliativos/seguranca_pub/jan-21.CSV"

src_22 = "/home/eduardo/Documents/ATITUS/python-atitus/trab_avaliativos/seguranca_pub/jan-22.CSV"

src_23 = "/home/eduardo/Documents/ATITUS/python-atitus/trab_avaliativos/seguranca_pub/jan-23.CSV"

src_json_v = "/home/eduardo/Documents/ATITUS/python-atitus/trab_avaliativos/seguranca_pub/crimes_violentos.json"

src_json_nv = "/home/eduardo/Documents/ATITUS/python-atitus/trab_avaliativos/seguranca_pub/crimes_nao_violentos.json"

crimes = {
    "violentos": {
                  "Vitimas de Homicidio Doloso": 10,
                  " Roubos": 2,
                  " Roubo de Veiculo": 3,
                  " Delitos Relacionados a Armas e Municoes": 2,
                  " Entorpecentes Trafico": 5,
                  "Vitimas de Latrocinio": 10,
                  "Vitimas de Lesao Corp Seg Morte": 10
                 },

    "nao_violentos": {
                      " Furtos": 3,
                      "Furto de Veiculo ": 3,
                      " Estelionato": 1,
                      " Entorpecentes Posse": 2
                     }
}


# ====================================================================================================


# PROGRAMA PRINCIPAL:


try:
        
    with open(src_21, "r", encoding="utf-8") as csv_21, open(src_22, "r", encoding="utf-8") as csv_22, open(src_23, "r", encoding="utf-8") as csv_23:

        arquivos = [csv_21, csv_22, csv_23]
        
        indice_crimes_violentos_ano, indice_crimes_nao_violentos_ano = calcula_indices_ano(arquivos, crimes)
        

    with open(src_21, "r", encoding="utf-8") as csv_21, open(src_22, "r", encoding="utf-8") as csv_22, open(src_23, "r", encoding="utf-8") as csv_23:

        arquivos = [csv_21, csv_22, csv_23]

        crimes_violentos_cidades, crimes_nao_violentos_cidades = calcula_indices_acidades(arquivos, crimes)
            

    print_indicaores_globais_ano(indice_crimes_violentos_ano, indice_crimes_nao_violentos_ano)    

    ranking(crimes_violentos_cidades, 20, False)
    ranking(crimes_violentos_cidades, 15)    
    ranking(crimes_nao_violentos_cidades, 50, False)
    ranking(crimes_nao_violentos_cidades, 7)

    salvar_json(crimes_violentos_cidades, src_json_v)
    salvar_json(crimes_nao_violentos_cidades, src_json_nv)
             

except OSError:

    print("Erro ao abrir o arquivo!")







# ====================================================================================================
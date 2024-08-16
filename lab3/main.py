"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 I M P O R T S   I M P O R T S   I M P O R T S   I M P O R T S   I M P O R T S   I M P O R T S   I M P O R T S
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from processos import *

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 M A I N   M A I N   M A I N   M A I N   M A I N   M A I N   M A I N   M A I N   M A I N   M A I N   M A I N  
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

nomes =     []
# nomes +=    ["test1" , "test2" , "test3" , "test4"]
nomes +=    ["frankestein", "war_and_peace"]

for nome in nomes:
    print(f" Nome: {nome}")

    print("     Ordenando")
    criar_sorted(nome)

    print("     Contando repetições")
    criar_counted(nome)

    print("     Criando ranque")
    criar_ranked(nome)

print("Processo finalizado!")

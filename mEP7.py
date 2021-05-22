def entrada(nome=[0],votos=[],eleitores=0,N=0,i=0,x=0,y=1):
    """Essa função valida a entrada e retorna 
    cada valor gerado para a função chamada."""
    if i == 0:
        print("Em caso de empate o primeiro candidato será eleito.")
        N = int(input("Informe quantos candidatos vão participar: "))
    
    if N <= 1 or N >= 101:
        return nome,votos,eleitores,N
    
    if 2 <= N <=100 and N != i:
        nomeCandidatos = input(f"Nº {y} do candidato: ")
    
    if i == N and eleitores == 0:
        eleitores = int(input("Quantidade de eleitores: "))
   
    if x < eleitores:
        if x == 0:
            print("Vote no respectivo número do candidato.")
        voto = int(input())
        return entrada(nome,votos+[voto],eleitores,N,i,x+1)
    
    if x == eleitores and eleitores > 0:
        return nome,votos,eleitores,N
    
    return entrada(nome+[nomeCandidatos],votos,eleitores,N,i+1,x,y+1)
   
def votosBrancos(votos,eleitores,i=0,branco=0):
    """Essa função conta os votos brancos da votação e retorna o seu resultado para 
    a função imprimeVotosCandidatos."""
    if i == eleitores:
        return branco
    
    if votos[i] == 0:
        branco +=1
    
    return votosBrancos(votos,eleitores,i+1,branco)

def contaVotos(votos,i,x=0,voto=0):
    """A função contaVotos, conta os votos de cada candidato e retorna seu resultado
    para a função imprimeVotosCandidatos."""
    if x == len(votos):
        return voto

    if i == votos[x]:
        voto +=1

    return contaVotos(votos, i, x+1,voto)

def contaNulos(nome,votos,i,x=0,nulos=0):
    """Essa função Conta a quantidade de votos nulos da votação e retorna 
    para a função imprimeVotosCandidatos."""
    if x == len(votos):
        return nulos
    
    if votos[x] >= i:
        nulos+=1

    return contaNulos(nome, votos, i,x+1,nulos)

def retornaVencedor(listaCandidato,listaVoto,x=0,i=0,s=[]):
    """Essa função valida o vencedor fazendo a conta dos votos gerados pela função
    contavotos e retorna o respectivos candidato que teve mais votos."""
    if i == len(listaVoto):
        return f"Vencedor(a): {listaCandidato[x]}"
    
    elif listaVoto[x] >= listaVoto[i]:
        return retornaVencedor(listaCandidato,listaVoto,x,i+1,s=listaVoto[x])
    
    elif listaVoto[x] < listaVoto[i]:
        return retornaVencedor(listaCandidato,listaVoto,x+1)

    return retornaVencedor(listaCandidato,listaVoto,x,i+1)

def imprimeVotosCandidatos(nome,votos,eleitores,i=1,listaVoto=[],listaCandidato=[],x=0):
    """Essa função recebe cada valor gerado pelas funções chamadas e
    imprime todos os resultados da votação"""
    if i < len(nome):
        candidato = nome[i]
        voto = contaVotos(votos,i)
        if x == 0:
            print("--> Votos de cada candidato <--")
        print(f"{candidato}: {voto}")
        listaVoto+=[voto]
        listaCandidato+=[candidato]
    
    if i == len(nome):
        print("--> Votos Brancos e Nulos <--")
        print(f"Brancos: {votosBrancos(votos,eleitores)}")
        nulos = contaNulos(nome,votos,i)
        print(f"Nulos: {nulos}")
        vencedor = retornaVencedor(listaCandidato,listaVoto)
        print("     >>>VENCEDOR<<<")
        print(vencedor)
        return
    
    return imprimeVotosCandidatos(nome, votos, eleitores, i+1,listaVoto,listaCandidato,x=1) 

def chamada():
    """Chama a função de entrada e depois armazena seus valores retornados,
    para serem utilizados na função imprimeVotosCandidatos."""
    nome,votos,eleitores,N=entrada()
    if N <= 1 :
        return
    if N != 1:
        imprimeVotosCandidatos(nome,votos,eleitores)
        
def main():
    """Chama a função que irá começar tudo."""
    chamada() 

main()
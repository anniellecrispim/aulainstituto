#fazendo uma 'main' no interpretador

print("Olá usuário! Qual o seu nome?\nPode digitar sem medo")
nome = input() 
print("Seja bem vindo ao mundo da Revisão " + nome +"\n Quaantos anos você tem?")
idade = int(input())

#fazendo uma condicional com vários if *bad pratice 

if idade < 90 and idade > 60:
    print("parabéns você é jovem!!! Não é idade chegando que vai te parar jovem gafanhoto")

elif idade >= 30:
    print ("Não deixe a crise dos 30 te animar, vocÊ ainda é uma criança")

elif idade < 20:
    print("pelo amor de Deus você ainda é um bebê. Aproveite o tempo serumaninho!")

else:
    print ("Sinal que viveu muito!!!! Sempre seremos jovens se nosso coração aspirar a ser!")

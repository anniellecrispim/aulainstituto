print('Desafio em Squads')


nomePaula = ('PAULA MARTINS')
mesPaula = ('JANEIRO') #variavel é mes_paula, mesPaula é padrão Java mas também pode ser usado 
compraPaula = 500,00
descontoPaula = 10
cupomPaula = ('PAULAÉ10')
print ('Olá', nomePaula, '. Em', mesPaula, 'você realizou uma compra no valor de R$ ', compraPaula, 'e ganhou um desconto de', descontoPaula, '% em sua próxima compra. Use o cupom', cupomPaula) #separando por vírgulas

print (f'Olá {nomePaula}. Em {mesPaula} você realizou uma compra no valor de R$ {compraPaula} e ganhou um desconto de {descontoPaula}% em sua próxima compra. Use o cupom {cupomPaula}') #primeiro Format
print ('Olá {}. Em {} você realizou uma compra no valor de R$ {} e ganhou um desconto de {}% em sua próxima compra. Use o cupom {}'.format(nomePaula,mesPaula, compraPaula, descontoPaula, cupomPaula)) #segundo Format
print ('Olá %s. Em %s você realizou uma compra no valor de R$ %s e ganhou um desconto de %s%% em sua próxima compra. Use o cupom %s' % (nomePaula, mesPaula, compraPaula, descontoPaula, cupomPaula)) #formart3

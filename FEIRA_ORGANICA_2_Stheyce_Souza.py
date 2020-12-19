from math import fsum
produtos = ['FOLHAS E HORTALIÇAS','','','','Alface americano',2.20,'Alface crespa',2.50,'Alho poró',2.00,'Capim santo',2.50,'Cebola',3.00,'Cebolinha',2.50,'Coentro',2.50,
'Couve folha',2.50,'Chinguezay (acelga chinesa)',3.00,'Espinafre',3.00,'Hortelã',2.50,'Salsinha',2.50,'Rúcula',2.50,'','', 'FRUTAS','','','',
'Banana pacovam(uni)',0.25,'Cana(saco)',2.00,'Laranja Comum (4uni)',2.00,'Laranja mimo(uni)',2.00,'Maracujá(1k)',7.00,'','','RAIZER, TUBERCULOS, LEGUMES E AFINS','','','',
'Batata doce',4.00,'Cara',5.00,'Cenoura',3.00,'Jerimum',5.00,'Macaxeira',4.00,'Rabanete',2.50,'Quiabo 15 unidades',2.00,'','','OUTROS','','','','Fava seca',
12.00,'Mel italiano 250gr',20.00,'Mel italiana 500 gr',35.00,'Mel no favo 450 gramas',25.00,'Ovos de capoeira unidade',1.00,'Polpa de cajá',6.00,
'Própolis 20ml', 16.00,'Pão sem trigo (grande)',13.00,'Pão com trigo (grande)',13.00,'Pão com trigo (pequeno)',7.00,'Bolo (sem trigo)',10.00,
'Bolinho de bacia (c/trigo)',2.00,'Mini pizza (a unidade)',3.00,'Pizza brotinho (a unidade)',5.00,'Bolacha com trigo',5.00,'Sucos sem açúcar (200 ml)',
3.00,'Sucos com açúcar (200 ml)',3.00,'Sucos com ou sem açucar (1 litro)',10.00,'Refeições congeladas (500 gr)',12.00,' Refeições congeladas (750 gr)',
15.00,'Hambúrguer de ora-pro-nóbis 6 unidades',12.00,'Molhos prontos',10.00,'Massa artesanal (lasanha ou taglatelle)',12.00,'','','PASTILHAS/GELEIAS','','','',
'Pepita de girassol',5.00,'Homus de grão de bico com paprika',5.00,'Bisnaga maionese de pepita girassol (250 ml)',10.00,'Pimentas ao mel de engenho',
15.00,'Confit de tomatinho, pimenta, pimento ou berinjela',15.00,'Geleia de tomate com pimenta abacaxi/ manga',15.00,'Caponata Siciliana','13.00',
'','','LANCHES SEM TRIGO','','','','quiiche de macaxeira c/ alho poró',5.00,'Quiche de macaxeira tomate seco',5.00,'Sanduíche sem glúten de ricota',6.00,
'Sanduiche sem glúten de caponata Siciliana',6.00,'Sanduiche sem glúten de ragu',6.00,'','','LANCHE COM TRIGO','','','','Empada de falso camarão',5.00,
'Empada de antepasto de berinjela',5.00,'Empada de Tofu com cebola caramelizada',5.00,'Pãozinhos de inhame recheados',5.00]

coisas=list()
lista_preços = []
quant=0
sair=0


while sair != 4:
    print('')
    print('BEM VINDO A FEIRA ORGANICA')
    print('='*30)
    print('''MENU DE OPÇÕES
        1- produtos
        2-pagamento
        3-carrinho
        4-finalizar compras
        5-sair''')
    print('='*30)


    menu = int(input('Qual opção deseja?'))
    print('')
    if menu == 1:
        print('')
        for i in range(0,len(produtos)):
            if i % 2 == 0:
                print(f'{produtos[i]:.<50}', end='')
            else:
                print(f'R$ {produtos[i]:>5}')
        while True:
            print('')
            produto = str(input("Qual o nome do produto?"))
            print('')
            coisas.append(produto)
            quant=quant+1
            preço = float(input("Qual o preço do produto?"))
            print('')
            lista_preços.append(preço)
            if preço > 1000:
                produtos_1000 += 1

            continuar = " "
            while continuar not in 'SN':
                continuar = str(input("Adicionar mais produtos?[S/N]")).strip().upper()
            if continuar == 'N':
                break
    
    if menu == 2:
        print('*'*30)
        print('''
        1-cartão
        2- Dinheiro
        ''')
        print('*'*30)
        pagamento= int(input('Qual a forma de pagamento?'))
        if pagamento == 1:
            print('*'*30)
            print('''
            -debito
            -credito
            ''')
            print('*'*30)
            tipo=str(input('Débito ou credito?'))
            Nome= str(input('qual é o seu nome?'))
            endereço= str(input('Qual o seu endereço?'))
        else:
            tipo=('Dinheiro')
            Nome= str(input('qual é o seu nome?'))
            endereço= str(input('Qual o seu endereço?'))
    if menu == 3:
        print('-'*30)
        print('SEU CARRINHO')
        print(coisas)
        print(f'a quantidade de produtos foram:{quant}')
        print(f"\nO total gasto na compra foi R${fsum(lista_preços):.2f}")
        print('-'*30)
    if menu == 4:
        print('*-'*30)
        print(f'OBRIGADA PELA PREFERÊNCIA {Nome}')
        print(f'- sua lista de compras: {coisas}') 
        print(f'- o total da sua compra foi:{fsum(lista_preços):.2f}')
        print(f'- forma de pagamento: {tipo}')
        print(f'- seu endereço: {endereço}')
        print('*-'*30)
        break
    if menu == 5:
        break

''' Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''


turno = input('Digite M se você estuda no periodo Matutino , digite V se você estuda no periodo Vespertino V, Digite N se você estuda no periodo Noturno  : ')
turno_maiuscula = turno.upper()

if turno_maiuscula == 'M':
    print('Bom Dia ! ') 
elif turno_maiuscula =='V':
    print('Boa tarde ! ')
elif turno_maiuscula == 'N':
    print('Boa Noite !') 
else:
    print('Valor Inválido !')
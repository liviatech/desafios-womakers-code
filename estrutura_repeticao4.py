'''Implemente um programa que classifique um aluno com base em sua pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário,  reprovado.'''
 
nota = -1
while nota < 0 or nota > 10:
    nota = int(input('Digite uma nota do Exame : '))
         
         
if nota < 7 :
    print('Aluno Reprovado !')
else:
    print('Aluno Aprovado !')

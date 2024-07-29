'''Faça um Programa que peça as quatro notas de 5 alunos, calcule e armazene numa lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.'''

aluno1 = []
nota1_aluno1 = float( input('Digite a primeira nota Aluno 1: ').replace(',', '.'))
aluno1.append(nota1_aluno1)
nota2_aluno1 = float(input('Digite a segunda nota  Aluno 1:').replace(',', '.'))
aluno1.append(nota2_aluno1)
nota3_aluno1 = float(input('Digite a terceira nota  Aluno 1: ').replace(',', '.'))
aluno1.append(nota3_aluno1)
nota4_aluno1 = float(input('Digite e quarta nota  Aluno 1: ').replace(',', '.'))
aluno1.append(nota4_aluno1)

aluno2 = []
nota1_aluno2 = float(input('Digite a primeira nota  Aluno 2: ').replace(',', '.'))
aluno2.append(nota1_aluno2)
nota2_aluno2 = float(input('Digite a segunda nota  Aluno 2:').replace(',', '.'))
aluno2.append(nota2_aluno2)
nota3_aluno2 = float(input('Digite a terceira nota  Aluno 2: ').replace(',', '.'))
aluno2.append(nota3_aluno2)
nota4_aluno2 = float(input('Digite e quarta nota  Aluno 2: ').replace(',', '.'))
aluno2.append(nota4_aluno2)

aluno3 = []
nota1_aluno3 = float(input('Digite a primeira nota  Aluno 3: ').replace(',', '.'))
aluno3.append(nota1_aluno3 )
nota2_aluno3 = float( input('Digite a segunda nota  Aluno 3:').replace(',', '.'))
aluno3.append(nota2_aluno3)
nota3_aluno3 = float(input('Digite a terceira nota  Aluno 3: ').replace(',', '.'))
aluno3.append(nota3_aluno3)
nota4_aluno3= float(input('Digite e quarta nota  Aluno 3: ').replace(',', '.'))
aluno3.append(nota4_aluno3)

aluno4 = []
nota1_aluno4 = float(input('Digite a primeira nota  Aluno 4: ').replace(',', '.'))
aluno4.append(nota1_aluno4)
nota2_aluno4 = float( input('Digite a segunda nota Aluno 4:').replace(',', '.'))
aluno4.append(nota2_aluno4)
nota3_aluno4 = float(input('Digite a terceira nota Aluno 4: ').replace(',', '.'))
aluno4.append(nota3_aluno4)
nota4_aluno4 = float(input('Digite e quarta nota Aluno 4: ').replace(',', '.'))
aluno4.append(nota4_aluno4)

aluno5 = []
nota1_aluno5 = float( input('Digite a primeira nota Aluno 5: ').replace(',', '.'))
aluno5.append(nota1_aluno5)
nota2_aluno5 =float( input('Digite a segunda nota Aluno 5:').replace(',', '.'))
aluno5.append(nota2_aluno5)
nota3_aluno5 = float(input('Digite a terceira nota Aluno 5: ').replace(',', '.'))
aluno5.append(nota3_aluno5)
nota4_aluno5 = float(input('Digite e quarta nota Aluno 5: ').replace(',', '.'))
aluno5.append(nota4_aluno5)
 
media_aluno1 = sum(aluno1) / 4
media_aluno2 = sum(aluno2) / 4
media_aluno3 = sum(aluno3) / 4
media_aluno4 = sum(aluno4) / 4
media_aluno5 = sum(aluno5) / 4


# Listar as médias
medias = [media_aluno1, media_aluno2, media_aluno3, media_aluno4, media_aluno5]

# Contar quantos alunos atingiram a média de 7 ou mais
num_alunos_com_media = sum(1 for media in medias if media >= 7)

print(f'Número de alunos que atingiram a média 7: {num_alunos_com_media}')
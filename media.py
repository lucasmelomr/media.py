alunos=[]
notas=[]
media=[]

for i in range(3):
    alunos.append(input('Insira o nome do aluno {} : '.format((i+1))))
    
for i in range(3):
    notas.append(float(input('Insira a nota de {} : '.format(alunos[(i)]))))
media=sum(notas) 
media=media/len(notas)   
for i in range(3):    
    if notas[(i)] == media:
        print('Parabéns,{}, você ficou na média da turma, que é: {}'.format(alunos[(i)], media))
    elif notas[(i)] > media:
        print('Parabéns,{}, você ficou acima da média da turma, que é: {}'.format(alunos[(i)], media))

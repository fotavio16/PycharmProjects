def notas(*args, sit=False):
    '''
    -> Calcula o Resultado do aluno e sua situação.
    :param args: pode receber várias notas usadas no cáculo
    :param sit: identifica se precisa informar a situação do aluno em caso de True. Padrão é False
    :return: dicionário com: total, maior, menor, média e situaçõa (opcional)
    '''
    resposta = dict()
    total = maior = media = 0
    menor = 10
    for nota in args:
        total += 1
        media += nota
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota
    media = media / total
    resposta['total'] = total
    resposta['maior'] = maior
    resposta['menor'] = menor
    resposta['média'] = media
    if sit:
        if media > 7.:
            resposta['situação'] = 'APROVADO'
        elif media > 5.:
            resposta['situação'] = 'PROVA FINAL'
        else:
            resposta['situação'] = 'REPROVADO'
    return resposta



# Programa Principal
resp = notas(5.4, 8.6, 7.9)
print(resp)
resp = notas(7.4, 9.6, 8.2, 7.9, 10)
print(resp)
resp = notas(8.4, 7.6, 9.2, 8.9, sit=True)
print(resp)
resp = notas(3.4, 5.6, 6.9, sit=True)
print(resp)
resp = notas(3.1, 5.2, 4.5, 3.9, sit=True)
print(resp)
help(notas)

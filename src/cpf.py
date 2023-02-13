import random

while True:
    print('Você deseja inserir [1] ou gerar um CPF [2]?')
    op=input('Insira o número correspondente: ')

    if op=='2':
        CPF_9digi=''
        CPF_10digi=''
        CPF_random=''
        for s in range(9):
            CPF_random+=str(random.randint(0,9))
            
                           
        CPF_9digi=CPF_random
        
       


    elif op=='1':
       
        while True:       
            CPF_inserido=input('Insira o CPF a ser validado: ')
            
            CPF_9digi=''
            CPF_10digi=''

            if len(CPF_inserido)!=11: 
                print('Você digitou um dígito a mais ou a menos!')
                continue
        #1º digito
            CPF_9digi=CPF_inserido[0:9]
            
            
        #2º dígito
            CPF_10digi=CPF_inserido[0:10]
            
            break

    else:
        print('Digite uma opção válida!')
        continue
    
    var_multiplica=10
    var_final=0
    for digito in CPF_9digi:
        var_somar=int(digito)*var_multiplica  
        var_final+=var_somar
        var_multiplica-=1


    var_finalx10=10*var_final

    if var_finalx10%11>9:
        var_resultado_digi1=0
    else:
        var_resultado_digi1=var_finalx10%11
            

    var_multiplica=11
    var_final=0
    if op=='2':
        CPF_10digi=CPF_9digi+str(var_resultado_digi1)

    for digito in CPF_10digi:
        var_somar=int(digito)*var_multiplica  
        var_final+=var_somar
        var_multiplica-=1


    var_finalx10=10*var_final

    if var_finalx10%11>9:
        var_resultado_digi2=0
    else:
        var_resultado_digi2=var_finalx10%11
        
        
   
        

    CPF_calculado=CPF_9digi+str(var_resultado_digi1)+str(var_resultado_digi2)

    if op=='2':
       print(f'O CPF gerado é: {CPF_calculado}')
    else: 
        if CPF_inserido==CPF_calculado:
            print(f'O CPF {CPF_inserido} é válido')
        else:
            print(f'O CPF {CPF_inserido} é invalido')  

    
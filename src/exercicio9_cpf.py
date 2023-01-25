import random

while True:
    print('Você deseja inserir [1] ou gerar um CPF [2]?')
    op=input('Insira o número correspondente: ')

    if op=='2':
        CPF_9digi=''
        CPF_10digi=''
        CPF_random=''
        for s in range(11):
            CPF_random+=str(random.randint(0,9))
            
            if s==9:
                CPF_9digi==CPF_random
            if s==10:
                 CPF_10digi==CPF_random
                
        CPF_inserido_sem_format=CPF_random
       


    elif op=='1':
       
        print('Insira o CPF, no seguinte formato: XXX.XXX.XXX-XX')
        CPF_inserido=input('Insira: ')
        while True:       
        #1º digito
            i=0
            CPF_9digi=''
            CPF_10digi=''

            if len(CPF_inserido)!=14: 
                print('Insira conforme o modelo!')
                break
    
            while i<len(CPF_inserido):
                if CPF_inserido[i]=='.':
                    CPF_9digi+=''
                elif CPF_inserido[i]=='-':
                    break
                else:
                    CPF_9digi+=CPF_inserido[i]
                i+=1
        #2º dígito
            i=0
            
            while i<len(CPF_inserido):
                if CPF_inserido[i]=='.':
                    CPF_10digi+=''
                elif CPF_inserido[i]=='-':
                    CPF_10digi+=CPF_inserido[i+1]
                    break
                else:
                    CPF_10digi+=CPF_inserido[i]
                i+=1
            
            i=0
            CPF_inserido_sem_format=''
            while i<len(CPF_inserido):
                if CPF_inserido[i]=='.' or CPF_inserido[i]=='-':
                    CPF_inserido_sem_format+=''
                else:
                    CPF_inserido_sem_format+=CPF_inserido[i]
                i+=1

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

    

    if CPF_inserido_sem_format==CPF_calculado:
        print(f'O CPF {CPF_calculado} é válido')
    else:
        print(f'O CPF {CPF_calculado} é invalido')
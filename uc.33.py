segundos=int(input("Digite um valor inteiro para realizar a conversão:  "))
horas = segundos // 3600
minutos = (segundos % 3600)//60
segundos= segundos % 60
print(str(horas)+":" + str(minutos)+":"+ str(segundos))

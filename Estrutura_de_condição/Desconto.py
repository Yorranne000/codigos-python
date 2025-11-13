#Cálculo_Desconto
Valor_total=float(input("Informe o valor total da Compra. " ))
Forma_de_pagamento=int(input("Informe a forma de pagamento, sendo 1 para a vista, 2 para cartão de crédito e 3 para parcelar  " ))
Desconto1=Valor_total -(Valor_total * 0.10)
Desconto2=Valor_total + (Valor_total * 0.05)

if Forma_de_pagamento == 1: 
   print("Valor a ser pago: ", Desconto1)
elif Forma_de_pagamento == 3:
   print("Valor a ser pago: ", Desconto2)
else:
   print("Valor total a ser pago ", Valor_total)
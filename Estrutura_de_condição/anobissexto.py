Ano=int(input("Informe o ano:(exemplo:2025) "))
if Ano%400 == 0 or Ano%4 == 0:
    if Ano%100 !=0:
     print("O ano é bissexto")
else:
    print("O ano não é bissexto")

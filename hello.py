
num = input("digite un numero de cinco digitos: ")
num = int(num)
rev,num_inver = 0,0

if num > 9999 and num < 99999:
    # 54345 palindromo
    digito1 = num % 10
    print('digito1 =',digito1)
    rev = int(num / 10)
    print('numero a revisar =',rev)
    num_inver = (num_inver * 10) + digito1
    print('numero invertido = ',num_inver)
    if rev != 0:
        print('*'*10)
        digito_2 = rev % 10
        print('digito2 = ',digito_2)
        rev = int(rev/10)
        print('numero a revisar =',rev)
        num_inver = (num_inver * 10) + digito_2
        print('numero invertido : ',num_inver)
        if rev !=0:
            print('*'*10)
            digito3 = rev % 10
            print('digito3 =',digito3)
            rev = int(rev/10)
            print('numero a revisar = ',rev)
            num_inver = (num_inver * 10) + digito3
            print('numero invertido = ',num_inver)
            if rev != 0:
                print('*'*10)
                digito4 = rev % 10
                print('digito4 = ',digito4)
                rev = int(rev/10)
                print('numero a revisar = ',rev)
                num_inver = (num_inver * 10) + digito4
                print('numero invertido = ',num_inver)
                if rev != 0:
                    print('*'*10)
                    digito5 = rev % 10
                    print('digito5 = ',digito5)
                    rev = int(rev / 10)
                    print('numero a revisar = ',rev)
                    num_inver = (num_inver * 10) + digito5
                    print('numero invertido = ',num_inver)
                    if rev != 0:
                        print('*'*10)
                        digito6 = rev % 10
                        print('digito6 = ',digito6)
                        rev = int (rev / 10)
                        print('numero a revisar = ',rev)
                        num_inver = (num_inver * 10) + digito6
                        print('numero invertido = ',num_inver)
                    else:
                        if num == num_inver:
                            print(' el numero es palindromo')
                        else:
                            print('el numero no es palindromo')
else:
    print(' el numero no es de cinco cifras')










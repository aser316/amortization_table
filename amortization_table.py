"""
NOTA:
este programa se usa relativedelta para el manejo de fechas y tabulate para imprimir los datos en forma de tabla, por favor instalar estos modulos antes de ejecutar el programa:
 pip install python-dateutil
 pip install tabulate
 """
import datetime
from dateutil.relativedelta import relativedelta
from tabulate import tabulate

def menu_loop():
    print("Welcomet to \"amortization table\" \n")
    #Solicitamos la fecha y validamos que sea una fecha valida con el formato solicitado
    while True:
        try:
            start_date = datetime.datetime.strptime(input("Enter date initial (YYYY-MM-DD)\n"), '%Y-%m-%d').date()
            #obtenemos la fecha actual
            now = datetime.datetime.now().date()
            #Validamos que la fecha no sea anterior a la fecha actual
            if str(now) <= str(start_date):
                break
            else:
                print("You CANNOT enter a date prior to the current date.")
        except ValueError:
            print("Invalid date, please enter the date in the following format YYYY-MM-DD")

    #Solicitamos el capital inicial, validamos que sea un numero y que sea mayor a 0
    while True:
        try:
            amount = float(input("\nEnter your initial capital:\n"))
            if amount > 0:
                break
            else:
                print("You can only enter values ​​greater than 0")
        except ValueError:
            print("You can only enter numbers ")

    #solicitamos el redito anual, validamos que sea un numero entero y que sea mayor a 0
    while True:
        try:
            anual_revenue = float(input("\nEnter the annual revenue\n"))
            if anual_revenue > 0:
                break
            else:
                print("You can only enter values ​​greater than 0")
        except ValueError:
            print("You can only enter numbers  ")

    print("The start date is: {}, the initial capital is: {}, the annual revenue is: {}%".format(start_date,amount,anual_revenue))

    #Mandamos los parametros solicitados a la funcion para realizar los calculos.
    amortization_table(start_date,amount,anual_revenue)


def amortization_table(start_date,amount,anual_revenue):
    #calculamos redito anual
    rate_percent = anual_revenue/100
    #Calculamos el ISR por año y por mes y lo truncamos a 2 digitos
    isr_year = round((amount*1.45)/100,2)
    isr_mont = round(isr_year / 12,2)

    #calculamos el redito
    revenues = (amount/anual_revenue)/12
    total_revenues= 0
    #calculamos redito acumulado
    real_revenues = revenues-isr_mont
    acumulated_revenues = real_revenues
    #agregamos un mes a la fecha inicio
    one_mont = start_date + relativedelta(months=1)

    #Declaramos una lista que contiene las cabeceras de nuestra tabla
    main_list = list()
    heads = ['','Cut off Date','Capital Initial','Rate','Revenues','ISR','Acumulated Renues']
    main_list.append(heads)
    cont = 0
    while True:
        lista = list()
        lista.append(str(one_mont))
        one_mont = one_mont + relativedelta(months=1)
        lista.append(amount)
        lista.append(rate_percent)
        lista.append(round(revenues,2))
        total_revenues = total_revenues + round(revenues,2)
        lista.append(isr_mont)
        lista.append(round(acumulated_revenues,2))
        acumulated_revenues = acumulated_revenues + real_revenues
        main_list.append(lista)
        if cont == 11:
            lista = list()
            lista.append('Total')
            lista.append('')
            lista.append('')
            lista.append(round(total_revenues,2))
            lista.append(isr_year)
            main_list.append(lista)
            break
        else:
            cont += 1

    print(tabulate(main_list,headers='firstrow',tablefmt='fancy_grid',stralign='center',showindex=True))

    option = input("Do you want to make another amortization table? y/n\n").lower()
    if option == "y":
        menu_loop()
    else:
        print("Thank you for using our amortization table")

if __name__ == '__main__':
    menu_loop()



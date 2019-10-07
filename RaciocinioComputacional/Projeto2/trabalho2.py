# coding: latin-1


class Trabalho2:

    def __init__(self):
            self.salaries = []

    def show_numeric_message(self):
        print('Favor entrar com val�res num�ricos.')

    def print_menu(self):
        print("""
                1 - Imprima uma mensagem para o usu�rio informando o
                    n�mero digitado.

                2 - Calcule a soma dos dois valores e imprima:

                3 - Calcule a m�dia de 4 notas e imprima:

                4 - Converter metros para cent�metros:

                5 - Entre a largura e a altura de uma parede em metro
                    s, calcule a sua �rea e a quantidade de tinta necess�
                    ria para pint�-la, sabendo que cada litro de tinta pi
                    nta uma �rea de 2 metros quadrados:

                6 - Calcular 5 de desconto de um pre�o de produto:

                7 - Ler o sal�rio de um funcion�rio e aumente 15%:

                8 - Sair.
            """)
        return input('Qual op��o voc� gostaria de executar?: ')

    def print_number(self):
        num = input('Entre o n�mero que deseja imprimir: ')
        print('O n�mero digitado foi: ', num)

    def sum(self):
        try:
            num1 = float(input('Entre com o primeiro valor: '))
            num2 = float(input('Entre com o segundo valor: '))
            print(round(num1 + num2, 2))
        except ValueError:
            self.show_numeric_message()

    def calc_mean(self):
            try:
                num1 = float(input('Entre com a primeira nota: '))
                num2 = float(input('Entre com a segunda nota: '))
                num3 = float(input('Entre com a terceira nota: '))
                num4 = float(input('Entre com a quarta nota: '))
                print('Sua m�dia foi de : ',
                      round((num1 + num2 + num3 + num4)/4, 2))
            except ValueError:
                self.show_numeric_message()

    def meters_to_centimeters(self):
            try:
                num1 = float(input('Quantos metros?: '))
                print(num1, ' metro(s) em centimetros s�o: ',
                      round((num1 * 100), 2))
            except ValueError:
                self.show_numeric_message()

    def calc_ink_liters(self):
        try:
            height = float(input('Entre com a altura da parede: '))
            widht = float(input('Entre com a largura da(s) parede(s)'))
            print('Quantidade de litros nescess�ria: ',
                  round((height * widht)/2, 2))
        except ValueError:
            self.show_numeric_message()

    def calc_discount(self):
        try:
            price = float(input('Entre com o pre�o do produto: '))
            print('O produto con 5% vai custar: ',
                  round((price * .95), 2))
        except ValueError:
            self.show_numeric_message()

    def read_salary(self):
        try:
            salary = float(input('Entre com o salario do funcion�rio para \
            aumento de 15%: '))
            print('O novo sal�rio do funcion�rio �: ',
                  round((salary * 1.15), 2))
        except ValueError:
            self.show_numeric_message()

    def show_menu(self):
        option = self.print_menu()
        while option != "8":
            if option == "1":
                self.print_number()
            elif option == "2":
                self.sum()
            elif option == "3":
                self.calc_mean()
            elif option == "4":
                self.meters_to_centimeters()
            elif option == "5":
                self.calc_ink_liters()
            elif option == "6":
                self.calc_discount()
            elif option == "7":
                self.read_salary()
            else:
                print('Op��o inv�lida, por favor escolha novamente:')
            option = self.print_menu()

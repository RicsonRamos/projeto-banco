from datetime import datetime
from random import randint
import pytz

class agencia:

    def _data_hora(self):
        """
        Returns the current date and time in the 'Brazil/East' timezone 
        formatted as 'dd/mm/yyyy hh:mm:ss'.
        """

        now = datetime.now(pytz.timezone('Brazil/East'))
        return now.strftime('%d/%m/%Y %H:%M:%S')
    def __init__(self, cnpj, telefone, agencia):
        
        
        """
        Inicializa a agência.

        :param cnpj: CNPJ da agência.
        :param telefone: Telefone da agência.
        :param agencia: Número da agência.
        """
        self._telefone = telefone
        self._agencia = agencia
        self._cnpj = cnpj
        self._caixa = 1000000
        self.emprestimos =  []
        self._clientes = []
        self._extrato = []


    def verificar_caixa(self):
        """
        Verifica o saldo da agência.

        :return: Saldo da agência.
        """
        if self._caixa < 1000000:
            print('Saldo em caixa insuficiente')
        else:
            print('Saldo em caixa dentro dos limites')
        return self._caixa
    
    def emprestimo(self, valor, cpf, juros):
        """
        Realiza um empréstimo na agência.

        :param valor: Valor do empréstimo.
        :return: None
        """
        if self._caixa > valor:
            self._caixa -= valor
            self.emprestimos.append((f'R$ {valor:,.2f}', self._data_hora(), cpf, juros))
        else:
            print('Saldo indisponível para empréstimo')

    def add_cliente(self, cpf, cliente, patrimonio):

        self._clientes.append((cpf, cliente, patrimonio))

    def mostrar_extrato(self):
        for extrato in self._extrato:
            print(extrato)

    def mostrar_clientes(self):
        for cliente in self._clientes:
            print(cliente)

# Agência Virtual
class AgenciaVirtual(agencia):

    def __init__(self, cnpj, telefone):
        """
        Inicializa a agência virtual.

        :param cnpj: CNPJ da agência virtual.
        :param telefone: Telefone da agência virtual.
        """
        super().__init__(cnpj, telefone, '0001')
        self._caixa = 1000000
        self._paypal = 0

    def exibir_caixa(self):
        print(f'Caixa: R$ {self._caixa:,.2f}')
        print(f'Saldo do PayPal: R$ {self._paypal:,.2f}')

    def deposito_paypal(self, valor):
        if self._caixa < valor:
            print('Saldo insuficiente')
        else:
            print('Deposito realizada com sucesso')
            self._caixa -= valor
            self._paypal += valor
            self._extrato.append((f'Deposito', self._data_hora(), valor))

    def saque_paypal(self, valor):
        if self._paypal < valor:
            print('Saldo insuficiente')
        else:
            print('Saque realizada com sucesso')
            self._caixa += valor
            self._paypal -= valor
            self._extrato.append((f'Saque', self._data_hora(), valor))

    def transferir_paypal(self, valor, conta_destino):
        if self._paypal < valor:
            print('Saldo insuficiente')
        else:
            print('Transferência realizada com sucesso')
            self._caixa += valor
            self._paypal -= valor
            conta_destino._caixa += valor
            self._extrato.append((f'Transferencia', self._data_hora(), valor))

# Agência Física
class AgenciaFisica(agencia):

    def __init__(self, cnpj, telefone):
        """
        Inicializa a agência física.

        :param cnpj: CNPJ da agência física.
        :param telefone: Telefone da agência física.
        :param agencia: Número da agência física.
        """
        super().__init__(cnpj, telefone, agencia=randint(1000, 9999))
        self._caixa = 1000000

# Agência Private
class AgenciaPrivate(agencia):

    def __init__(self, cnpj, telefone):
        """
        Inicializa a agência private.

        :param cnpj: CNPJ da agência private.
        :param telefone: Telefone da agência private.
        :param agencia: Número da agência private.
        """
        super().__init__(cnpj, telefone, agencia=randint(1000, 9999))
        self._caixa = 1000000000

    def add_cliente(self, cpf, cliente, patrimonio):
        if patrimonio >= 1000000:
           super().add_cliente(cpf, cliente, patrimonio)
           print('Cadastro realizado com sucesso')
           self._clientes.append((cpf, cliente, patrimonio))

        else:
            print('Pratrimônio infsuficiente para cadastro')

agencia_private = AgenciaPrivate('12345678901234', '123456789')

agencia_private.add_cliente('123.123.123-12', 'Matheus', 10000000)
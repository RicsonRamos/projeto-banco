from datetime import datetime
from random import randint
import re
import pytz


class ContaCorrente():

    def _data_hora(self):
        """
        Returns the current date and time in the 'Brazil/East' timezone 
        formatted as 'dd/mm/yyyy hh:mm:ss'.
        """

        now = datetime.now(pytz.timezone('Brazil/East'))
        return now.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, saldo, conta, agencia):
        
        """
        Inicializa a conta corrente.

        :param nome: Nome do titular da conta.
        :param cpf: CPF do titular da conta.
        :param saldo: Saldo inicial da conta.
        :param conta: N mero da conta.
        :param agencia: N mero da ag ncia.
        """
        self._conta = conta
        self._agencia = agencia
        self._nome = nome
        self._cpf = cpf
        self._saldo = saldo
        self._senha = None
        self._cheque_especial = None 
        self._extrato = []
        self.cartoes = []   

    def mostrar_saldo(self):
        """
        Mostra o saldo atual da conta.

        :return: None
        """
        print(f'Seu saldo é: R$ {self._saldo:,.2f}')
        

    def depositar(self, valor):
        """
        Realiza um depósito na conta corrente.

        :param valor: Valor a ser depositado.
        :return: None
        """
        self._saldo += valor
        print('Deposito realizado com sucesso')
        self._extrato.append((f'R$ {valor:,.2f}', self._data_hora(), f'Saldo após transação: R$ {self._saldo:,.2f}'))

    def sacar(self, valor):
        """
        Realiza um saque na conta corrente.

        :param valor: Valor a ser sacado.
        :return: None
        """
        if self.verificar_limite(valor):
            self._saldo -= valor        
            self._extrato.append((f'R$ {-valor:,.2f}', self._data_hora(), f'Saldo após transação: R$ {self._saldo:,.2f}'))

    def get_cheque_especial(self):
        """
        Retorna o valor do cheque especial.

        :return: Valor do cheque especial.
        """
        self._cheque_especial = -1000
        return self._cheque_especial

    def transferir(self, valor, conta_destino):
        """
        Transfere um valor entre contas correntes.

        :param valor: Valor a ser transferido.
        :param conta_destino: Conta corrente destino.
        :return: None
        """
        if self.verificar_limite(valor):
            self._saldo -= valor
            conta_destino._saldo += valor
            self._extrato.append((f'R$ {-valor:,.2f}', self._data_hora(), f'Saldo após transação: R$ {self._saldo:,.2f}'))

    def mostrar_extrato(self):
        """
        Mostra o extrato da conta corrente.

        :return: None
        """
        
        print(f'Cc: {self._conta}, Ag: {self._agencia}, Nome: {self._nome}')
        for extrato in self._extrato:
            print(extrato)

    def verificar_limite(self, valor):
        """
        Verifica se o valor passado como parâmetro não ultrapassa o saldo da conta e o cheque especial.

        :param valor: Valor a ser verificado.
        :return: True se o valor for válido, False caso contrário.
        """
        if self._saldo - valor < self.get_cheque_especial():
            print('Saldo insuficiente')
            return False
        else:
            print('Operação realizada com sucesso')
            return True


class CartaoCredito(ContaCorrente):


    def _data_hora(self):
        """
        Retorna a data e hora atual no Brasil.

        :return: Uma datetime atual no Brasil.
        """
        now = datetime.now(pytz.timezone('Brazil/East'))
        return now

    def __init__(self, titular, contacorrente, bandeira, limite):
        """
        Inicializa o cartão de crédito.

        :param titular: Titular do cartão.
        :param contacorrente: Objeto da conta corrente associada.
        :param bandeira: Bandeira do cartão de crédito.
        :param limite: Limite de crédito do cartão.
        """

        self._titular = titular
        self._contacorrente = contacorrente
        self._bandeira = bandeira
        self._numero = f'5543-4330-{randint(1000, 9999)}-{randint(1000, 9999)}'
        self._limite = limite
        self._validade = f'{self._data_hora().month}/{self._data_hora().year + 5}'
        self._ccv = f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}'
        contacorrente.cartoes.append(self)

    @property
    def senha(self):
        """
        Retorna a senha do cart o, somente n meros.

        :return: Senha do cart o.
        """
        return self._senha

    @senha.setter
    def senha(self, senha):
        """
        Define a senha do cart o.

        :param senha: Senha do cart o, 4 n meros.
        :raises ValueError: Se a senha tiver outro tamanho ou n o for n mero.
        """
        if re.fullmatch(r'\d{4}', senha):  # Confere se a senha tem 4 números
                self._senha = senha
                print('Senha cadastrada com sucesso')
        else:
            
            print('Senha inválida')

    

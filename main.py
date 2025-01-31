from bank import CartaoCredito, ContaCorrente
from agencia import agencia, AgenciaFisica, AgenciaPrivate, AgenciaVirtual


conta1 = ContaCorrente('João', '123.123.123-12', 1000, 1, 1)
conta2 = ContaCorrente('Maria', '321.321.321-32', 2000, 2, 2)
conta3 = ContaCorrente('Pedro', '456.456.456-45', 3000, 3, 3)

agencia_fisica = AgenciaFisica('123.123.123-12', '123456789')
agencia_private = AgenciaPrivate('123.123.123-12', '123456789')  
agencia_virtual = AgenciaVirtual('123.123.123-12', '123456789')

agencia_private.add_cliente('123.123.123-12', 'Matheus', 10000000)
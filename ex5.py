class Empregado:
    def pagar_salario(self):
       pass

class EmpregadoHora(Empregado):
    def __init__(self, horas_trabalhadas, taxa_por_hora):
        self.horas_trabalhadas = horas_trabalhadas
        self.taxa_por_hora = taxa_por_hora

    def pagar_salario(self):
        return self.horas_trabalhadas * self.taxa_por_hora

class EmpregadoMes(Empregado):
    def __init__(self, salario_mensal):
        self.salario_mensal = salario_mensal

    def pagar_salario(self):
        return self.salario_mensal

funcionarios = [EmpregadoHora(1620, 25), EmpregadoMes(303200)]

for funcionario in funcionarios:
    print(funcionario.pagar_salario())

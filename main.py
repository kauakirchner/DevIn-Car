from random import randint  
class Veiculo:
    def __init__(self, data_fabricacao, nome_veiculo, placa_veiculo, valor_veiculo, cpf_comprador, cor_veiculo):
        self.num_chassi = randint(0, 10000000000000)
        self.data_fabricacao = data_fabricacao
        self.nome_veiculo = nome_veiculo
        self.placa_veiculo = placa_veiculo
        self.valor_veiculo = valor_veiculo
        self.cpf_comprador = cpf_comprador
        self.cor_veiculo = cor_veiculo
        self.em_estoque = True
        self.dados_transacao = []

    def vender_veiculo(self):
        print(f'O Veículo Do modelo: \n ------ {self.nome_veiculo} ------ \n Cor: \n ------ {self.cor_veiculo} ------ \n Placa: \n ------ {self.placa_veiculo} ------ \n Foi vendido.')
        self.em_estoque = False
        
    def listar_informacoes(self):
        print(f'Nome: \n ------ {self.nome_veiculo} ------ \n Cor: \n ------ {self.cor_veiculo} ------ \n Número de chassi: \n ------ {self.num_chassi} ------ \n Placa: \n ------ {self.placa_veiculo} ------ \n Data de fabricação: \n ------ {self.data_fabricacao} ------ \n CPF do comprador: \n ------ {self.cpf_comprador} ------ \n Valor: \n ------ {self.valor_veiculo} ------ \n Em estoque: \n ------ {self.em_estoque} ------')
        return True

    def alterar_informações(self):
        print('Lembrando que você só pode alterar a cor e o valor do veículo! \n ')
        nova_cor = str(input(f'Qual será a nova cor do seu {self.nome_veiculo}: \n '))
        novo_valor = float(input(f'Qual será o novo valor do seu {self.nome_veiculo}: '))
        self.cor_veiculo = nova_cor
        self.valor_veiculo = novo_valor
        print(f'A nova cor do seu veículo é: \n ------ {self.cor_veiculo} ------ \n Com o valor atualizado de: \n ------ {self.valor_veiculo}R$ ------')

    def salva_dados_transacao(self, data_compra, cpf_comprador, valor, num_chassi, placa_veiculo):
        self.dados_transacao.append(Transacoes(data_compra=data_compra, cpf_comprador=cpf_comprador, valor=valor, num_chassi=num_chassi, placa_veiculo=placa_veiculo))

    def lista_dados_transacao(self):
        for i in self.dados_transacao:
            print(f'Número Chassi: \n ------ {i.num_chassi} ------ \n Placa: \n ------- {i.placa_veiculo} ------ \n Data da venda: \n ------ {i.data_compra} ------ \n Valor: \n ------ {i.valor} ------ \n CPF comprador: \n ------ {i.cpf_comprador} ------')

    def salva_data_base(self, veiculo):
        DATA_BASE.append(veiculo)

    def relatorio_veiculo_maior_valor(self):
        info_veiculo = None
        maior_valor = 0
        for veiculo in DATA_BASE:
            if veiculo.valor_veiculo > maior_valor:
                info_veiculo = veiculo
                maior_valor = veiculo.valor_veiculo
        print(f'O Veículo com maior valor é: \n ------ {info_veiculo.nome_veiculo} ------ \n E seu preço é: \n ------ {maior_valor}R$ ------')

    def relatorio_veiculo_menor_valor(self):
        info_veiculo = None
        menor_valor = 99999999999
        for veiculo in DATA_BASE:
            if veiculo.valor_veiculo < menor_valor:
                info_veiculo = veiculo
                menor_valor = veiculo.valor_veiculo
        print(f'O Veículo com menor valor é: \n ------ {info_veiculo.nome_veiculo} ------ \n E seu preço é: \n ------ {menor_valor}R$ ------')

    def relatorio_por_tipo_veiculo(self):
        categoria_veiculo = int(input('Qual categoria de Veículo você deseja listar? \n Carros[1] \n Motos/Triciculos[2] \n Camionetes[3] \n Todos[4]'))
        if categoria_veiculo == 1:
            print('------ Temos apenas 1 carro no estoque no momento ------')
            print(f'Data de fabricação: \n ------ {v1.data_fabricacao} ------ \n Modelo: \n ------ {v1.nome_veiculo} \n Placa: ------ {v1.placa_veiculo} ------ \n Potência: \n ------ {v1.potencia_motor} ------ \n Tipo de combustível: \n ------ {v1.tipo_combustivel} ------ \n Total de portas: \n ------ {v1.qtd_portas} ------')

        if categoria_veiculo == 2:
            print('------ Temos apenas 2 motos no estoque no momento ------')
            print(f'Data de fabricação: \n ------ {v2.data_fabricacao} ------ \n Modelo: \n ------ {v2.nome_veiculo} \n Placa: ------ {v2.placa_veiculo} ------ \n Potência: \n ------ {v2.potencia_motor} ------ \n Quantidade de Rodas: \n ------ {v2.qtd_rodas} ------')

            print(f'Data de fabricação: \n ------ {v3.data_fabricacao} ------ \n Modelo: \n ------ {v3.nome_veiculo} \n Placa: ------ {v3.placa_veiculo} ------ \n Potência: \n ------ {v3.potencia_motor} ------ \n Quantidade de rodas: \n ------ {v3.qtd_rodas} ------')

        if categoria_veiculo == 3:
            print('------ Temos apenas 1 camionete no estoque no momento ------')
            print(f'Data de fabricação: \n ------ {v4.data_fabricacao} ------ \n Modelo: \n ------ {v4.nome_veiculo} \n Placa: ------ {v4.placa_veiculo} ------ \n Quantidade de portas: \n ------ {v4.qtd_portas} ------ \n Tipo de combustível: \n ------ {v4.tipo_combustivel} ------ \n Potência: \n ------ {v4.potencia_motor} ------ \n Capacidade de carregamento: \n ------ {v4.capacidade_carregamento} ------')

    


DATA_BASE = []
class Transacoes:
    def __init__(self, data_compra, cpf_comprador, valor, num_chassi, placa_veiculo):
        self.data_compra = data_compra
        self.cpf_comprador = cpf_comprador
        self.valor = valor
        self.num_chassi = num_chassi
        self.placa_veiculo = placa_veiculo

class Moto_Triciculo(Veiculo):
    def __init__(self, data_fabricacao, nome_veiculo, placa_veiculo, valor_veiculo, cpf_comprador, cor_veiculo, potencia_motor, qtd_rodas):
        self.potencia_motor = potencia_motor
        self.qtd_rodas = qtd_rodas
        super().__init__(data_fabricacao, nome_veiculo, placa_veiculo, valor_veiculo, cpf_comprador, cor_veiculo)

class Carro(Veiculo):
    def __init__(self, data_fabricacao, nome_veiculo, placa_veiculo, valor_veiculo, cpf_comprador, cor_veiculo, qtd_portas, tipo_combustivel, potencia_motor):
        self.qtd_portas = qtd_portas
        self.tipo_combustivel = tipo_combustivel
        self.potencia_motor = potencia_motor
        super().__init__(data_fabricacao, nome_veiculo, placa_veiculo, valor_veiculo, cpf_comprador, cor_veiculo)

class Camionete(Veiculo):
    def __init__(self,data_fabricacao, nome_veiculo, placa_veiculo, valor_veiculo, cpf_comprador, qtd_portas, tipo_combustivel, capacidade_carregamento, potencia_motor, cor_veiculo="roxo"):
        self.qtd_portas = qtd_portas
        self.tipo_combustivel = tipo_combustivel
        self.capacidade_carregamento = capacidade_carregamento
        self.potencia_motor = potencia_motor
        super().__init__(data_fabricacao, nome_veiculo, placa_veiculo, valor_veiculo, cpf_comprador, cor_veiculo)

v1 = Carro('10/10/21', 'Montana', 102034, '1R$', 107727, 'Roxo', 4, 'Flex', '420cv')
v2 = Moto_Triciculo('10/10/21',  'S1000rr', 102034, '5000000R$', 107727, 'Rosa', '200cv', 2)
v3 = Moto_Triciculo('10/10/21',  'Gs1250r', 102034, '1000R$', 107727, 'branco', '500cv', 4)
v4 = Camionete('10/10/21', 'Gol', 102034, '1000R$', 107727, 4, 'Diesel', '400l', '280cv')

v1.salva_data_base(v1)
v2.salva_data_base(v2)
v3.salva_data_base(v3)
v4.salva_data_base(v4)
v1.relatorio_por_tipo_veiculo()

while True:
    decida_a_acao = int(input('Qual ação você deseja realizar? \n Vender um veículo[1] \n Listar informações de um veículo[2] \n Alterar informações[3] \n Listar Dados das transacoes[4] \n Sair[5]  \n '))
    if decida_a_acao == 1:
        veiculo_desejado = int(input("Qual veículo deseja vender? V1[1] \n V2[2] \n V3[3] \n V4[4] \n "))
        if veiculo_desejado == 1:
            v1.vender_veiculo()

        if veiculo_desejado == 2:
            v2.vender_veiculo()
        
        if veiculo_desejado == 3:
            v3.vender_veiculo()

        if veiculo_desejado == 4:
            v4.vender_veiculo()


    if decida_a_acao == 2:
        veiculo_desejado = int(input("Qual veículo deseja listar as informações? \n V1[1] \n V2[2] \n V3[3] \n V4[4] \n "))
        if veiculo_desejado == 1:
            v1.listar_informacoes()

        if veiculo_desejado == 2:
            v2.listar_informacoes()
        
        if veiculo_desejado == 3:
            v3.listar_informacoes()

        if veiculo_desejado == 4:
            v4.listar_informacoes()

    if decida_a_acao == 3:
        veiculo_desejado = int(input("Qual veículo deseja alterar as informações? \n V1[1] \n V2[2] \n V3[3] \n V4[4] \n "))
        if veiculo_desejado == 1:
            v1.alterar_informações()

        if veiculo_desejado == 2:
            v2.alterar_informações()
        
        if veiculo_desejado == 3:
            v3.alterar_informações()

        if veiculo_desejado == 4:
            v4.alterar_informações()

    if decida_a_acao == 4:
        veiculo_desejado = int(input("Qual veículo deseja listar os dados de transações? \n V1[1] \n V2[2] \n V3[3] \n V4[4] \n "))
        if veiculo_desejado == 1:
            v1.vender_veiculo()
            v1.salva_dados_transacao(data_compra= '12/12/2021', cpf_comprador=v1.cpf_comprador, valor=v1.valor_veiculo, num_chassi=v1.num_chassi, placa_veiculo=v1.placa_veiculo)
            v1.lista_dados_transacao()

        if veiculo_desejado == 2:
            v2.vender_veiculo()
            v2.salva_dados_transacao(data_compra= '13/12/2021', cpf_comprador=v2.cpf_comprador, valor=v2.valor_veiculo, num_chassi=v2.num_chassi, placa_veiculo=v2.placa_veiculo )
            v2.lista_dados_transacao()
        
        if veiculo_desejado == 3:
            v3.vender_veiculo()
            v3.salva_dados_transacao(data_compra= '14/12/2021', cpf_comprador=v3.cpf_comprador, valor=v3.valor_veiculo, num_chassi=v3.num_chassi, placa_veiculo=v3.placa_veiculo )
            v3.lista_dados_transacao()

        if veiculo_desejado == 4:
            v4.vender_veiculo()
            v4.salva_dados_transacao(data_compra= '15/12/2021', cpf_comprador=v4.cpf_comprador, valor=v4.valor_veiculo, num_chassi=v4.num_chassi, placa_veiculo=v4.placa_veiculo )
            v4.lista_dados_transacao()

    if decida_a_acao == 5:
        print('Até mais!!')
        break


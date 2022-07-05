class Veiculo:
    def __init__(self, num_chassi, data_fabricacao, nome_veiculo, placa_veiculo, valor_veiculo, cpf_comprador, cor_veiculo):
        self.num_chassi = num_chassi
        self.data_fabricacao = data_fabricacao
        self.nome_veiculo = nome_veiculo
        self.placa_veiculo = placa_veiculo
        self.valor_veiculo = valor_veiculo
        self.cpf_comprador = cpf_comprador
        self.cor_veiculo = cor_veiculo
        self.em_estoque = True

    def vender_veiculo(self):
        print(f'O {self.nome_veiculo} {self.cor_veiculo} de placa {self.placa_veiculo} foi vendido. \n cpf do comprador: {self.cpf_comprador}')
        self.em_estoque = False
        
    def listar_informacoes(self):
        print(f'{self.nome_veiculo} \n {self.cor_veiculo} \n número de chassi: {self.num_chassi} \n placa: {self.placa_veiculo} /n data de fabricação: {self.data_fabricacao} \n cpf do comprador: {self.cpf_comprador} \n valor: {self.valor_veiculo} \n em estoque: {self.em_estoque}')
        return True

    def alterar_informações(self):
        print('Lembrando que você só pode alterar a cor e o valor do veículo! ')
        nova_cor = str(input(f'Qual será a nova cor do seu {self.nome_veiculo}: '))
        novo_valor = float(input(f'Qual será o novo valor do seu {self.nome_veiculo}: '))
        self.cor_veiculo = nova_cor
        self.valor_veiculo = novo_valor
        print(f'A nova cor do seu veículo é: {self.cor_veiculo} com o valor atualizado de: {self.valor_veiculo}R$')

class Moto_Triciculo(Veiculo):
    def __init__(self, num_chassi, data_fabricacao, nome_veiculo, placa_veiculo, valor_veiculo, cpf_comprador, cor_veiculo, potencia_motor, qtd_rodas):
        self.potencia_motor = potencia_motor
        self.qtd_rodas = qtd_rodas
        super().__init__(num_chassi, data_fabricacao, nome_veiculo, placa_veiculo, valor_veiculo, cpf_comprador, cor_veiculo)

class Carro(Veiculo):
    def __init__(self, num_chassi, data_fabricacao, nome_veiculo, placa_veiculo, valor_veiculo, cpf_comprador, cor_veiculo, qtd_portas, tipo_combustivel, potencia_motor):
        self.qtd_portas = qtd_portas
        self.tipo_combustivel = tipo_combustivel
        self.potencia_motor = potencia_motor
        super().__init__(num_chassi, data_fabricacao, nome_veiculo, placa_veiculo, valor_veiculo, cpf_comprador, cor_veiculo)
        
    

v1 = Carro(1010, 2008, 'Montana', 102034, 1000, 107727, 'Roxo', 4, 'Flex', '420cv')
v2 = Moto_Triciculo(1010, 2008, 'S1000rr', 102034, 1000, 107727, 'Rosa', '200cv', 2)
v3 = Moto_Triciculo(1010, 2008, 'Gs1250r', 102034, 1000, 107727, 'branco', '500cv', 4)
v4 = Veiculo(1010, 2008, 'Gool', 102034, 1000, 107727, 'Azul')
v5 = Veiculo(1010, 2008, 'Azera', 102034, 1000, 107727, 'Verde')
while True:
    decida_a_acao = int(input('Qual ação você deseja realizar? Vender um veículo[1] \n Listar informações de um veículo[2] \n Alterar informações[3] \n Sair[4] \n '))
    if decida_a_acao == 1:
        veiculo_desejado = int(input("Qual veículo deseja vender? V1[1] \n V2[2] \n V3[3] \n V4[4] \n V5[5] \n "))
        if veiculo_desejado == 1:
            v1.vender_veiculo()

        if veiculo_desejado == 2:
            v2.vender_veiculo()
        
        if veiculo_desejado == 3:
            v3.vender_veiculo()

        if veiculo_desejado == 4:
            v4.vender_veiculo()

        if veiculo_desejado == 5:
            v5.vender_veiculo()

    if decida_a_acao == 2:
        veiculo_desejado = int(input("Qual veículo deseja listar as informações? V1[1] \n V2[2] \n V3[3] \n V4[4] \n V5[5] \n "))
        if veiculo_desejado == 1:
            v1.listar_informacoes()

        if veiculo_desejado == 2:
            v2.listar_informacoes()
        
        if veiculo_desejado == 3:
            v3.listar_informacoes()

        if veiculo_desejado == 4:
            v4.listar_informacoes()

        if veiculo_desejado == 5:
            v5.listar_informacoes()

    if decida_a_acao == 3:
        veiculo_desejado = int(input("Qual veículo deseja listar as informações? V1[1] \n V2[2] \n V3[3] \n V4[4] \n V5[5] \n "))
        if veiculo_desejado == 1:
            v1.alterar_informações()

        if veiculo_desejado == 2:
            v2.alterar_informações()
        
        if veiculo_desejado == 3:
            v3.alterar_informações()

        if veiculo_desejado == 4:
            v4.alterar_informações()

        if veiculo_desejado == 5:
            v5.alterar_informações()
    
    if decida_a_acao == 4:
        print('Até mais!!')
        break


import pickle


estoque = {}
categorias = set()
vendas = []

def menu_inicial(): # menu inicial, onde vai pedir para o colaborador entrar com o que deseja entre 1 a 7
    print('\n*** Sistema de Gereciamento de Vendas ***\n')
    print('1. Cadastrar novo produto')
    print('2. Registrar venda')
    print('3. Consultar produtos em estoque')
    print('4. Relatório de produtos com estoque baixo')
    print('5. Valor total do estoque')
    print('6. Análise de vendas por categoria')
    print('7. Busca de produtos por nome')
    print('8. Excluir a ultima compra.')
    print('9. Sair\n')
    return input("Escolha uma opção: ")
# menu_inicial() vou manter todos os testes comentados.


def login():
    usuarios = {'ADMIN': '123456', 'GILBERTO': '140187', 'EMANUEL': '456789'}
    print('\n*** Login ***\n')
    for _ in range(5):
        usuario = input('Usuário: ').upper().strip()
        senha = input('Senha: ')
        if usuarios.get(usuario) == senha:
            print('\nLogin efetuado com sucesso')
            return True
        else:
            print('\nlogin ou senha incorreto.\n')
    print('\nnúmero de tentativas exedido.')
    return False
# login()


def cadastro_item(estoque, categorias): # cadastro de items no estoque por categoria.
    print('\n*** Cadastro de produtos ***\n')
    while True:
            try: # 1 
                codigo = int(input('Entre com o codigo: '))
                break
            except ValueError:
                print('Dado incorreto! Por favor, insira um número inteiro para o código.')
    nome = input('Entre com o nome do produto: ').upper()
    categoria = input('Entre com a categoria: ').upper()
    while True:
        try: # 1
            quantidade = int(input('Quantidade do item: '))
            break
        except ValueError:
            print('Dado incorreto! Por favor, insira um número inteiro para o código.')
    while True:
        try: # 1
            valor = float(input('Entre com o valor R$ '))
            break
        except ValueError:
            print('Dado incorreto! Por favor, insira um número inteiro ou flutuante.')
    estoque[codigo] = {'nome':nome, 'categoria':categoria, 'quantidade':quantidade, 'valor':valor}
    categorias.add(categoria)
    print(f'\nproduto "{nome}" foi cadastrado com sucesso!')
'''
# 1 estou usando ele para validar a entrada, assim caso o usuario entre com string não pare, 
usei desta forma também para o colaborador / usuario indentificar qual o campo esta errando. Não
vi a nescessidade de por nas strings, ja que existe variadades de produtos com numeros e ate caracteres 
especiais.
'''
# cadastro_item(estoque, categorias)


def registrar_venda(estoque, vendas):
    print('\n*** Registro de Vendas ***')
    while True:
        try:
            codigo = int(input('Entre com o codigo: '))
            break
        except ValueError:
            print('Dado incorreto! Por favor, insira um número inteiro para o código.')
    if codigo in estoque:
        while True:
            try:
                venda = int(input('Entre com a quantidade de itens vendidos: '))
                break
            except ValueError:
                print('Dado incorreto! Por favor, insira um número inteiro.')
        if estoque[codigo]['quantidade'] >= venda:
            estoque[codigo]['quantidade'] -= venda # estoque[codigo]['quantidade'] = estoque[codigo]['quantidade'] - venda
            vendas.append({'codigo':codigo, 'quantidade':venda, 'categoria':estoque[codigo]['categoria']})
            print('Venda efetuada!')
        else:
            print('Não foi possivel vender o produto, estoque em baixa.')
    else:
        print('Produto não localizado.')
# registrar_venda(estoque, vendas)


def cancelar_venda(estoque, vendas):
    if vendas:
        venda = vendas.pop()
        codigo = venda['codigo']
        quantidade = venda['quantidade']
        estoque[codigo]['quantidade'] += quantidade
        print(f'Venda cancelada: {quantidade} unidades do produto {estoque[codigo]["nome"]}, voltaram ao estoque.')
    else:
        print('Não a venda para ser desfeita.')
# cancelar_venda(estoque, vendas)


def consulta_item(estoque):
    print('\n*** Produtos do estoque ***\n')
    for codigo, info in estoque.items():
        print(f'Código: {codigo}\nNome: {info["nome"]}\nQuantidade: {info["quantidade"]}\n')
# consulta_item(estoque)           
    

def relatorio_de_items_em_Baixa(estoque):
    print('\n*** Produtos do estoque em baixa ***\n')
    for codigo, info, in estoque.items():
        if int(info['quantidade']) < 5:
          print(f'Código: {codigo}\nNome: {info["nome"]}\nQuantidade: {info["quantidade"]}')
# relatorio_de_items_em_Baixa(estoque)    


def valor_total_estoque(estoque):
    valor_total_estoque = sum(float(info['valor']) * int(info['quantidade']) for info in estoque.values())
    print(f'\n Valor total do estoque é de: R$ {valor_total_estoque:.2f}')
# valor_total_estoque(estoque)


def analise_de_vendas(vendas):
    print('\n*** Vendas por categoria ***')
    venda_categoria = {}
    for venda in vendas:
        categoria = venda['categoria']
        venda_categoria['categoria'] = venda_categoria.get(categoria, 0) + venda['quantidade']
    for categoria, quantidade in venda_categoria.items():
        print(f'Categoria: {categoria}, total vendidos {quantidade}')
# analise_de_vendas(vendas)


def salvar_dados(estoque, vendas, categorias):
    with open('banco.plk','wb') as file:
        pickle.dump({'estoque':estoque, 'vendas':vendas, 'categorias':categorias}, file)


def carregar_dados():
    try:
        with open('banco.plk', 'rb') as file:
            banco = pickle.load(file)
            return banco['estoque'], banco['vendas'], banco['categorias']
    except FileNotFoundError:
        return{}, [], set()
    except Exception as e:
        print(f'Erro ao carregar os dados: {e}')
        return {}, [], set()
# carregar_dados()


def localizar_produto(estoque):
    print('\n*** Buscar produto ***\n')
    buscar = input('Entre com o nome ou categoria do produto: ').upper()
    localizar = [info for info in estoque.values() if buscar in info['nome'] or buscar in info['categoria']]
    if localizar:
        for produto in localizar:
            print(f'\nNome: {produto["nome"]} \nCategoria: {produto["categoria"]} \nQuantidade: {produto["quantidade"]} \nValor R$ {produto["valor"]:.2f}')
    else:
        print('\nProduto não localizado')
# localizar_produto(estoque)


def main():
    global estoque, vendas, categorias
    estoque, vendas, categorias = carregar_dados()

    if not login():
        return
    
    while True:
        try:
            opcao = int(menu_inicial())   
            if opcao == 1:
                cadastro_item(estoque, categorias) 
            elif opcao == 2:
                registrar_venda(estoque, vendas) 
            elif opcao == 3:
                consulta_item(estoque)
            elif opcao == 4:
                relatorio_de_items_em_Baixa(estoque)
            elif opcao == 5:
                valor_total_estoque(estoque)
            elif opcao == 6:
                analise_de_vendas(vendas)
            elif opcao == 7:
                localizar_produto(estoque)
            elif opcao == 8:
                cancelar_venda(estoque, vendas)
            elif opcao == 9:
                salvar_dados(estoque, vendas, categorias)
                break
        except ValueError:
            print('\nDado incorreto')
if __name__ == "__main__":
    main()
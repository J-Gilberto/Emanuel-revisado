def login():
  criei um validador de usuario que vai ter 5 tratativas, pedindo usuario e senha, coloquei no imput 'upper() e strip() para não gerar erro com palavras em casp ou mesmo espaços.
  de inicio tinha so criado o admin, mas também criei 2 novos usuarios, coloquei eles em maiusculo, para facilitar. usuarios = {'ADMIN': '123456', 'GILBERTO': '140187', 'EMANUEL': '456789'}

def menu_inicial():
  nada de especial no menu que o colaborador vai acessar, mas ele tem 9 escolhas e a 9° vai sair do programa e salvar todas as entradas e saidas no banco.plk 
  (tive uma dificuldade imensa a respeoito de como salvar em um banco persistente, tive que pesquisar no stackoverflow e outros foruns, tenho muito o que estudar)

def cadastro_item(estoque, categorias):
  criei o cadastro de itens com o validador ('try' e o 'except ValueError') para numeros inteiros e flutuantes, as strings não vi a necessidade de fazer isso, 
  pode haver cadastro errado por conta do colaborador, isso na entrada do 'nome' e 'categoria' do produto, mas codigo, quantidade e valor, se entrar com 
  caracteres sem ser inteiro ou flutuante, vai chamar o erro "Dado incorreto! Por favor, insira um número inteiro ou flutuante."

def registrar_venda(estoque, vendas):
  no registro de vendas, tambem usei o try e o except ValueError caso o colaborador entrar com dado errado, aqui vai registrar toda a venda e a baixa no estoque após ela


  
  

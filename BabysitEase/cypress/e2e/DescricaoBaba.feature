#utf-8
#language: pt

Funcionalidade: Visualizar Descrição da Baba
  Cenário: Acessar Descrição Baba com sucesso
    Dado que estou na página inicial
    E existam babas disponíveis
    Quando eu acessar "Read More" da baba
    Então devo conseguir visualizar as mesmas informações da baba selecionada

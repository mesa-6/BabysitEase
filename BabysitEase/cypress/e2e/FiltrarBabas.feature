#utf-8
#language: pt

Funcionalidade: Filtrar babás por preço
  Cenário: Filtrar lista de babás pelo preço com sucesso
    Dado que estou na página inicial
    E a barra lateral está aberta
    Quando seleciono e confirmo um filtro de preço
    Então devo conseguir visualizar apenas as babás que se enquadram nessa faixa de preço

  Cenário: Filtrar busca e não conter babás disponíveis
    Dado que estou na página inicial
    E a barra lateral está aberta
    Quando seleciono um filtro que não contém babas disponíveis
    Então devo conseguir visualizar apenas a mensagem: "Não há babás disponíveis"
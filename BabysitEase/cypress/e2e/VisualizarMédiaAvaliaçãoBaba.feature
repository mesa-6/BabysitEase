#utf-8
#language: pt

Funcionalidade: Visualizar a média da babá

  Cenário: Visualizar resposta padrão para babás sem avaliação prévia
    Dado que estou na home
    E existam babas disponíveis
    Quando eu acessar "Read More" da baba
    E a babá ainda não foi avaliada
    Então devo visualizar uma mensagem “Ops! Nenhuma avaliação disponível.”

  Cenário: Visualizar nota média de avaliação de uma babá já avaliada com sucesso
    Dado que estou na home
    E existam babas disponíveis
    Quando eu acessar "Read More" da baba que já foi avaliada
    Então devo visualizar uma média das avaliações da babá
  
#utf-8
#language: pt

Funcionalidade: Visualizar Feedbacks da baba
  Cenário: Visualizar mensagem quando não há feedbacks disponíveis da babá
    Dado que estou na página inicial
    E existam babas disponíveis
    Quando eu acessar o “Read More” da baba
    E estiver na seção de “Feedbacks”
    Então devo ver a mensagem: "Não tenho feedbacks disponíveis ainda."
  
  Cenário: Visualizar feedbacks existentes da babá
    Dado que estou na página inicial
    E existam babas disponíveis
    E exista algum comentário na 1° babá
    Quando eu acessar o "Read More" da 1° babá
    E estiver na seção de "Feedbacks"
    Então devo ver os feedbacks existentes sobre a babá.

#utf-8
#language: pt

Funcionalidade: Enviar mensagem para a babá a partir da página de detalhes

Cenário: Enviar mensagem para a babá com sucesso
  Dado que tenho um perfil de usuário
  E existam babas disponíveis
  E estou na página "Detalhes da Babá"
  Quando eu seleciono a opção "enviar mensagem"
  E escrevo uma mensagem para a babá
  E confirmo o envio da mensagem
  Então devo ver uma confirmação de que a mensagem foi enviada com sucesso
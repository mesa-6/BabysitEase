#utf-8
#language: pt

Funcionalidade: Verificação do Histórico de Conversas

Cenário: Visualizar perfil da babá adicionado ao histórico de conversas com sucesso
  Dado que tenho um perfil de usuário.
  E existam babas disponíveis
  E eu acessar "Read More" da baba
  Quando eu seleciono a opção "enviar mensagem"
  E escrevo uma mensagem para a babá.
  E confirmo o envio da mensagem
  E acesso página "messages"
  Então devo conseguir visualizar meu usuário e mensagem enviada no "Histórico de Conversas"

Cenário: Visualizar histórico de conversas sem conversa prévia
  Dado que estou logado com um perfil de usuário
  E estou na página "Histórico de Mensagens"
  Quando eu não tiver enviado mensagens antes
  Então devo visualizar "Não existem conversas"
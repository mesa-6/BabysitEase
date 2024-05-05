#utf-8
#language: pt

Funcionalidade: Enviar Solicitação de Horário à baba
  Cenário: Enviar Solicitação à babá com sucesso
    Dado que tenho um perfil de usuário 
    E estou na pagina "Detalhes da Baba"
    Quando eu selecionar um horário disponível, e enviar e confirmar a solicitação
    Então devo visualizar o horário selecionado como "Pendente"

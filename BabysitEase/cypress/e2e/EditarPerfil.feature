#utf-8
#language: pt

Funcionalidade: Editar campos do perfil
  Cenário: Alterar campos já preenchidos do perfil
    Dado que tenho um perfil de usuário chamado "tiago" no site
    E esteja na página "Profile"
    Quando eu acessar "Editar Perfil", e trocar o nome para "hiago"
    Então o novo nome do perfil deve ser "hiago"

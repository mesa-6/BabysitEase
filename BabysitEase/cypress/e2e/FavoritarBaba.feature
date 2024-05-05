#utf-8
#language: pt

Funcionalidade: Favoritrar Baba
  Cenário: Favoritar Baba com sucesso
    Dado que tenho um perfil de usuário no site
    E existam babas 
    Quando eu favoritar uma babá
    Então ela deve ser visualizada com prioridade na minha lista de favoritos

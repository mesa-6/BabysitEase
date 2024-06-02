// Cenário 1
Given('que tenho um perfil de usuário', () => {
    cy.visit('/register')
    cy.cadastrar('TesteEnviarMensagem',
    '1',
    'tem@cesar.school',
    '1',
    '79996863018',
    '1990-01-01',
    'Male',
    'rua',
    'bairro',
    '12345178',
    '113')
    cy.wait(2000);
    cy.login('TesteEnviarMensagem', 
    '1' )
    cy.visit('/');
    
  });
  
  And('existam babas disponíveis', () => {
    cy.get('#SemBabasDisponiveis').should('not.exist');
    cy.wait(2000);
    cy.get('.card.h-100').should('exist');
    cy.wait(2000);
  });

  And('estou na página "Detalhes da Babá"', () => {
    cy.wait(2000);
    cy.get('.card.h-100').first().within(() => {
        cy.wait(2000);
        cy.get('.btn-readmore').click();
    });
  });
  
  When('eu seleciono a opção "enviar mensagem"', () => {
    cy.wait(2000);
    cy.get('#btnmensagem').click();

});

And('escrevo uma mensagem para a babá', () => {
    cy.wait(2000);
    cy.get('#message-text').type('Teste feedback');
  });

  And('confirmo o envio da mensagem', () => {
    cy.wait(2000);
    cy.get('#EnviarMensagemBaba').click();
  });

  Then('devo ver uma confirmação de que a mensagem foi enviada com sucesso', () => {
    cy.wait(2000);
    cy.get('#MensagemEnviadoSucesso').should('contain', 'Sua mensagem foi enviada');
    cy.wait(2000);

});


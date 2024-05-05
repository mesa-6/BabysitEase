const { Given, And, When, Then } = require("cypress-cucumber-preprocessor/lib/resolveStepDefinition")

let babysitterName = '';

// Cenário 1
Given('que tenho um perfil de usuário chamado "tiago" no site', () => {
    cy.visit('/register')
    cy.cadastrar('tiago',
    '1',
    'th@cesar.school',
    '1',
    '12345678900',
    '1990-01-01',
    'Male',
    'rua',
    'bairro',
    '12345178',
    '113')
    cy.login('tiago', 
    '1' )
    
  });
  
  And('esteja na página "Profile"', () => {
    cy.verProfile();

  });
  When('eu acessar "Editar Perfil", e trocar o nome para "hiago"', () => {
    cy.get('#EditarPerfil').click();
    cy.get('#id_first_name').clear().type('hiago');
    cy.get('#AtualizarPerfil').click();

});

  Then('o novo nome do perfil deve ser "hiago"', () => {
    cy.verProfile();
    cy.get('#username').invoke('val').should('contain', 'hiago');

});


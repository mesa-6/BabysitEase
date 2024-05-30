const { Given, And, When, Then } = require("cypress-cucumber-preprocessor/lib/resolveStepDefinition")

let babysitterName = '';

// Cenário 1
Given('que tenho um perfil de usuário no site', () => {
    cy.visit('/register')
    cy.cadastrar('teste',
    '1',
    'tst@cesar.school',
    '1',
    '12345698900',
    '1990-01-01',
    'Male',
    'rua',
    'bairro',
    '12345678',
    '123')
    cy.login('teste', 
    '1' )
  });
  
  And('existam babas', () => {
    cy.get('#SemBabasDisponiveis').should('not.exist');
    cy.wait(2000);

    cy.get('.btn.btn-outline-secondary').should('exist');
  });
  
  When('eu favoritar uma babá', () => {
    cy.wait(2000);
  cy.get('.card.h-100').first().within(() => {
    cy.get('.card-body').within(() => {
      cy.get('h5').invoke('text').then(text => {
        babysitterName = text.trim();
      });
    });
    cy.get('.btn.btn-outline-secondary').click();
  });
});
  
  Then('ela deve ser visualizada com prioridade na minha lista de favoritos', () => {
    cy.wait(2000);
    cy.get('#FavSuccess').should('exist');
    cy.wait(2000);
    cy.get('.row-cols-1.row-cols-md-4.g-4.flex-wrap > :nth-child(1) .card-body > .card-title').should('contain.text', babysitterName);

  });


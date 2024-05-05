const { Given, And, When, Then } = require("cypress-cucumber-preprocessor/lib/resolveStepDefinition")

let horarioEncontrado = false;
let idHorarioDisponivel = '';

// Cenário 1
Given('que tenho um perfil de usuário', () => {
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
  
  And('estou na pagina "Detalhes da Baba"', () => {
    cy.get('#SemBabasDisponiveis').should('not.exist');

    cy.get('.card.h-100').first().within(() => {
        cy.get('.btn-readmore').click();
      });

  });
  When('eu selecionar um horário disponível, e enviar e confirmar a solicitação', () => {
    
    cy.get('#quarta-noite').should('contain', 'Disponível');
    cy.get('#quarta-noite').click();

    
    cy.get('#confirmButton').click();
    cy.get('#confirmModal').within(() => {
        cy.get('#sendDataButton').click({ force: true });
      });

});

  Then('devo visualizar o horário selecionado como "Pendente"', () => {
    cy.get('#quarta-noite').should('contain', 'Pendente');

});


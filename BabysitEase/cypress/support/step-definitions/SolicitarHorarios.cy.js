const { Given, And, When, Then } = require("cypress-cucumber-preprocessor/lib/resolveStepDefinition")

// Cenário 1
Given('que tenho um perfil de usuário', () => {
    cy.visit('/register')
    cy.cadastrar('joao',
    '1',
    'jh@cesar.school',
    '1',
    '12885678900',
    '1990-01-01',
    'Male',
    'rua',
    'bairro',
    '12345178',
    '113')
    cy.login('joao', 
    '1' )
    
  });
  
  And('estou na pagina "Detalhes da Baba"', () => {
    cy.get('#SemBabasDisponiveis').should('not.exist');
    cy.wait(2000);
    cy.get('.card.h-100').first().within(() => {
        cy.get('.btn-readmore').click();
      });
    cy.wait(2000);

  });
  When('eu selecionar um horário disponível, e enviar e confirmar a solicitação', () => {
    cy.wait(2000);
    cy.get('#quarta-noite').should('contain', 'Disponível');
    cy.get('#quarta-noite').click();

    cy.wait(2000);
    
    cy.get('#confirmButton').click();
    cy.wait(2000);
    cy.get('#confirmModal').within(() => {
      cy.wait(2000);
        cy.get('#sendDataButton').click({ force: true });
      });
      cy.wait(2000);
});

  Then('devo visualizar o horário selecionado como "Pendente"', () => {
    cy.get('#quarta-noite').should('contain', 'Pendente');
    cy.wait(2000);
});

// Cenário 2
Given('que tenho login em um perfil de usuário', () => {
    cy.wait(2000);  
    cy.visit('/login')
    cy.wait(2000);
    cy.login('joao', 
    '1' )
    
  });
  
  And('estou na pagina "Detalhes da Baba"', () => {
    cy.get('#SemBabasDisponiveis').should('not.exist');
    cy.wait(2000);
    cy.get('.card.h-100').first().within(() => {
      cy.wait(2000);
        cy.get('.btn-readmore').click();
      });
      cy.wait(2000);

  });
  When('eu selecionar botão de Solicitar e confirmar sem antes selecionar um horário', () => {
    
    cy.get('#confirmButton').click();
    cy.wait(2000);
    cy.get('#confirmModal').within(() => {
      cy.wait(2000);
        cy.get('#sendDataButton').click({ force: true });
        cy.wait(2000);
      });

});

  Then('devo visualizar mensagem "Por favor, selecione pelo menos um horário."', () => {
    cy.wait(2000);
    cy.get('#aoMenosUmHorario').should('contain', 'Por favor, selecione pelo menos um horário.');

});
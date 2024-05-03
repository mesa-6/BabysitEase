const { Given, And, When, Then } = require("cypress-cucumber-preprocessor/lib/resolveStepDefinition");

let babysitterName;
let babysitterDescription;

// Cenário 1
Given('que estou na página inicial', () => {
  cy.visit('/');

});

And('existam babas disponíveis', () => {
  cy.get('#SemBabasDisponiveis').should('not.exist');
  cy.get('.card.h-100').should('exist');
  cy.wait(2000);
});

When('eu acessar "Read More" da baba', () => {
    cy.get('.card.h-100').first().within(() => {
        cy.get('.card-body').within(() => {
          cy.get('h5').invoke('text').then(text => {
            babysitterName = text.trim(); 
          });
          cy.get('p').invoke('text').then(text => {
            babysitterDescription = text.trim(); 
          });
        });
        cy.get('.btn-readmore').click();
      });
    });
    

Then('devo conseguir visualizar as mesmas informações da baba selecionada', () => {
    cy.get('.card').first().within(() => {
        cy.get('.card-body').within(() => {
          cy.get('h5').invoke('text').then(detailName => {
            expect(detailName.trim()).to.equal(babysitterName);
          });
          cy.get('p').invoke('text').then(detailDescription => {
            expect(detailDescription.trim()).to.equal(babysitterDescription);
          });
        });
      });
    });

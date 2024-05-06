const { Given, And, When, Then } = require("cypress-cucumber-preprocessor/lib/resolveStepDefinition")

// Cenário 1
Given('que estou na página inicial', () => {
    cy.visit('/');
    
  });
  
  And('a barra lateral está aberta', () => {
    cy.get('.toggle-btn').click();
    cy.wait(2000);
  });
  
  When('seleciono e confirmo um filtro de preço', () => {
    cy.wait(2000);
    cy.get('[data-bs-target="#location"]').click();
    cy.wait(2000);
    cy.get('input[value="41,60"]').click();
    cy.wait(2000);
    cy.get('#filtroPreco').click();
  });
  
  Then('devo conseguir visualizar apenas as babás que se enquadram nessa faixa de preço', () => {
    cy.get('#SemBabasDisponiveis').should('not.exist');
    cy.wait(2000);
    
    cy.get('.card.h-100').each(($card) => {
        const priceText = $card.find('.card-footer small').text().replace('Preço/Hora: R$ ', '');
        const price = parseFloat(priceText.replace(',', '.'));
        expect(price).to.be.greaterThan(41.60);
      });
      cy.wait(2000);

  });
  

// Cenário 2
Given('que estou na página inicio', () => {
    cy.visit('/');
    cy.wait(2000);
  });
  
  And('a barra lateral está aberta', () => {
    cy.get('.toggle-btn').click();
    cy.wait(2000);
  });
  
  When('seleciono um filtro que não contém babas disponíveis', () => {
    cy.get('[data-bs-target="#location"]').click();
    cy.wait(2000);
    cy.get('#low-price').click();
    cy.wait(2000);
    cy.get('#filtroPreco').click();
    cy.wait(2000);
  });
  
  Then('devo conseguir visualizar apenas a mensagem: "Não há babás disponíveis"', () => {
    cy.get('#SemBabasDisponiveis').should('exist');
    cy.wait(2000);
  });

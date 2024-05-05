Cypress.Commands.add('verHome', () => {
    cy.visit('/');
    cy.url().should('equal', 'http://127.0.0.1:8000/');
})
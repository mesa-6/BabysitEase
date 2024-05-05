Cypress.Commands.add('verProfile', () => {
    cy.visit('/profile');
    cy.url().should('equal', 'http://127.0.0.1:8000/profile/');
})
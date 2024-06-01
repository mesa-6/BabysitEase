Cypress.Commands.add('loginComoAdmin', () => {
    cy.visit('/admin/login/');
    
    cy.get('input[name="username"]').type('gheyson');
    cy.get('input[name="password"]').type('1234');
    cy.get('input[type="submit"]').click();
    
    cy.url().should('contain', '/admin/');
})
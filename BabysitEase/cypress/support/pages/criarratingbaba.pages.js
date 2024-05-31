Cypress.Commands.add('criarRatingBaba', (babysitterId, userId, rating) => {
    cy.visit('/admin/base/babysitterrating/add/');
    
    // Preenche os campos do formulário
    cy.get('#id_babysitter').select(babysitterId);
    cy.get('#id_user').select(userId);
    cy.get('#id_rating').type(rating);
    
    // Submete o formulário
    cy.get('input[name="_save"]').click();
    
    // Verifica se a entrada de babysitterrating foi criada com sucesso
    cy.url().should('contain', '/admin/base/babysitterrating/');
    cy.contains(`${babysitterId} - ${userId}`).should('exist'); // Verifica se a entrada é exibida corretamente
    cy.contains(`${rating}`).should('exist'); // Verifica se o rating é exibido corretamente
    
    // Volta para a página inicial do site
    cy.visit('/babysitter-dtl/' + babysitterId);
  });

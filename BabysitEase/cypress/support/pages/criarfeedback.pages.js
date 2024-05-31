Cypress.Commands.add('criarFeedback', (babysitterId, userName, mensagem) => {
    cy.visit('/admin/base/feedback/add/');
    
    // Preenche os campos do formulário
    cy.get('#id_babysitter').select(babysitterId);
    cy.get('#id_user').select(userName);
    cy.get('#id_rating').type('5');
    cy.get('#id_feedback').type(mensagem);
    
    // Submete o formulário
    cy.get('input[name="_save"]').click();
    
    // Verifica se a entrada de feedback foi criada com sucesso
    cy.url().should('contain', '/admin/base/feedback/');
    cy.contains(mensagem).should('exist');
    
    // Volta para a página inicial do site
    cy.visit('/');
  });
  
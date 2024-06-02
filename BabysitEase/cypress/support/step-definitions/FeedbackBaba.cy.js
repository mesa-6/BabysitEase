// Cenário 1
Given('que estou na página inicial', () => {
    cy.visit('/');
  
  });
  
And('existam babas disponíveis', () => {
    cy.get('#SemBabasDisponiveis').should('not.exist');
    cy.wait(2000);
    cy.get('.card.h-100').should('exist');
    cy.wait(2000);
});
  
When('eu acessar o “Read More” da baba', () => {
cy.wait(2000);
    cy.get('.card.h-100').first().within(() => {
        cy.wait(2000);
        cy.get('.btn-readmore').click();
    });
});

And('estiver na seção de “Feedbacks”', () => {
    cy.wait(2000);
    cy.get('#feedbacksTitle').should('exist');

});

Then('devo ver a mensagem: "Não tenho feedbacks disponíveis ainda."', () => {
    cy.wait(2000);
    cy.get('#noFeedbackMessage').should('exist').and('contain', 'Não tenho feedbacks disponíveis ainda.');
    cy.wait(5000);
});



// Cenário 2
Given('que estou na página inicial', () => {
    cy.visit('/');
});
    
And('existam babas disponíveis', () => {
    cy.get('#SemBabasDisponiveis').should('not.exist');
    cy.wait(2000);
    cy.get('.card.h-100').should('exist');
    cy.wait(2000);
});

And('exista algum comentário na 1° babá', () => {
    // Execute as etapas específicas do Cenário 2 aqui
    cy.visit('/register');
    cy.cadastrar('testfeedback', '1', 'th@cesar.school', '1', '12345633330', '1990-01-01', 'Male', 'rua', 'bairro', '12345178', '113');
    cy.login('testfeedback', '1');
    cy.visit('/');
    cy.get('.card.h-100').first().within(() => {
        cy.get('.btn-readmore').click();
    });
    return cy.extrairNumeroDoURL().then(numero => {
        // Execute as etapas que dependem do número extraído do URL
        cy.loginComoAdmin();
        cy.wait(2000);
        cy.criarFeedback(numero, 'testfeedback', 'Excelente Serviço!');
        cy.wait(2000);
        cy.visit('/');
    });
});
    
When('eu acessar o "Read More" da 1° babá', () => {
    cy.wait(2000);
    cy.get('.card.h-100').first().within(() => {
        cy.wait(2000);
        cy.get('.btn-readmore').click();
    });
});

And('estiver na seção de "Feedbacks"', () => {
    cy.get('#feedbacksTitle').should('exist');
});

Then('devo ver os feedbacks existentes sobre a babá.', () => {
    cy.wait(2000);
    cy.get('.feedback').should('have.length.gt', 0);
});


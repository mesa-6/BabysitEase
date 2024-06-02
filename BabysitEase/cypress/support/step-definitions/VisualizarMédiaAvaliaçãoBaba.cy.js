// Cenário 1
Given('que estou na home', () => {
    cy.visit('/');
});

And('existam babas disponíveis', () => {
    cy.get('#SemBabasDisponiveis').should('not.exist');
    cy.wait(2000);
    cy.get('.card.h-100').should('exist');
    cy.wait(2000);
});

When('eu acessar "Read More" da baba', () => {
    cy.wait(2000);
    cy.get('.card.h-100').first().within(() => {
        cy.wait(2000);
        cy.get('.btn-readmore').click();
    });

});

And('a babá ainda não foi avaliada', () => {
    
});

Then('devo visualizar uma mensagem “Ops! Nenhuma avaliação disponível.”', () => {
    cy.wait(2000);
    cy.get('.no-rating-message').should('exist');
    
});

// Cenário 2
Given('que estou na home', () => {
    cy.visit('/');
});

And('existam babas disponíveis', () => {
    cy.get('#SemBabasDisponiveis').should('not.exist');
    cy.wait(2000);
    cy.get('.card.h-100').should('exist');
    cy.wait(2000);
});

When('eu acessar "Read More" da baba que já foi avaliada', () => {
    
    cy.wait(2000);
    cy.get('.card.h-100').first().within(() => {
        cy.wait(2000);
        cy.get('.btn-readmore').click();
    });

    return cy.extrairNumeroDoURL().then(numero => {
        // Execute as etapas que dependem do número extraído do URL
        cy.loginComoAdmin();
        cy.wait(2000);
        cy.criarRatingBaba(numero, 'gheyson', 5);
        cy.wait(2000);
        cy.visit('/babysitter-dtl/' + numero);
    });

});

Then('devo visualizar uma média das avaliações da babá', () => {
    cy.wait(2000);
    cy.get('.rating-message').should('exist');
    
});

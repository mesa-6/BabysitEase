let MensagemVizTeste = "Teste Visualizar Mensagem";

// Cenário 1
Given('que tenho um perfil de usuário.', () => {
    cy.visit('/register');
    cy.cadastrar('testevizmensagem',
    '1',
    'tem@cesar.school',
    '1',
    '42640586009',
    '1990-01-01',
    'Male',
    'rua',
    'bairro',
    '12345178',
    '113');
    cy.wait(2000);
    cy.login('testevizmensagem', '1');
});

And('existam babas disponíveis', () => {
    cy.get('#SemBabasDisponiveis').should('not.exist');
    cy.wait(2000);
    cy.get('.card.h-100').should('exist');
    cy.wait(2000);
});

And('eu acessar "Read More" da baba', () => {
    cy.wait(2000);
    cy.get('.card.h-100').first().within(() => {
        cy.wait(2000);
        cy.get('.btn-readmore').click();
    });

});

When('eu seleciono a opção "enviar mensagem"', () => {
    cy.wait(2000);
    cy.get('#btnmensagem').click();
});

And('escrevo uma mensagem para a babá.', () => {
    cy.wait(2000);
    cy.get('#message-text').type(MensagemVizTeste);
});

And('confirmo o envio da mensagem', () => {
    cy.wait(2000);
    cy.get('#EnviarMensagemBaba').click();
});

And('acesso página "messages"', () => {
    cy.wait(2000);
    cy.get('#MensagemEnviadoSucesso').should('contain', 'Sua mensagem foi enviada');
    cy.wait(2000);
    cy.get('#IrPaginaMensagens').click();
});

Then('devo conseguir visualizar meu usuário e mensagem enviada no "Histórico de Conversas"', () => {
    cy.url().should('equal', 'http://127.0.0.1:8000/messages/');
    cy.wait(2000);
    cy.get('#UsuarioMensagem').should('contain', 'testevizmensagem');
    cy.wait(2000);
    cy.get('#MensagemParaBaba').should('contain', MensagemVizTeste);
});

// Cenário 2
Given('que estou logado com um perfil de usuário', () => {
    cy.visit('/register');
    cy.cadastrar('testevizmensagem2',
    '1',
    'tem2@cesar.school',
    '1',
    '95444649055',
    '1990-01-01',
    'Male',
    'rua',
    'bairro',
    '12345178',
    '113');
    cy.wait(2000);
    cy.login('testevizmensagem2', '1');
});

And('estou na página "Histórico de Mensagens"', () => {
    cy.visit('/messages')
    cy.wait(2000);
    cy.url().should('eq', 'http://127.0.0.1:8000/messages/');
});

When('eu não tiver enviado mensagens antes', () => {
});

Then('devo visualizar "Não existem conversas"', () => {
    cy.wait(2000);
    cy.contains('.text-center', 'Ops! Você não tem nenhuma conversa ainda.').should('exist');

});

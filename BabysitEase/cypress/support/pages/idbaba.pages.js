Cypress.Commands.add('extrairNumeroDoURL', () => {
    return cy.url().then(url => {
      const parts = url.split('/');
      const numero = parts[parts.length - 2]; // Aqui pega a penúltima parte, onde tá o id da babá
      return numero;
    });
  })
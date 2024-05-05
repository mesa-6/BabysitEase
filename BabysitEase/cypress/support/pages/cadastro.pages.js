const INPUT_NOME = '#name'
const INPUT_LAST_NAME = '#last_name'
const INPUT_EMAIL = '#email'
const INPUT_SENHA = '#password'
const INPUT_CPF = '#cpf'
const INPUT_BIRTH_DATE = '#birth_date'
const INPUT_SEX = '#sex'
const INPUT_STREET = '#street'
const INPUT_NEIGHBORHOOD = '#neiborhood'
const INPUT_ZIP_CODE = '#zip_code'
const INPUT_NUMBER = '#number'
const BUTTON_SUBMIT = '.btn-primary' 

Cypress.Commands.add('cadastrar', (nome, sobrenome, email, senha, cpf, dataNascimento, sexo, rua, bairro, cep, numero) => {
    cy.get(INPUT_NOME).type(nome)
    cy.get(INPUT_LAST_NAME).type(sobrenome)
    cy.get(INPUT_EMAIL).type(email)
    cy.get(INPUT_SENHA).type(senha)
    cy.get(INPUT_CPF).type(cpf)
    cy.get(INPUT_BIRTH_DATE).type(dataNascimento)
    cy.get(INPUT_SEX).select(sexo)
    cy.get(INPUT_STREET).type(rua)
    cy.get(INPUT_NEIGHBORHOOD).type(bairro)
    cy.get(INPUT_ZIP_CODE).type(cep)
    cy.get(INPUT_NUMBER).type(numero)
    cy.get(BUTTON_SUBMIT).click()
})


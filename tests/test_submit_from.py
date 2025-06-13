import pytest
from selene import browser, have


def test_submit_form():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://demoqa.com/automation-practice-form')


    # Заполняем имя
    browser.element('#firstName').type('Michael')

    # Заполняем фамилию
    browser.element('#lastName').type('Rodionov')

    # Заполняем email
    browser.element('#userEmail').type('jaosnjgotnasgnon@asnfomnoas.weq')

    # Выбираем пол
    browser.element('.custom-control-label').click()

    # Заполняем номер телефона
    browser.element('#userNumber').type('0123456789')

    # Заполняем дату рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1997"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="3"]').click()
    browser.element('[aria-label="Choose Friday, April 11th, 1997"]').click()

    # Заполняем объект
    browser.element('#subjectsInput').type('e')
    browser.element('#react-select-2-option-0').click()
    browser.element('#subjectsInput').type('e')
    browser.element('#react-select-2-option-1').click()

    # Выбираем хобби
    browser.element('.custom-control-label').click()

    # Заполняем адрес
    browser.element('#currentAddress').type('Russia, Moscow, st.Pushkina, h.23')

    # Выбираем страну
    browser.element('#state').click()
    browser.element('#react-select-3-option-2').click()

    # Выбираем город
    browser.element('#city').click()
    browser.element('#react-select-4-option-1').click()

    browser.element('#submit').click()

    # Проверяем, что форма отправлена
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

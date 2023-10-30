import os
import re
from selenium.webdriver.support.ui import Select
from config import ConfigDriver


class TestCasePositive(ConfigDriver):
    def test_name(cls):
        att_ids = ['firstName', 'lastName']
        values = ['Maulana', 'Anwar']

        for element_id, value in zip(att_ids, values):
            element = cls.driver.find_element(cls.BY.ID, f'{element_id}')
            element.send_keys(f'{value}')
            assert element.get_attribute('type') == 'text'
            assert element.get_attribute('value') == value
            assert element.get_attribute('required')

    def test_email(cls):
        value = 'himaulanaa@gmail.com'
        element = cls.driver.find_element(cls.BY.ID, 'userEmail')
        element.send_keys(value)

        assert element.get_attribute('value') == value

    def test_phone_number(cls):
        value = '0895808372'
        element = cls.driver.find_element(cls.BY.ID, 'userNumber')
        element.send_keys(value)

        assert element.get_attribute('value') == value
        assert element.get_attribute('required')
        assert element.get_attribute(
            'minlength') == '10' and element.get_attribute('maxlength') == '10'

    def test_gender(cls):
        element = cls.WAIT(cls.driver, 10).until(
            cls.EC.presence_of_element_located((cls.BY.ID, 'gender-radio-1')))
        cls.driver.execute_script("arguments[0].click();", element)

        assert element.is_selected()

    def test_date_birth(cls):
        date = cls.WAIT(cls.driver, 10).until(
            cls.EC.presence_of_element_located((cls.BY.XPATH, '//*[@id="dateOfBirthInput"]')))
        cls.driver.execute_script("arguments[0].click();", date)

        year = Select(cls.WAIT(cls.driver, 10).until(cls.EC.presence_of_element_located(
            (cls.BY.XPATH, '//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select'))))

        month = Select(cls.WAIT(cls.driver, 10).until(cls.EC.presence_of_element_located(
            (cls.BY.XPATH, '//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select'))))

        year.select_by_visible_text('2001')
        month.select_by_visible_text('May')

        day = cls.driver.find_element(cls.BY.XPATH, "//div[text()='12']")
        day.click()

        value_date = cls.driver.find_element(cls.BY.ID, 'dateOfBirthInput')

        assert value_date.get_attribute('value') == '12 May 2001'

    def test_hobbie(cls):
        element = cls.WAIT(cls.driver, 10).until(
            cls.EC.presence_of_element_located((cls.BY.ID, 'hobbies-checkbox-3')))
        cls.driver.execute_script("arguments[0].click();", element)

        assert element.is_selected()

    def test_upload_img(cls):
        element = cls.driver.find_element(
            cls.BY.CLASS_NAME, 'form-control-file')
        element.send_keys(os.getcwd() + '/public/Maulana Anwar.jpg')

    def test_address(cls):
        element = cls.driver.find_element(cls.BY.ID, 'currentAddress')
        element.send_keys(
            'Kp. Bulak Teko RT 003/011 Kel. Kalideres, Kclscls.EC. Kalideres, Jakarta Barat, Jakarta')

    def test_submit(cls):
        btn_submit = cls.driver.find_element(cls.BY.ID, 'submit')

        if btn_submit.is_displayed():
            btn_submit.submit()

        try:
            title_modal = cls.WAIT(cls.driver, 10).until(
                cls.EC.visibility_of_element_located((cls.BY.ID, 'example-modal-sizes-title-lg')))

            match = re.search('thanks', title_modal.text, re.IGNORECASE)

            assert match is not None
            cls.driver.quit()

        except:
            cls.driver.quit()

    @classmethod
    def teardown_class(cls):
        if cls.driver:
            cls.driver.quit()

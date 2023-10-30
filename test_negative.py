import time
from config import ConfigDriver


class TestCaseNegative(ConfigDriver):
    def test_invalid_name(cls):
        att_ids = ['firstName', 'lastName']
        values = ['', '']

        for element_id, value in zip(att_ids, values):
            element = cls.driver.find_element(cls.BY.ID, f'{element_id}')
            element.send_keys(f'{value}')

            cls.submit()
            border_color = element.value_of_css_property('border-color')
            assert border_color == 'rgb(220, 53, 69)'

    def test_invalid_email(cls):
        value = 'himaulanaagmail.com'
        element = cls.driver.find_element(cls.BY.ID, 'userEmail')
        element.send_keys(value)

        cls.submit()
        border_color = element.value_of_css_property('border-color')
        assert border_color == 'rgb(220, 53, 69)'

    def test_gender_empty(cls):
        cls.submit()

        for i in range(1, 3):
            element = cls.WAIT(cls.driver, 5).until(
                cls.EC.presence_of_element_located((cls.BY.XPATH, f'//*[@id="genterWrapper"]/div[2]/div[{i}]/label')))

            color = element.value_of_css_property('color')
            assert color == 'rgba(220, 53, 69, 1)'

    def test_empty_phone_number(cls):
        cls.submit()

        element = cls.driver.find_element(cls.BY.ID, 'userNumber')

        border_color = element.value_of_css_property('border-color')
        assert border_color == 'rgb(220, 53, 69)'

    def test_invalid_phone_number(cls):
        value = 'lore9878x'
        element = cls.driver.find_element(cls.BY.ID, 'userNumber')
        element.send_keys(value)

        cls.submit()

        border_color = element.value_of_css_property('border-color')
        assert border_color == 'rgb(220, 53, 69)'

    def test_size_phone_number(cls):
        value = '0895909672182'
        element = cls.driver.find_element(cls.BY.ID, 'userNumber')
        element.send_keys(value)

        cls.submit()
        element_value = cls.driver.find_element(
            cls.BY.ID, 'userNumber').get_attribute('value')

        assert len(element_value) == 10

    def test_default_value_date(cls):
        cls.submit()

        element_date = cls.WAIT(cls.driver, 10).until(
            cls.EC.presence_of_element_located((cls.BY.XPATH, '//*[@id="dateOfBirthInput"]')))
        date_value = element_date.get_attribute('value')

        assert date_value is not None

    def submit(cls):
        btn_submit = cls.driver.find_element(cls.BY.ID, 'submit')
        btn_submit.submit()

        time.sleep(2)

    @classmethod
    def teardown_class(cls):
        if cls.driver:
            cls.driver.quit()

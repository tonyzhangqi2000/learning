from selenium.webdriver.support.select import Select

from day0802.demo01_v1_locator import Page_Register_Locator


class MyComments:
    def __init__(self, driver):
        self.prl = Page_Register_Locator()
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def type_name(self, n):
        name = self.driver.find_element(*self.prl.findName)
        name.send_keys(n)

    def type_password(self, n):
        password = self.driver.find_element(*self.prl.findPassword)
        password.send_keys(n)

    def click_male(self):
        male = self.driver.find_element(*self.prl.findMale)
        male.click()

    def click_female(self):
        female = self.driver.find_element(*self.prl.findFemale)
        female.click()

    def type_email(self, n):
        email = self.driver.find_element(*self.prl.findEmail)
        email.send_keys(n)

    def select_profession(self, n):
        profession = self.driver.find_element(*self.prl.findProfession)
        ps = Select(profession)
        ps.select_by_visible_text(n)

    def click_computer(self):
        computer = self.driver.find_element(*self.prl.findComputer)
        computer.click()

    def click_film(self):
        film = self.driver.find_element(*self.prl.findFilm)
        film.click()

    def click_chess(self):
        chess = self.driver.find_element(*self.prl.findChess)
        chess.click()

    def click_read(self):
        read = self.driver.find_element(*self.prl.findRead)
        read.click()

    def click_food(self):
        food = self.driver.find_element(*self.prl.findFood)
        food.click()

    def click_painting(self):
        painting = self.driver.find_element(*self.prl.findPainting)
        painting.click()

    def type_comments(self, n):
        comments = self.driver.find_element(*self.prl.findComments)
        comments.send_keys(n)

    def click_submit(self):
        submit = self.driver.find_element(*self.prl.findSubmit)
        submit.click()

    def click_submit2(self):
        submit2 = self.driver.find_element(*self.prl.findSubmit2)
        submit2.click()

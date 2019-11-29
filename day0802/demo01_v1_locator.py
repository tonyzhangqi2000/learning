from selenium.webdriver.common.by import By


class Page_Register_Locator:

    def __init__(self):
        self.findName = (By.NAME, "username")
        self.findPassword = (By.NAME, "passwords")
        self.findMale = (By.XPATH, "/html/body/form/table/tbody/tr[4]/td[2]/font/input[1]")
        self.findFemale = (By.XPATH, "/html/body/form/table/tbody/tr[4]/td[2]/font/input[2]")
        self.findEmail = (By.NAME, "email")
        self.findProfession = (By.NAME, "profession")
        self.findComputer = (By.NAME, "computer")
        self.findFilm = (By.NAME, "film")
        self.findChess = (By.NAME, "chess")
        self.findRead = (By.NAME, "read")
        self.findFood = (By.NAME, "food")
        self.findPainting = (By.NAME, "painting")
        self.findComments = (By.NAME, "textfield")
        self.findSubmit = (By.NAME, "submit")
        self.findSubmit2 = (By.NAME, "submit2")

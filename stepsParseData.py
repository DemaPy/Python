from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from multiprocessing import Pool
import time
driver = webdriver.Chrome()


SOCIALS = ["instagram"]
INSTA = "instagram"

# # Задаем ключ API для OpenAI
# API_KEY = "YOUR_API_KEY_HERE"

# # Создаем драйвер браузера Chrome

# def getById(id):
#     return driver.find_element("id", id)

# # Переходим на сайт OpenAI API и авторизуемся
# driver.get("https://beta.openai.com/login/")
# time.sleep(5)
# email_input = getById("username")
# email_input.send_keys("benderdema@gmail.com")
# driver.find_element("xpath","/html/body/main/section/div/div/div/form/div[2]/button").click()
# time.sleep(5)

# password = getById("password")
# password.send_keys("oturig02")
# driver.find_element(By.CLASS_NAME, "ca4ba6ae0").click()
# time.sleep(50)

mainPhrase = {
    "EN": "Please, can you write post for me on theme: ",
    "RU": "Пожалуйста, можешь ли ты написать текст для меня на тему: "
}
posts = [
    {
        "img": "slava.jpg",
        "text": "Baltic Sea.",
        "textContent": 'The Baltic Sea is a body of water located in Northern Europe, surrounded by countries such as Sweden, Finland, Russia, Estonia, Latvia, Lithuania, Poland, and Germany. It is the largest brackish water sea in the world, meaning it is a mixture of saltwater and freshwater. The Baltic Sea has been an important resource for the people living around it for centuries, providing food, transportation, and a source of trade.'
    }
]


class Socials:
    socials = {}

    def addSocial(self, name, options):
        self.socials[name] = options

    def getSocial(self):
        return self.socials
    
    def email(self, type):
        return self.socials[type]["email"]
    
    def password(self, type):
        return self.socials[type]["password"]
    


class LoginPath:
    steps = []

    def nextStep(self):
        pass
    
    def setStep(self, by, step, type):
        self.steps.append([by, step, type])

    def getAllSteps(self):
        return self.steps


social = Socials()
loginInsta = LoginPath()

loginInsta.setStep("js", "document.querySelector('._a9--._a9_0').click()", "script")
loginInsta.setStep(By.NAME, "username", "email")
loginInsta.setStep(By.NAME, "password", "password")
loginInsta.setStep(By.CLASS_NAME, "_acan._acap._acas._aj1-", "click")

createPost = LoginPath()

createPost.setStep("js", 'document.querySelectorAll(".x9f619.xxk0z11.xvy4d1p.x11xpdln.xii2z7h.x19c4wfv")[7].click()', 'script')
createPost.setStep("js", 'document.querySelector("._acan._acap._acas._aj1-").click()', 'script')


social.addSocial(
INSTA,
{
    "link": "https://www.instagram.com/",
    "password": "benderslavaua18",
    "email": "+48728708675"
})


def steps():
    steps = []

    def addStep(step):
        steps.append(step)

    def getSteps():
        return steps

    return addStep, getSteps


stepsArr = steps()

addStep = stepsArr[0]
addStep(loginInsta)
addStep(createPost)

getStep = stepsArr[1]





def getBy(by, selector, type):
    if type == "script":
        driver.execute_script(selector)
    elif type == "click":
        driver.find_element(by, selector).click()
        print("Selector %s has been found. Clicked." % selector)
    else:
        driver.find_element(by, selector).send_keys(getattr(social, type)(INSTA))
        print("Selector %s has been found. Keep working on it" % selector)


def openLink(link):
    driver.get(link)
    time.sleep(5)
    for stepObj in getStep():
        for step in getattr(stepObj, "getAllSteps")():
            getBy(step[0], step[1], step[2])
            time.sleep(10)

def login(type):
    if type == INSTA:
        openLink(social.getSocial()[type]["link"])



if __name__ == "__main__":
    amountOfProcess = int(input("Amount of proccesses: "))
    multiply = SOCIALS * amountOfProcess
    Pool(amountOfProcess).map(login, multiply)
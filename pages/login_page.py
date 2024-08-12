from abc import ABC, abstractmethod

class Page(ABC):
    def __init__(self, driver):
        self.driver = driver
    
    @abstractmethod
    def is_loaded(self):
        pass


class HeaderComponent:
    def __init__(self, driver):
        self.driver = driver
    
    def click_profile(self):
        profile_button = self.driver.find_element(By.ID, "profile")
        profile_button.click()

class LoginPage(Page):
    def is_loaded(self):
        return "Login" in self.driver.title

    def open_link(self, url):
        self.driver.get(url)
  
    def enter_username(self, username):
        self.send_keys(self._username_locator, username)
        return self  # Allow chaining

    def enter_password(self, password):
        self.send_keys(self._password_locator, password)
        return self  # Allow chaining

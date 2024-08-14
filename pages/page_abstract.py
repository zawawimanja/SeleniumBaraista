from abc import ABC, abstractmethod

# If you have multiple types of pages (e.g., LoginPage, HomePage, etc.), and they share common behaviors (e.g., navigating or checking if a page is loaded),
# you could define an abstract base class that enforces these behaviors.


class Page(ABC):
    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def is_loaded(self):
        """Check if the page is loaded."""
        pass

    @abstractmethod
    def open_link(self):
        """Check if the page is loaded."""
        pass

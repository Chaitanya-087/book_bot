import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from robot.libraries.BuiltIn import BuiltIn

BRAVE_BINARY = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
BRAVE_PROFILE_DIR = "/Users/chaitanya/Library/Application Support/BraveSoftware/Brave-Browser"


class BrowserSetup:

    def open_chrome_session(self):
        """Opens Brave with existing user session. Optimised for zero-lag booking."""
        # Remove stale profile locks
        for lock in ["SingletonLock", "SingletonCookie", "SingletonSocket"]:
            lock_path = os.path.join(BRAVE_PROFILE_DIR, lock)
            if os.path.exists(lock_path):
                os.remove(lock_path)

        options = webdriver.ChromeOptions()
        options.binary_location = BRAVE_BINARY
        options.add_argument(f"--user-data-dir={BRAVE_PROFILE_DIR}")
        options.add_argument("--profile-directory=Default")
        options.add_argument("--no-first-run")
        options.add_argument("--no-default-browser-check")
        options.add_argument("--disable-sync")
        options.add_argument("--start-maximized")
        # Eager load — don't wait for all resources, act as soon as DOM is ready
        options.page_load_strategy = "eager"
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        driver = webdriver.Chrome(options=options)

        selenium_lib = BuiltIn().get_library_instance("SeleniumLibrary")
        selenium_lib.register_driver(driver, alias="brave")
        return driver

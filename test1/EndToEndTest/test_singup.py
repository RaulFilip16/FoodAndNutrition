import re
from playwright.sync_api import Page, expect


def test_singup(page: Page) -> None:
    page.goto("http://127.0.0.1:8000/accounts/authentication/")
    page.get_by_role("link", name="Sign Up").click()
    page.get_by_placeholder("Enter your username").click()
    page.get_by_placeholder("Enter your username").fill("paco2")
    page.get_by_placeholder("Enter your password").click()
    page.get_by_placeholder("Enter your password").fill("paco2")
    page.get_by_placeholder("Enter your email").click()
    page.get_by_placeholder("Enter your email").fill("paco2@gmail.com")
    page.get_by_role("button", name="Sign Up").click()
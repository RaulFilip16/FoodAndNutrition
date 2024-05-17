import re
from playwright.sync_api import Page, expect


def test_login_logout(page: Page) -> None:
    page.goto("http://127.0.0.1:8000/")
    page.get_by_role("link", name="Log In").click()
    page.get_by_placeholder("Enter your username").click()
    page.get_by_placeholder("Enter your username").fill("admin")
    page.get_by_placeholder("Enter your password").click()
    page.get_by_placeholder("Enter your password").fill("kebab")
    page.get_by_role("button", name="Log In").click()
    page.get_by_placeholder("Enter your username").click()
    page.get_by_placeholder("Enter your username").fill("admin")
    page.get_by_placeholder("Enter your password").click()
    page.get_by_placeholder("Enter your password").fill("los4fantasticos")
    page.get_by_role("button", name="Log In").click()
    page.get_by_role("link", name="Home").click()
    page.get_by_role("link", name="About Us").click()
    page.get_by_role("link", name="Contact").click()
    page.get_by_role("link", name="Home").click()
    page.get_by_role("button", name="Log Out").click()
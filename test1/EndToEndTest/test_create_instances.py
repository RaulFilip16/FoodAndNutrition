import re
from playwright.sync_api import sync_playwright


def test_create_instances():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("http://127.0.0.1:8000/")
        page.get_by_role("link", name="Log In").click()
        page.get_by_placeholder("Enter your username").fill("admin")
        page.get_by_placeholder("Enter your password").fill("los4fantasticos")
        page.get_by_placeholder("Enter your password").press("Enter")
        page.click("text='Consulta tus estadísticas'")
        page.click("text='Añadir'")
        page.wait_for_selector("#addPlatoModal.show", state="visible", timeout=5000)
        page.fill('#addPlatoModal input[name="name"]', "Eggs")
        page.fill('#addPlatoModal input[name="grams"]', "100")
        page.select_option('#addPlatoModal select[name="meal"]', 'Desayuno')
        page.click('#addPlatoModal button[type="submit"]')
        page.wait_for_selector("text='Eggs'", timeout=5000)
        assert page.is_visible("text='Eggs'")

        browser.close()


if __name__ == "__main__":
    test_create_instances()

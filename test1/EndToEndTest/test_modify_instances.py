from playwright.sync_api import sync_playwright


def test_modify_plato():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("http://127.0.0.1:8000/")
        page.get_by_role("link", name="Log In").click()
        page.get_by_placeholder("Enter your username").fill("admin")
        page.get_by_placeholder("Enter your password").fill("los4fantasticos")
        page.get_by_placeholder("Enter your password").press("Enter")
        page.click("text='Consulta tus estadísticas'")
        page.wait_for_selector("button[data-bs-target='#modifyPlatoModal']", timeout=5000)
        page.click("button[data-bs-target='#modifyPlatoModal']")
        page.wait_for_selector("#modifyPlatoModal.show", state="visible", timeout=5000)
        page.fill('#modifyPlatoModal input[name="name"]', "Plato Modificado")
        page.fill('#modifyPlatoModal input[name="grams"]', "200")
        page.select_option('#modifyPlatoModal select[name="meal"]', 'Desayuno')
        page.click('#modifyPlatoModal button[type="submit"]')
        page.wait_for_selector("text='Plato Modificado'", timeout=5000)
        assert page.is_visible("text='Plato Modificado'")

        browser.close()


if __name__ == "__main__":
    test_modify_plato()

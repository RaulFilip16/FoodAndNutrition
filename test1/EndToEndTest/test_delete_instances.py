from playwright.sync_api import sync_playwright


def test_delete_instances():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("http://127.0.0.1:8000/")
        page.get_by_role("link", name="Log In").click()
        page.get_by_placeholder("Enter your username").fill("admin")
        page.get_by_placeholder("Enter your password").fill("los4fantasticos")
        page.get_by_placeholder("Enter your password").press("Enter")
        page.click("text='Consulta tus estadísticas'")
        page.wait_for_selector("button[data-bs-target='#deletePlatoModal']", timeout=5000)
        page.click("button[data-bs-target='#deletePlatoModal']")
        page.wait_for_selector("#deletePlatoModal.show", state="visible", timeout=5000)
        page.click('#deletePlatoModal button[type="submit"]')
        page.wait_for_selector("#deletePlatoModal", state="hidden", timeout=5000)
        page.wait_for_timeout(1000)
        assert not page.is_visible("text='Eggs'")

        browser.close()

if __name__ == "__main__":
    test_delete_instances()

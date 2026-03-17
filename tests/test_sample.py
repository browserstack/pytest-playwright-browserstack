from playwright.sync_api import expect


def test_add_product_to_cart(page):
    page.goto("https://bstackdemo.com/")
    page.locator("[id=\"\\31 \"]").wait_for()

    product_name = page.locator("[id=\"\\31 \"] .shelf-item__title").inner_text()
    page.locator("[id=\"\\31 \"] .shelf-item__buy-btn").click()

    cart = page.locator(".float-cart__content")
    cart.wait_for()
    expect(cart.locator(".shelf-item__details .title")).to_have_text(product_name)

import pytest
from playwright.sync_api import expect


def test_sample(session_capabilities, base_url) -> None:
    try:
        # Load the PAge returned by the fixture
        page = session_capabilities
        print(page)
        # Navigate to the base url
        page.goto(base_url, timeout=0)

        # Add the first item to cart
        page.locator("[id=\"\\31 \"]").get_by_text("Add to cart").click()
        phone = page.locator("[id=\"\\31 \"]").locator(".shelf-item__title").all_inner_texts()
        print("Phone =>" + str(phone[0]))

        # Get the items from Cart
        qty = page.locator(".bag__quantity").all_inner_texts()
        print("Bag quantity => " + str(qty[0]))

        # Verify if there is a shopping cart
        expect(page.locator(".bag__quantity")).to_have_count(1)
        # Verify if there is only one item in the shopping cart
        expect(page.locator(".bag__quantity")).to_have_text("1")

        # Get the handle for cart item
        cart_item = page.locator(".shelf-item__details")

        # Verify if the cart has the right item
        #expect(cart_item.locator(".title")).to_have_text(phone)
        print("Cart item => "+cart_item.locator(".title").all_inner_texts()[0])
        assert cart_item.locator(".title").all_inner_texts()[0]==phone[0]
    except Exception as err:
        # Extract error message from Exception
        error = str(err).split("Call log:")[0].replace("\n", " but ").replace(":", "=>").replace("'", "")
        raise ValueError(error)

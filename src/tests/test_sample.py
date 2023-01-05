def test_sample(session_capabilities) -> None:
    page=session_capabilities
    print(page)
    page.goto("https://bstackdemo.com/", timeout=0)
    page.locator("[id=\"\\31 \"]").get_by_text("Add to cart").click()
    page.get_by_text("Checkout").click()
    page.locator("#username svg").click()
    page.locator("#react-select-2-option-0-3").click()
    page.locator(".css-tlfecz-indicatorContainer").click()
    page.locator("#react-select-3-option-0-0").click()
    page.get_by_role("button", name="Log In").click()
    page.get_by_label("First Name").click()
    page.get_by_label("First Name").fill("Venaktesh")
    page.get_by_label("First Name").press("Tab")
    page.get_by_label("Last Name").fill("Raghunathan")
    page.get_by_label("Last Name").press("Tab")
    page.get_by_label("Address").fill("200 John Olds Driver")
    page.get_by_label("Address").press("Tab")
    page.get_by_label("Address").click()
    page.get_by_label("Address").fill("200 John Olds Drive")
    page.get_by_label("Address").press("Tab")
    page.get_by_label("State/Province").fill("CT")
    page.get_by_label("State/Province").press("Tab")
    page.get_by_label("Postal Code").fill("06042")
    page.get_by_role("button", name="Submit").click()
    with page.expect_download() as download_info:
        page.get_by_text("Download order receipt").click()
    download = download_info.value

#with sync_playwright() as playwright:
#    run(playwright)

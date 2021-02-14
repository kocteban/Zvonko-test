from helper.page_helper import js_click


def press_show_all_widgets(browser, *widget):
	js_click(browser, *widget)

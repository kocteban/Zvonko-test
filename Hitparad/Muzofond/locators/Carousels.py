from selenium.webdriver.common.by import By


class CarouselsLocators:
    TOP_CAR_SHOW_ALL = (By.CSS_SELECTOR, "div.span.desktop > div > div.mobileShow div > a")
    MID_CAR_SHOW_ALL = (By.CSS_SELECTOR, "div.smallMargin > div:nth-child(1) > div.widgetHeader > a")
    BOT_CAR_SHOW_ALL = (By.CSS_SELECTOR, "div.smallMargin > div:nth-child(2) > div.widgetHeader > a")

    TOP_CAR_ARROW = (By.CSS_SELECTOR, "div.mobileShow button.slick-next.slick-arrow")
    MID_CAR_ARROW = (By.CSS_SELECTOR, "div.smallMargin div:nth-child(1) div.kineticRight")
    BOT_CAR_ARROW = (By.CSS_SELECTOR, "div.smallMargin > div:nth-child(2) div.kineticRight")

    TOP_CAR_BACK_ARROW = (By.CSS_SELECTOR, "div.mobileShow button.slick-prev.slick-arrow")
    MID_CAR_BACK_ARROW = (By.CSS_SELECTOR, "div.smallMargin > div:nth-child(1) div.kineticLeft")
    BOT_CAR_BACK_ARROW = (By.CSS_SELECTOR, "div.smallMargin > div:nth-child(2) div.kineticLeft")

    TOP_COLLECTION = (By.CSS_SELECTOR, "#slick-slide16")
    MID_COLLECTION = (By.CSS_SELECTOR, "div.smallMargin > div:nth-child(1) li:nth-child(5)")
    BOT_COLLECTION = (By.CSS_SELECTOR, "div.smallMargin > div:nth-child(2) li:nth-child(5)")

    TOP_COLLECTION_NAME = (By.CSS_SELECTOR, "#slick-slide16 span")
    MID_COLLECTION_NAME = (By.CSS_SELECTOR, "div.smallMargin > div:nth-child(1) li:nth-child(5) span")
    BOT_COLLECTION_NAME = (By.CSS_SELECTOR, "div.smallMargin > div:nth-child(2) li:nth-child(5) span")
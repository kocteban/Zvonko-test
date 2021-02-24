from selenium.webdriver.common.by import By


class WidgetsLocators:
    SLIDER_SHOW_ALL = (By.CSS_SELECTOR, ".box.widget.miniSlider .widgetLink")
    GENRES_SHOW_ALL = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(3) div > a")
    SINGERS_SHOW_ALL = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(4) div > a")
    NEWS_SHOW_ALL = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(5) div > a")
    RADIO_SHOW_ALL = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(6) div > a")
    OST_SHOW_ALL = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(8) div > a")
    DISCO_SHOW_ALL = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(9) div > a")
    NATIONAL_SHOW_ALL = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(10) div > a")

    SLIDER_COLLECTION_NAME = (By.CSS_SELECTOR, "#slick-slide00 > a > p")
    GENRES_COLLECTION_NAME = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(3) > div > ul > "
                                               "li:nth-child(6) > a > span")
    GENRES_COLLECTION = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(3) > div > ul > li:nth-child(6) "
                                          "> a > div > :nth-child(1) ")

    SINGERS_COLLECTION_NAME = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(4) > div > ul > li:nth-child(6) > a > span ")
    SINGERS_COLLECTION = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(4) > div > ul > li:nth-child(6) > a > div > :nth-child(1)")

    OST_COLLECTION_NAME = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(8) > div > ul > li:nth-child("
                                            "6) > a > span")
    OST_COLLECTION = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(8) > div > ul > li:nth-child(6) > a "
                                       "> div > :nth-child(1)")

    DISCO_COLLECTION_NAME = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(9) > div > ul > "
                                              "li:nth-child(6) > a > span")
    DISCO_COLLECTION = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(9) > div > ul > li:nth-child(6) > "
                                         "a > div > :nth-child(1)")

    NATIONAL_COLLECTION_NAME = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(10) > div > ul > "
                                                 "li:nth-child(6) > a > span")
    NATIONAL_COLLECTION = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(10) > div > ul > li:nth-child("
                                            "6) > a > div > :nth-child(1)")

    SEARCH_PLAY_STOP = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(7) ul > li:nth-child(3) ul > li")
    NEWS_PLAY_STOP = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(5) ul > li:nth-child(3) ul > li")

    NEWS_SINGERS_NAME = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(5) div.module-layout li:nth-child(2) div > h3 > a:nth-child(1) > span")
    NEWS_SINGERS = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(5) div.module-layout > ul > li:nth-child(2) div > h3 > a:nth-child(1)")

    SEARCH_SINGERS_NAME = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(7) div.module-layout li:nth-child(2) div > h3 > a:nth-child(1) > span")
    SEARCH_SINGER = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(7) div.module-layout > ul > li:nth-child(2) div > h3 > a:nth-child(1)")

    NEWS_SONG_NAME = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(5) div.module-layout li:nth-child(6) div > h3 > a:nth-child(3) > span")
    NEWS_SONG = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(5) div.module-layout li:nth-child(6) div > h3 > a:nth-child(3)")

    RADIO_PLAY = (By.CSS_SELECTOR, "div.span.desktop-sidebar > div:nth-child(6) li:nth-child(5) span.cover > img")

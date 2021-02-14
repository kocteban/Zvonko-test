from selenium.webdriver.common.by import By
from random import *


class CollectionLocators:
    COLLECTION_NAME = (By.CSS_SELECTOR, "div.span.desktop div ul li:nth-child(%s) a span" % str(randint(1, 20)))

    n = randint(1, 21)
    COLLECTION_SLIDER_HEADER = (By.CSS_SELECTOR, ".span.desktop>:nth-child(%s) .widgetLink h3" % n)
    COLLECTION_SLIDER_SHOW_ALL = (By.CSS_SELECTOR, "div.span.desktop > div:nth-child(%s) > div.widgetHeader > a.moreButton"
                                  % n)
    COLLECTION_SLIDER_ARROW = (By.CSS_SELECTOR, "div.span.desktop > div:nth-child(%s) div.kineticRight" % n)
    COLLECTION_SLIDER_CHECK = (By.CSS_SELECTOR, "div.span.desktop > div:nth-child(%s) div.kineticCenter.kinetic-active > ul > li:nth-child(6) > a"
                               % n)
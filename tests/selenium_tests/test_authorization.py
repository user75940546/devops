from .config import *
from .pages.etu_auth_page import EtuAuthPage
from .pages.trajectories_auth_page import TrajectoriesAuthPage


def test_authorization(browser, wait):
    trajectories_page = TrajectoriesAuthPage(browser, wait, TRAJECTORIES_URL)
    trajectories_page.open()
    trajectories_page.go_to_auth_by_ETU_ID()

    etu_auth_page = EtuAuthPage(browser, wait, browser.current_url)
    etu_auth_page.authorize(LOGIN, PASSWORD)
    etu_auth_page.accept_authorize_oauth()

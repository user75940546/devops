from .config import *
from .pages.documents_opop_page import DocumentsOpopPage
from .pages.etu_auth_page import EtuAuthPage
from .pages.opop_list_page import OpopListPage
from .pages.trajectories_auth_by_user_page import TrajectoriesAuthByUserPage
from .pages.trajectories_auth_page import TrajectoriesAuthPage


def test_opop(browser, wait):
    trajectories_page = TrajectoriesAuthPage(browser, wait, TRAJECTORIES_URL)
    trajectories_page.open()
    trajectories_page.accept_cookies()
    trajectories_page.go_to_auth_by_ETU_ID()

    etu_auth_page = EtuAuthPage(browser, wait, browser.current_url)
    etu_auth_page.authorize(LOGIN, PASSWORD)
    etu_auth_page.accept_authorize_oauth()

    auth_by_user_page = TrajectoriesAuthByUserPage(browser, wait, AUTH_BY_USER_URL)
    auth_by_user_page.open()
    auth_by_user_page.authorize_by_user(ADMIN_ID)

    opop_list_page = OpopListPage(browser, wait, OPOP_LIST_URL)
    opop_list_page.open()

    # Создание нового документа
    # document_id = opop_list_page.add_document(
    #     '01.04.02 Прикладная математика и информатика  - ФКТИ',
    #     '01.04.02 Прикладная математика и информатика (01.04.02_23_567с1.plx, 2024-2025) - каф.ВТ'
    # )
    # documents_opop_page = DocumentsOpopPage(browser, wait, DOCUMENT_OPOP(document_id))

    # (1231 документ - черновик)
    documents_opop_page = DocumentsOpopPage(browser, wait, DOCUMENT_OPOP(1231))
    documents_opop_page.open()
    documents_opop_page.fill_document()
    documents_opop_page.is_document_saved()

import os

WAIT = 10
ADMIN_ID = 1305
TRAJECTORIES_URL = "https://test.digital.etu.ru/trajectories/auth"
AUTH_BY_USER_URL = "https://test.digital.etu.ru/trajectories/admin/fake"
OPOP_LIST_URL = "https://test.digital.etu.ru/trajectories/documents/opop-list"
LOGIN = (os.environ.get("ETU_ID_LOGIN"),)
PASSWORD = os.environ.get("ETU_ID_PASSWORD")
DOCUMENT_OPOP = (
    lambda id: f"https://test.digital.etu.ru/trajectories/documents/opop/{id}"
)

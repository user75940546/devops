import os

import requests

BASE_URL = "http://app:5000"
FILES_FOLDER = os.path.join(os.path.dirname(__file__), "files")
FILENAME = "file.png"


def test_upload_file(
    expected_status=200,
    files_folder=FILES_FOLDER,
    filename=FILENAME,
    content_type="image/png",
):
    file_path = os.path.join(files_folder, filename)

    with open(file_path, "rb") as f:
        files = {"file": (filename, f, content_type)}

        try:
            response = requests.post(f"{BASE_URL}/upload", files=files)
            assert (
                response.status_code == expected_status
            ), f"Expected status: {expected_status}, received: {response.status_code}"

            if expected_status == 200:
                assert filename in response.json()["files"], f"{filename} not found"

        except requests.exceptions.RequestException as e:
            assert False, f"POST error: {filename}. {e}"

    try:
        response = requests.get(f"{BASE_URL}/download/{filename}")
        assert (
            response.status_code == 200
        ), f"Expected status: {expected_status}, received: {response.status_code}"
        assert response.content == open(file_path, "rb").read(), "File mismatch"
    except requests.exceptions.RequestException as e:
        assert False, f"GET error: {filename}. {e}"

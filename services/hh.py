from dotenv import load_dotenv
import os
import requests

from settings import HeadHunterSettings

BASE_URL = "https://api.hh.ru/"


class HeadHunter:
    def __init__(self):
        self.settings = HeadHunterSettings()

    def found_vacancy(self, vacancy_id: str):
        URL = BASE_URL + "/vacancies/" + vacancy_id
        headers = {
            "User-Agent": "AutoFeedback/1.0 (zalimpshigotizhev@yandex.ru)",
            "HH-User-Agent": "AutoFeedback/1.0 (zalimpshigotizhev@yandex.ru)"
        }
        response = requests.get(URL, headers=headers)
        return response.json()

    def search_vacancies(
            self,
            page: int = 0,
            per_page: int = 10,
            text = None,
            period = None
    ):
        URL = BASE_URL + "vacancies"
        data = {
            "text": text,
            "page": page,
            "per_page": per_page,
            "period": period
        }
        headers = {
            "User-Agent": "AutoFeedback/1.0 (zalimpshigotizhev@yandex.ru)",
            "HH-User-Agent": "AutoFeedback/1.0 (zalimpshigotizhev@yandex.ru)"
        }

        response = requests.get(URL, data=data, headers=headers)
        return response.json()

    def get_link_for_auth(self):
        return (f"https://hh.ru/oauth/authorize?client_id={self.settings.client_id}"
                f"&response_type=code")

    def list_resumes(self):
        URL = BASE_URL + "/resumes/mine"
        headers = {
            "User-Agent": "AutoFeedback/1.0 (zalimpshigotizhev@yandex.ru)",
            "HH-User-Agent": "AutoFeedback/1.0 (zalimpshigotizhev@yandex.ru)"
        }
        response = requests.get(URL, headers=headers)
        return response.json()

    def authorize(
            self,
            client_secret: str,
            code: str,
            grant_type: str,
            redirect_uri: str = None
    ) -> dict:
        URL = BASE_URL + "/token"

        data = {
            "client_id": self.settings.client_id,
            "client_secret": client_secret,
            "code": code,
            "grant_type": grant_type,
            "redirect_uri": redirect_uri
        }
        headers = {
            "User-Agent": "AutoFeedback/1.0 (zalimpshigotizhev@yandex.ru)",
            "HH-User-Agent": "AutoFeedback/1.0 (zalimpshigotizhev@yandex.ru)"
        }

        response = requests.post(url=URL, data=data, headers=headers)
        return response.json()

    def me(self, access_token: str) -> dict:
        URL = BASE_URL + "/me"

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "User-Agent": "AutoFeedback/1.0 (zalimpshigotizhev@yandex.ru)",
            "HH-User-Agent": "AutoFeedback/1.0 (zalimpshigotizhev@yandex.ru)"

        }

        response = requests.get(URL, headers=headers)

        return response.json()

    def my_resumes(self, access_token: str) -> dict:
        URL = BASE_URL + "/resumes/mine"

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "User-Agent": "AutoFeedback/1.0 (zalimpshigotizhev@yandex.ru)",
            "HH-User-Agent": "AutoFeedback/1.0 (zalimpshigotizhev@yandex.ru)"
        }

        response = requests.get(URL, headers=headers)

        return response.json()

    def negotiations(
            self,
            access_token: str,
            resume_id: str,
            vacancy_id: str,
            message: str = None,
    ):
        URL = BASE_URL + "/negotiations"
        data = {
            "message": message,
            "resume_id": resume_id,
            "vacancy_id": vacancy_id,
        }
        headers = {
            "Authorization": f"Bearer {access_token}",
            "User-Agent": "AutoFeedback/1.0 (zalimpshigotizhev@yandex.ru)",
            "HH-User-Agent": "AutoFeedback/1.0 (zalimpshigotizhev@yandex.ru)"
        }

        response = requests.post(URL, data=data, headers=headers)
        if int(response.status_code) != 201:
            return response.json()


    def get_similar_vacancies(
            self, resume_id: str,
            text: str,
            page: int = 0, per_page: int = 10,
    ) -> list:
        URL = BASE_URL + "/resumes" + f"/{resume_id}" + "/similar_vacancies"
        data = {
            "text": text,
            "page": page,
            "per_page": per_page
        }
        headers = {
            "User-Agent": "AutoFeedback/1.0 (zalimpshigotizhev@yandex.ru)",
            "HH-User-Agent": "AutoFeedback/1.0 (zalimpshigotizhev@yandex.ru)"
        }

        response = requests.get(URL, data=data, headers=headers)
        return response.json()
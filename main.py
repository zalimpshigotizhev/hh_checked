import time

from repo.json_db import JsonDB
from services.hh import HeadHunter
from services.tg_api import TelegramAPI


if __name__ == '__main__':
    tg = TelegramAPI()
    hh = HeadHunter()
    db = JsonDB()

    text_for_search = "'Python' AND ('FastAPI' OR 'Django')"
    while True:
        time.sleep(60)
        vacs = hh.search_vacancies(per_page=100, text=text_for_search, period=1)
        vac = vacs.get("items")[0]
        print(f"Найдено {vacs.get('found')}")

        ids_vacs = [vac.get("id") for vac in vacs.get("items")]
        ids_checked = db.get_checked_list()

        ids_res = set(ids_vacs) - set(ids_checked)

        if ids_res:
            for id_vac in ids_res:
                vac = hh.found_vacancy(id_vac)
                tg.send_message(
                    f"Новая вакансия !!!\n*{vac.get('name')}*\n{vac.get('alternate_url')}"
                )
                db.add_checked(vac.get("id"))

import requests
from multiprocessing import Pool
import json
import codecs



def api_t(url_list):
    payload = {"api": "risk",
               "key": "You_api_KEY",
               "tbclass": "div.post__wrapper",
               "url": url_list}
    
    r = requests.post("https://turgenev.ashmanov.com/", data=payload)
    
    dump = r.json()
    
    try:
        risk_num = [i["sum"] for i in dump["details"]]
        return {str(url_list):[str(dump["level"]),str(dump["risk"])]}
    except Exception as error:
        return error


def pars_url_list():
    with open(r"urls_list.txt",  encoding="utf-8") as file:
        f = file.read().splitlines()
        return f


if __name__ == '__main__':
    with Pool(5) as p:
        list_result = p.map(api_t, pars_url_list())
        result ={}
        for i in list_result:
            if type(i) == dict: 
                result.update(i)
        with codecs.open(r"result.json", 'w', encoding="utf-8") as file:
                json.dump(result, file, ensure_ascii=False)
                print('Готово')


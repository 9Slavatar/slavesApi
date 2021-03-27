import requests
import json

# Vars
buy_url = "https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/buySlave" # URL 4 buy
job_url = "https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/jobSlave" # URL 4 job
user_url = "https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/user?id=" # URL 4 user
fetter_url = "https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/buyFetter" # URL 4 fetter
slaves_url = "https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/slaveList?id=" # URL 4 slaves

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": None,
    "origin": "https://prod-app7794757-6f6bf9481ca4.pages-ac.vk-apps.com",
    "referer": "https://prod-app7794757-6f6bf9481ca4.pages-ac.vk-apps.com/",
    "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    "content-type": "application/json",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}



# Slave class & function
class Slave:
    def __init__(self, id = 1, json = None):
        if json == None:
            r = requests.get(user_url + str(id), headers=headers)
            if r.status_code == 200:
                json = r.json()
            else:
                print(f"Oops! Error code {r.status_code}, {r.text}")
                return

        self.item_type = json["item_type"]
        self.id = json["id"]
        self.job = json["job"]
        self.master_id = json["master_id"]
        self.profit_per_min = json["profit_per_min"]
        self.fetter_to = json["fetter_to"]
        self.fetter_price = json["fetter_price"]
        self.sale_price = json["sale_price"]
        self.chicken_mark = json["chicken_mark"]
        self.price = json["price"]
        self.balance = json["balance"]
        self.duel_count = json["duel_count"]
        self.duel_win = json["duel_win"]
        self.duel_reject = json["duel_reject"]
        self.chicken_mark_clean = json["chicken_mark_clean"]
        self.slaves_count = json["slaves_count"]
        self.rating_position = json["rating_position"]
        self.slaves_profit_per_min = json["slaves_profit_per_min"]
        self.was_in_app = json["was_in_app"]
        self.fetter_hour = json["fetter_hour"]
        self.steps_at = json["steps_at"]
        self.jump_at = json["jump_at"]
        self.deleted_at = json["deleted_at"]

        print(f"Initilization slave with {self.id}")

    def buy(self):
        requests.post(buy_url, headers=headers, data=json.dumps({"slave_id": self.id}))

    def setJob(self, job="github.com/SlavatarGit"):
        requests.post(job_url, headers=headers, data=json.dumps({"slave_id": self.id,"name": str(job)}))

    def buyFetter(self):
        requests.post(fetter_url, headers=headers, data=json.dumps({"slave_id": self.id}))

    def getSlaves(self):
        r = requests.get(slaves_url + str(self.id), headers=headers)
        if r.status_code == 200:
            return r.json()
        else:
            return None


# Example
import random
import time
if __name__ == "__main__":
    while True:
        """ Покупает рандомных рабов от 30к и до 150к
        slave = Slave(random.randint(1, 646516091))
        try:
            if slave.price > 30000 and slave.price < 150000 and not slave.fetter_to:
                print(f"Finded slave {slave.id} cost {slave.price}")
                slave.buy()
                slave.setJob()
                #slave.buyFetter()
                    
            else:
                print(f"Slave {slave.id} cost {slave.price}; is fetter: {slave.fetter_to}, aborted")
        except:
            continue
        """

        """ Рейдит одного пользователя, скупая всех рабов от 30к до 300к
        dungeonmaster = Slave(173217382)
        dungeonmaster_slaves = dungeonmaster.getSlaves()
        for i in dungeonmaster_slaves["slaves"]:
            slave = Slave(json=i)
            if slave.price > 30000 and slave.price < 300000 and not slave.fetter_to:
                print(f"Finded slave {slave.id} cost {slave.price}")
                slave.buy()
                slave.setJob()
                time.sleep(2.5)
            else:
                print(f"Slave {slave.id} cost {slave.price}; is fetter: {slave.fetter_to}, aborted")
        """
        
        """Устанавливает работы для всех рабов в вашем владении
        dungeonmaster = Slave(411715303) # Твой айди тут
        dungeonmaster_slave = dungeonmaster.getSlaves()
        for i in dungeonmaster_slave["slaves"]:
            slave = Slave(json=i)
            slave.setJob("🦾 github.com/SlavatarGit")
            if not slave.fetter_to: 
                slave.buyFetter()

            time.sleep(2.5)
        """

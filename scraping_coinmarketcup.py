from datetime import datetime
from time import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

from clustering_coinmarket import clustering

csvFilePath = "data/market_crypto_data_test.csv"

crypto_link = []
crypto_name = []
crypto_image = []
crypto_company = []
crypto_price = []
crypto_price_change24h = []
high24h = []
low24h = []
volume24h = []
volume_in_market_cap = []
market_dominance = []
market_rank = []
market_cap = []
fully_diluted_market_cap = []
yesterday_low = []
yesterday_high = []
yesterday_open = []
yesterday_close = []
yesterday_change = []
yesterday_volume = []
_7d_low = []
_7d_high = []
_30d_low = []
_30d_high = []
_30d_low = []
_30d_high = []
_90d_low = []
_90d_high = []
_52w_low = []
_52w_high = []
_all_time_low = []
_all_time_high = []
_all_time_low_date = []
_all_time_high_date = []
circulatingSupply = []
maxSupplyValue = []
totalSupplyValue = []
date = []

scroll = 2000
x = 10

nbre_cryptos = 5


def lancerScraping(nbre_pages = 2):

    driver = webdriver.Chrome()
    driver.maximize_window()

    for page in range(nbre_pages) :

        driver.get(f"https://coinmarketcap.com/coins/?page={page+1}")

        driver.execute_script("window.scrollTo(0,1000)")    

        table =  driver.find_elements_by_xpath("//table[@class='h7vnx2-2 czTsgW cmc-table  ']/tbody/tr")

        tmp = driver.find_element_by_xpath("//table[@class='h7vnx2-2 czTsgW cmc-table  ']/tbody")

        print("\ntotal = " + str(len(table)))

        for i in range(len(table)):

            driver.execute_script("window.scrollTo(0,"+ str(1000 + 80*(i+1)) +")")

            crypto_link0 = tmp.find_element_by_xpath(f"tr[{i+1}]/td[3]/div/a").get_attribute("href")
            crypto_link.append(crypto_link0)

            crypto_name0 = tmp.find_element_by_xpath(f"tr[{i+1}]/td[3]/div/a/div/div/p").get_attribute("innerHTML").split("<")[0]

            crypto_name.append(crypto_name0)

            crypto_company0 = tmp.find_element_by_xpath(f"tr[{i+1}]/td[3]/div/a/div/div/div/p").get_attribute("innerHTML")

            crypto_company.append(crypto_company0)

            crypto_company0 = tmp.find_element_by_xpath(f"tr[{i+1}]/td[2]/p").get_attribute("innerHTML")

            crypto_company.append(crypto_company0)

            # print("\nlink = " +crypto_link0)

    # print("\ncryptos length = " + str(len(crypto_link)))
    # print(crypto_link)

    for cl in crypto_link[0:nbre_cryptos] :

        try :
            driver.get(cl)

        except :
            print(cl + " introuvable")
        
        try :
            crypto_image0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/img").get_attribute("src")
        except:
            crypto_image0 = "https://s2.coinmarketcap.com/static/img/coins/64x64/1.png"
        crypto_image.append(crypto_image0)
        print(crypto_image)
        
        driver.execute_script("window.scrollTo(0,"+str(scroll)+")")
        
        try :
            crypto_price0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[1]/table/tbody/tr[1]/td").get_attribute("innerHTML")
        except :
            try :
                crypto_price0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[1]/table/tbody/tr[1]/td").get_attribute("innerHTML")
            except :
                try :
                    crypto_price0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[1]/table/tbody/tr[1]/td").get_attribute("innerHTML")
                except :
                    crypto_price0 = "NaN"
        crypto_price.append(crypto_price0)        
        print(crypto_price)
        try:    
            crypto_price_change24h0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[1]/table/tbody/tr[2]/td/span").get_attribute("innerHTML")
        except:
            try:
                crypto_price_change24h0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[1]/table/tbody/tr[2]/td/span").get_attribute("innerHTML")
            except:
                try:
                    crypto_price_change24h0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[1]/table/tbody/tr[2]/td/span").get_attribute("innerHTML").split("<!")[0]
                except:
                    crypto_price_change24h0 = "NaN"
        crypto_price_change24h.append(crypto_price_change24h0)
        print(crypto_price_change24h)
        try:
            low24h0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[1]/table/tbody/tr[3]/td/div[1]").get_attribute("innerHTML").split("<!")[0]
        except:
            try:
                low24h0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[1]/table/tbody/tr[3]/td/div[1]").get_attribute("innerHTML").split("<!")[0]
            except:
                try:
                    low24h0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[1]/table/tbody/tr[3]/td/div[1]").get_attribute("innerHTML").split("<!")[0]
                except:
                    low24h0 = "NaN" 
        low24h.append(low24h0)
        print(low24h)
        try:
            high24h0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[1]/table/tbody/tr[3]/td/div[2]").get_attribute("innerHTML")
        except:
            try:
                high24h0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[1]/table/tbody/tr[3]/td/div[2]").get_attribute("innerHTML")
            except:
                try:
                    high24h0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[1]/table/tbody/tr[3]/td/div[2]").get_attribute("innerHTML")
                except:
                    high24h0 = "NaN"
        high24h.append(high24h0)
        print(high24h)
        try:
            volume24h0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[1]/table/tbody/tr[4]/td/span").get_attribute("innerHTML")
        except:
            try:
                volume24h0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[1]/table/tbody/tr[4]/td/span").get_attribute("innerHTML")
            except:
                try:
                    volume24h0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[1]/table/tbody/tr[4]/td/span").get_attribute("innerHTML")
                except:
                    volume24h0 = "NaN"
        volume24h.append(volume24h0)
        print(volume24h)
        try:
            volume_in_market_cap0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[1]/table/tbody/tr[5]/td").get_attribute("innerHTML")
        except:
            try:
                volume_in_market_cap0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[1]/table/tbody/tr[5]/td").get_attribute("innerHTML")
            except:
                try:
                    volume_in_market_cap0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[1]/table/tbody/tr[5]/td").get_attribute("innerHTML")
                except:
                    volume_in_market_cap0 = "NaN"
        volume_in_market_cap.append(volume_in_market_cap0)
        print(volume_in_market_cap)
        try:
            market_dominance0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[1]/table/tbody/tr[6]/td/span").get_attribute("innerHTML").split("<!")[0] + "%"
        except:
            try:
                market_dominance0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[1]/table/tbody/tr[6]/td/span").get_attribute("innerHTML").split("<!")[0] + "%"
            except:
                try:
                    market_dominance0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[1]/table/tbody/tr[6]/td/span").get_attribute("innerHTML").split("<!")[0] + "%"
                except:
                    market_dominance0 = "NaN"
        market_dominance.append(market_dominance0)
        print(market_dominance)
        try:   
            market_rank0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[1]/table/tbody/tr[7]/td").get_attribute("innerHTML").split("#")[1]
        except:
            try:
                market_rank0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[1]/table/tbody/tr[7]/td").get_attribute("innerHTML").split("#")[1]
            except:
                try:
                    market_rank0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[1]/table/tbody/tr[7]/td").get_attribute("innerHTML").split("#")[1]
                except:
                    market_rank0 = "NaN"
        market_rank.append(market_rank0)
        print(market_rank)
        try:
            market_cap0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[2]/table/tbody/tr[1]/td/span").get_attribute("innerHTML")
        except:
            try:
                market_cap0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[2]/table/tbody/tr[1]/td/span").get_attribute("innerHTML")
            except:    
                try:
                    market_cap0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[2]/table/tbody/tr[1]/td/span").get_attribute("innerHTML")
                except:    
                    market_cap0 = "NaN"
        market_cap.append(market_cap0)
        print(market_cap)
        try:
            fully_diluted_market_cap0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[2]/table/tbody/tr[2]/td/span").get_attribute("innerHTML")
        except:
            try:
                fully_diluted_market_cap0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[2]/table/tbody/tr[2]/td/span").get_attribute("innerHTML")
            except:
                try:
                    fully_diluted_market_cap0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[2]/table/tbody/tr[2]/td/span").get_attribute("innerHTML")
                except:
                    fully_diluted_market_cap0 = "NaN"
        fully_diluted_market_cap.append(fully_diluted_market_cap0)
        print(fully_diluted_market_cap)

        try:
            driver.execute_script("window.scrollTo(0,"+str(scroll + x*10)+")")
            btn = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/button")
            btn.click()
        except:
            try:
                driver.execute_script("window.scrollTo(0,"+str(scroll + x*20)+")")
                btn = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/button")
                btn.click()
            except:
                try:
                    driver.execute_script("window.scrollTo(0,"+str(scroll + x*10)+")")
                    btn = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/button")
                    btn.click()
                except:
                    print("btn introuvable")

        try:
            yesterday_low0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[3]/div[1]/table/tbody/tr[1]/td/div[1]").get_attribute("innerHTML").split("<")[0]
        except:
            try:
                yesterday_low0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[3]/div[1]/table/tbody/tr[1]/td/div[1]").get_attribute("innerHTML").split("<")[0]
            except:
                try:
                    yesterday_low0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[3]/div[1]/table/tbody/tr[1]/td/div[1]").get_attribute("innerHTML").split("<")[0]
                except:
                    yesterday_low0 = "NaN"
        yesterday_low.append(yesterday_low0)
        print(yesterday_low)

        try:
            yesterday_high0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[3]/div[1]/table/tbody/tr[1]/td/div[2]").get_attribute("innerHTML").split("<")[0]
        except:
            try:
                yesterday_high0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[3]/div[1]/table/tbody/tr[1]/td/div[2]").get_attribute("innerHTML").split("<")[0]
            except:
                try:
                    yesterday_high0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[3]/div[1]/table/tbody/tr[1]/td/div[2]").get_attribute("innerHTML").split("<")[0]
                except:
                    yesterday_high0 = "NaN"
        yesterday_high.append(yesterday_high0)
        print(yesterday_high)

        try:
            yesterday_open0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[3]/div[1]/table/tbody/tr[2]/td/div[1]").get_attribute("innerHTML").split("<")[0]
        except:
            try:
                yesterday_open0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[3]/div[1]/table/tbody/tr[2]/td/div[1]").get_attribute("innerHTML").split("<")[0]
            except:
                try:
                    yesterday_open0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[3]/div[1]/table/tbody/tr[2]/td/div[1]").get_attribute("innerHTML").split("<")[0]
                except:
                    yesterday_open0 = "NaN"
        yesterday_open.append(yesterday_open0)
        print(yesterday_open)


        try:
            yesterday_close0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[3]/div[1]/table/tbody/tr[2]/td/div[2]").get_attribute("innerHTML")
        except:
            try:
                yesterday_close0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[3]/div[1]/table/tbody/tr[2]/td/div[2]").get_attribute("innerHTML")
            except:
                try:
                    yesterday_close0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[3]/div[1]/table/tbody/tr[2]/td/div[2]").get_attribute("innerHTML")
                except:
                    yesterday_close0 = "NaN"
        yesterday_close.append(yesterday_close0)
        print(yesterday_close)

        try:
            yesterday_change0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[3]/div[1]/table/tbody/tr[3]/td/div/p").get_attribute("innerHTML").split("svg>")[1]
        except:
            try:
                yesterday_change0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[3]/div[1]/table/tbody/tr[3]/td/div/p").get_attribute("innerHTML").split("svg>")[1]
            except:
                try:
                    yesterday_change0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[3]/div[1]/table/tbody/tr[3]/td/div/p").get_attribute("innerHTML").split("svg>")[1]
                except:
                    yesterday_change0 = "NaN"
        yesterday_change.append(yesterday_change0)
        print(yesterday_change)

        try:
            yesterday_volume0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[3]/div[1]/table/tbody/tr[4]/td").get_attribute("innerHTML")
        except:
            try:
                yesterday_volume0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[3]/div[1]/table/tbody/tr[4]/td").get_attribute("innerHTML")
            except:
                try:
                    yesterday_volume0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[3]/div[1]/table/tbody/tr[4]/td").get_attribute("innerHTML")
                except:
                    yesterday_volume0 = "NaN"
        yesterday_volume.append(yesterday_volume0)
        print(yesterday_volume)

        try:
            _7d_low0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[3]/div[2]/table/tbody/tr[1]/td/div[1]").get_attribute("innerHTML").split("<!")[0]
        except:
            try:
                _7d_low0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[3]/div[2]/table/tbody/tr[1]/td/div[1]").get_attribute("innerHTML").split("<!")[0]
            except:    
                try:
                    _7d_low0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[3]/div[2]/table/tbody/tr[1]/td/div[1]").get_attribute("innerHTML").split("<!")[0]
                except:    
                    _7d_low0 = "NaN"
        _7d_low.append(_7d_low0)
        print(_7d_low)
        try:
            _7d_high0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[3]/div[2]/table/tbody/tr[1]/td/div[2]").get_attribute("innerHTML")
        except:
            try:
                _7d_high0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[3]/div[2]/table/tbody/tr[1]/td/div[2]").get_attribute("innerHTML")
            except:
                try:
                    _7d_high0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[3]/div[2]/table/tbody/tr[1]/td/div[2]").get_attribute("innerHTML")
                except:
                    _7d_high0 = "NaN"
        _7d_high.append(_7d_high0)
        print(_7d_high)
        try:
            _30d_low0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[3]/div[2]/table/tbody/tr[1]/td/div[1]").get_attribute("innerHTML").split("<!")[0]
        except:
            try:
                _30d_low0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[3]/div[2]/table/tbody/tr[1]/td/div[1]").get_attribute("innerHTML").split("<!")[0]
            except:    
                try:
                    _30d_low0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[3]/div[2]/table/tbody/tr[2]/td/div[1]").get_attribute("innerHTML").split("<!")[0]
                except:    
                    _30d_low0 = "NaN"
        _30d_low.append(_30d_low0)
        print(_30d_low)
        try:
            _30d_high0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[3]/div[2]/table/tbody/tr[1]/td/div[2]").get_attribute("innerHTML")
        except:
            try:
                _30d_high0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[3]/div[2]/table/tbody/tr[1]/td/div[2]").get_attribute("innerHTML")
            except:
                try:
                    _30d_high0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[3]/div[2]/table/tbody/tr[2]/td/div[2]").get_attribute("innerHTML")
                except:
                    _30d_high0 = "NaN"
        _30d_high.append(_30d_high0)
        print(_30d_high)
        try:
            _90d_low0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[3]/div[2]/table/tbody/tr[3]/td/div[1]").get_attribute("innerHTML").split("<!")[0]
        except:
            try:
                _90d_low0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[3]/div[2]/table/tbody/tr[3]/td/div[1]").get_attribute("innerHTML").split("<!")[0]
            except:
                try:
                    _90d_low0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[3]/div[2]/table/tbody/tr[3]/td/div[1]").get_attribute("innerHTML").split("<!")[0]
                except:
                    _90d_low0 = "NaN"
        _90d_low.append(_90d_low0)
        print(_90d_low)
        try:
            _90d_high0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[3]/div[2]/table/tbody/tr[3]/td/div[2]").get_attribute("innerHTML")
        except:
            try:
                _90d_high0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[3]/div[2]/table/tbody/tr[3]/td/div[2]").get_attribute("innerHTML")
            except:
                try:
                    _90d_high0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[3]/div[2]/table/tbody/tr[3]/td/div[2]").get_attribute("innerHTML")
                except:
                    _90d_high0 = "NaN"
        _90d_high.append(_90d_high0)
        print(_90d_high)
        try:
            _52w_low0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[3]/div[2]/table/tbody/tr[4]/td/div[1]").get_attribute("innerHTML").split("<!")[0]
        except:
            try:
                _52w_low0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[3]/div[2]/table/tbody/tr[4]/td/div[1]").get_attribute("innerHTML").split("<!")[0]
            except:
                try:
                    _52w_low0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[3]/div[2]/table/tbody/tr[4]/td/div[1]").get_attribute("innerHTML").split("<!")[0]
                except:
                    _52w_low0 = "NaN"
        _52w_low.append(_52w_low0)
        print(_52w_low)
        try:
            _52w_high0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[3]/div[2]/table/tbody/tr[4]/td/div[2]").get_attribute("innerHTML")
        except:
            try:
                _52w_high0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[3]/div[2]/table/tbody/tr[4]/td/div[2]").get_attribute("innerHTML")
            except:    
                try:
                    _52w_high0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[3]/div[2]/table/tbody/tr[4]/td/div[2]").get_attribute("innerHTML")
                except:    
                    _52w_high0 = "NaN"
        _52w_high.append(_52w_high0)
        print(_52w_high)
        try:
            _all_time_high0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[3]/div[2]/table/tbody/tr[5]/td/span").get_attribute("innerHTML")
        except:
            try:
                _all_time_high0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[3]/div[2]/table/tbody/tr[5]/td/span").get_attribute("innerHTML")
            except:
                try:
                    _all_time_high0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[3]/div[2]/table/tbody/tr[5]/td/span").get_attribute("innerHTML")
                except:
                    _all_time_high0 = "NaN"
        _all_time_high.append(_all_time_high0)
        print(_all_time_high)
        try:
            _all_time_high_date0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[3]/div[2]/table/tbody/tr[5]/th/small").get_attribute("innerHTML").split("<!")[0]
        except:
            try:
                _all_time_high_date0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[3]/div[2]/table/tbody/tr[5]/th/small").get_attribute("innerHTML").split("<!")[0]
            except:
                try:
                    _all_time_high_date0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[3]/div[2]/table/tbody/tr[5]/th/small").get_attribute("innerHTML").split("<!")[0]
                except:
                    _all_time_high_date0 = "NaN"
        _all_time_high_date.append(_all_time_high_date0)
        print(_all_time_high_date)
        try:
            _all_time_low0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[3]/div[2]/table/tbody/tr[6]/td/span").get_attribute("innerHTML")
        except:
            try:
                _all_time_low0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[3]/div[2]/table/tbody/tr[6]/td/span").get_attribute("innerHTML")
            except:
                try:
                    _all_time_low0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[3]/div[2]/table/tbody/tr[6]/td/span").get_attribute("innerHTML")
                except:
                    _all_time_low0 = "NaN"
        _all_time_low.append(_all_time_low0)
        print(_all_time_low)
        try:
            _all_time_low_date0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[3]/div[2]/table/tbody/tr[6]/th/small").get_attribute("innerHTML").split("<!")[0]
        except:
            try:
                _all_time_low_date0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[3]/div[2]/table/tbody/tr[6]/th/small").get_attribute("innerHTML").split("<!")[0]
            except:
                try:
                    _all_time_low_date0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[3]/div[2]/table/tbody/tr[6]/th/small").get_attribute("innerHTML").split("<!")[0]
                except:
                    _all_time_low_date0 = "NaN"
        _all_time_low_date.append(_all_time_low_date0)
        print(_all_time_low_date)
        try:
            circulatingSupply0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[3]/div[3]/table/tbody/tr[1]/td").get_attribute("innerHTML").split(" ")[0]
        except:
            try:
                circulatingSupply0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[3]/div[3]/table/tbody/tr[1]/td").get_attribute("innerHTML").split(" ")[0]
            except:
                try:
                    circulatingSupply0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[3]/div[3]/table/tbody/tr[1]/td").get_attribute("innerHTML").split(" ")[0]
                except:
                    circulatingSupply0 = "NaN"
        circulatingSupply.append(circulatingSupply0)
        print(circulatingSupply)
        try:
            totalSupplyValue0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[3]/div[3]/table/tbody/tr[2]/td").get_attribute("innerHTML").split(" ")[0]
        except:
            try:
                totalSupplyValue0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[3]/div[3]/table/tbody/tr[2]/td").get_attribute("innerHTML").split(" ")[0]
            except:
                try:
                    totalSupplyValue0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[3]/div[3]/table/tbody/tr[2]/td").get_attribute("innerHTML").split(" ")[0]
                except:
                    totalSupplyValue0 = "NaN"
        totalSupplyValue.append(totalSupplyValue0)
        print(totalSupplyValue)
        try:
            maxSupplyValue0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[3]/div/div[3]/div[3]/table/tbody/tr[3]/td").get_attribute("innerHTML").split(" ")[0]
        except:
            try:
                maxSupplyValue0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div/div[3]/div[3]/table/tbody/tr[3]/td").get_attribute("innerHTML").split(" ")[0]
            except:
                try:
                    maxSupplyValue0 = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/div[3]/div[3]/table/tbody/tr[3]/td").get_attribute("innerHTML").split(" ")[0]
                except:
                    maxSupplyValue0 = "NaN"
        maxSupplyValue.append(maxSupplyValue0)
        print(maxSupplyValue)  
        
        date.append(datetime.today())


    print("\n++++++++++++++++++++++++++++++++++++++++++++++++++ Data ++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\nnbre_total = " + str(len(crypto_link)))
    print(len(crypto_link))
    print(len(crypto_name))
    print(len(crypto_image))
    print(len(crypto_company))
    print(len(crypto_price))
    print(len(crypto_price_change24h))
    print(len(high24h))
    print(len(low24h))
    print(len(volume24h))
    print(len(volume_in_market_cap))
    print(len(market_dominance))
    print(len(market_rank))
    print(len(market_cap))
    print(len(fully_diluted_market_cap))
    print(len(yesterday_low))
    print(len(yesterday_high))
    print(len(yesterday_open))
    print(len(yesterday_close))
    print(len(yesterday_change))
    print(len(yesterday_volume))
    print(len(_7d_low))
    print(len(_7d_high))
    print(len(_30d_low))
    print(len(_30d_high))
    print(len(_30d_low))
    print(len(_30d_high))
    print(len(_90d_low))
    print(len(_90d_high))
    print(len(_52w_low))
    print(len(_52w_high))
    print(len(_all_time_low))
    print(len(_all_time_high))
    print(len(_all_time_low_date))
    print(len(_all_time_high_date))
    print(len(circulatingSupply))
    print(len(maxSupplyValue))
    print(len(totalSupplyValue))
    print(len(date))
    print("\n")


    df = pd.DataFrame(list(zip(market_rank,crypto_image,crypto_name,crypto_company,market_cap,fully_diluted_market_cap,
    yesterday_low,yesterday_high,yesterday_open,yesterday_close,yesterday_change,yesterday_volume,
    crypto_price,volume24h,volume_in_market_cap,market_dominance,circulatingSupply,maxSupplyValue,totalSupplyValue,
    crypto_price_change24h,high24h,low24h,_7d_high,_7d_low,_30d_high,_30d_low,_90d_high,_90d_low,_52w_high,_52w_low,
    _all_time_high,_all_time_low,_all_time_high_date,_all_time_low_date,date)),index=None,
    columns =['rank','image','name','company','marketCap','fullyDilutedMarketCap','yesterday_low','yesterday_high',
    'yesterday_open','yesterday_close','yesterday_change','yesterday_volume','price','volume_24h',
    'volume24hInMarketCap','dominance','circulatingSupply','maxSupplyValue','totalSupplyValue','price_change_24h',
    'high_24h','low_24h','high_7d','low_7d','high_30d','low_30d','high_90d','low_90d','high_52w','low_52w',
    'high_all_time','low_all_time','high_all_time_date','low_all_time_date','date'])

    #remove na
    # df.dropna(inplace=True)
    # df.drop('Unnamed: 0', axis = 1, inplace=True) 
    
    print("total = " + str(len(df)))
    print(df.head())

    df.to_csv(csvFilePath)

    clustering(csvFilePath)



# start_time = time()   
# lancerScraping()
# print("\n\ntime of scraping = " + str((time() - start_time)/60.0))




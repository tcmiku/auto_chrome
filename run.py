from config import *
import time

if __name__ == '__main__':
    start_time = time.time()
    url = "http://local.adspower.com:50325"
    chrome_id = "kp4ocpg"
    domain_name = 'couoyam'
    countrys = 'us'
    run_auto(url,chrome_id,domain_name,countrys).auto()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"程序运行时间: {elapsed_time:.2f} 秒")
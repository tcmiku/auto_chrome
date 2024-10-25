# my_script.py
import argparse
from config import *
import time

def main():
    start_time = time.time()
    url = "http://local.adspower.com:50325"

    parser = argparse.ArgumentParser(description='处理一些参数')
    parser.add_argument('chrome_id', type=str, help='浏览器ID')
    parser.add_argument('domain_name', type=int, help='域名')
    parser.add_argument('countrys', type=int, help='语言模板')
    args = parser.parse_args()

    print(f'参数1: {args.chrome_id}')
    print(f'参数2: {args.domain_name}')
    print(f'参数2: {args.countrys}')

    # run_auto(url,chrome_id,domain_name,countrys).auto()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"程序运行时间: {elapsed_time:.2f} 秒")

if __name__ == '__main__':
    main()




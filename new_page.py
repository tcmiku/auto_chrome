
from josn_pages.json_in import *
class NewPage:
    """
    用于格式化新页面
    countr默认为英文页面
    countr = ”de“ 则为德文页面
    """
    def __init__(self,country = "us"):
        file_path = 'josn_pages/pages.json'
        self.date = JSON_IN(file_path).read_json()
        self.country = country

    def add_page(self,web:str,end:str):
        new_page = self.date
        top_web = web.capitalize()
        big_web = web.upper()
        index = ['page'+ str(i) for i in range(1,len(new_page[self.country])+1)]
        for i in index:
            new_page[self.country][i]['content'] = self.__re_page(web,top_web,big_web,end,i)
        return new_page[self.country]

    def __re_page(self,web:str,top_web:str,big_web:str,end:str,index:str):
        page_content = self.date[self.country][index]['content']
        page_content = page_content.replace('{web}',web)
        page_content = page_content.replace('{top_web}',top_web)
        page_content = page_content.replace('{big_web}',big_web)
        page_content = page_content.replace('{end}', end)
        return page_content

if __name__ == '__main__':
    page = NewPage(country="grunsguru")   #德语模式
    print(page.add_page('qoupuay','de'))
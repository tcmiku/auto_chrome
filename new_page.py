from josn_pages.json_in import *
class NewPage:
    def __init__(self,country = "us"):
        file_path = 'josn_pages/pages.json'
        self.date = JSON_IN(file_path).read_json()
        self.country = country

    def add_page(self,web:str):
        top_web = web.capitalize()
        big_web = web.upper()
        self.__re_page(web,top_web,big_web)

    def __re_page(self,web:str,top_web:str,big_web:str):
        page_content = self.date[self.country]["page3"]['content']
        page_content = page_content.replace('{web}',web)
        page_content = page_content.replace('{top_web}',top_web)
        page_content = page_content.replace('{big_web}',big_web)
        print(page_content)

if __name__ == '__main__':
    page = NewPage()
    page.add_page('tcmiku')
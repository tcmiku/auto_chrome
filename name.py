from faker import Faker

class Name:
    def __init__(self):
        self.fake = Faker('zh_CN')  # 生成中文数据

    def generate_name(self):
        name = self.fake.name()          # 生成随机姓名
        address = self.fake.address()    # 生成随机地址
        email = self.fake.email()        # 生成随机邮箱
        return {'name': name, 'address': address, 'email': email}


if __name__ == '__main__':
    name = Name()
    print(name.generate_name())
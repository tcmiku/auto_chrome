# 随机密码生成器可选择密码长度以及是否包含数字、字母、特殊字符
import random
import string


class PasswordGenerator:
    def __init__(self,length=12, use_digits=True, use_letters=True, use_special=True):
        self.length = length
        self.use_digits = use_digits
        self.use_letters = use_letters
        self.use_special = use_special

    def generate_password(self):
        # 检查密码长度和字符类型的有效性
        if self.length < 4 and (self.use_digits or self.use_letters or self.use_special):
            raise ValueError("密码长度应至少为4个字符，若使用数字、字母或特殊字符。")
        if self.length < 1:
            raise ValueError("密码长度应至少为1个字符。")

        characters = ''
        if self.use_digits:
            characters += string.digits
        if self.use_letters:
            characters += string.ascii_letters
        if self.use_special:
            characters += string.punctuation

        if len(characters) < 1:
            raise ValueError("至少应使用一种字符类型。")

        password = []
        if self.use_digits:
            password.append(random.choice(string.digits))
        if self.use_letters:
            password.append(random.choice(string.ascii_letters))
        if self.use_special:
            password.append(random.choice(string.punctuation))

        # 计算剩余字符数
        remaining_length = self.length - len(password)
        if remaining_length > 0:
            password += random.choices(characters, k=remaining_length)

        random.shuffle(password)

        return ''.join(password)

# 示例用法：
if __name__ == '__main__':
    try:
        password = PasswordGenerator(length=10, use_digits=True, use_letters=True, use_special=False)
        print("密码:", password.generate_password())
    except ValueError as e:
        print("发生错误:", e)
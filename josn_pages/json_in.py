
import json

class JSON_IN:
    def __init__(self, filename):
        self.filename = filename

    def read_json(self) -> dict:
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
                print("成功读取 JSON 文件内容")
                return self.data
        except FileNotFoundError:
            print(f"文件 {self.filename} 未找到。")
        except json.JSONDecodeError:
            print("文件内容无法解码为 JSON。")
        except Exception as e:
            print(f"读取文件时发生错误: {e}")


if __name__ == '__main__':
    json_reader = JSON_IN('shippinganddelivery.json')
    print(type(json_reader.read_json()))
    print(json_reader.read_json())





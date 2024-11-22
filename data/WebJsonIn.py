def WebJsonIn_data(file_path,out_file_path,web_name) -> str:
    with open(file_path, 'r') as f:
        data = f.read()

    with open(out_file_path, 'w') as f:
        f.write(data.replace('{web_name}',web_name))

    return data.replace('{web_name}',web_name)


if __name__ == '__main__':
    WebJsonIn_data("yanximail.com.txt","../new_data/new_yanximail.com.txt","yanximail.com")
def text_reader(data_way):
    with open(data_way) as f:
        data = f.read().splitlines()
        print(data)
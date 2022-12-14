

def get_input(path: str):
    with open(path) as input_file:
        lines = input_file.readlines()
    return [line.strip('\n') for line in lines]

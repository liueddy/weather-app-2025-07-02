import re
from datetime import datetime
from collections import defaultdict

def my_map_reduce(file_name):
    d = defaultdict(int)

    def fun(s):
        d[s] += 1

    with open(f"{file_name}","r") as f:
        for ln in f:
            if not ln or ln[0] == "=" or "https://" in ln:
                continue
            else:
                [fun(x.lower()) for x in re.sub(r'[^a-zA-Z0-9]', ' ',ln).split()]
    
    return d

if __name__ == "__main__":
    start_time = datetime.now()
    d = my_map_reduce("ws.txt")
    end_time = datetime.now()

    print(d)
    print(f'Duration: {end_time - start_time}')
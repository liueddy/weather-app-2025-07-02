import re
from datetime import datetime
from collections import defaultdict

def my_map_reduce(file_name):
    c = defaultdict(int)
    d = defaultdict(int)

    a = {}
    ad = defaultdict(int)
    a["ACT 0"] = ad

    def fun(d,s):
        d[s] += 1

    with open(f"{file_name}","r") as f:
        for ln in f:
            if not ln or ln[0] == "=" or "https://" in ln:
                continue
            elif ln[:3] == "ACT":
                ad = defaultdict(int)
                a[f"ACT {ln[4]}"] = ad

            else:
                ls = re.sub(r'[^a-zA-Z0-9]', ' ',ln).split()
                # log words
                [fun( d,x.lower()) for x in ls]
                [fun(ad,x.lower()) for x in ls]
                # log chars:
                if len(ls) >= 2 and ls[1].isupper() and ls[0].isupper() and len(ls[1]) > 1 and len(ls[0]) > 1 and ls[0] != "PROLOGUE":
                    fun(c," ".join(ls[:2]))
                elif len(ls) >= 1 and len(ls[0]) > 1 and ls[0].isupper() and ls[0] != "PROLOGUE":
                    fun(c,ls[0])
                else:
                    continue

    return a,c,d

if __name__ == "__main__":
    start_time = datetime.now()
    a,c,d = my_map_reduce("ws.txt")
    end_time = datetime.now()

    # print(a["ACT 0"])
    print(c)
    print(f'Duration: {end_time - start_time}')
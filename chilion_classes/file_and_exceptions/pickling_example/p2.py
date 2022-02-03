import pickle
import os
from p3 import MyDate

def get_lst_dump():
    with open(os.path.join(os.path.dirname(__file__), "lst_dump"), "rb") as f:
        lst = pickle.load(f)

    print(lst)

get_lst_dump()# 5 more mins please
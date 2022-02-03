import pickle
import os

def make_lst(lst):

    with open(os.path.join(os.path.dirname(__file__), "lst_dump"), "wb") as f:
        pickle.dump(lst, f)


if __name__ == '__main__':
    lst = [x for x in range(100, 10000) if x % 2 != 0]
    make_lst(lst)

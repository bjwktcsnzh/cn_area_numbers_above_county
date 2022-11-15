# -*- coding: UTF-8 -*-
import sys
import os


def is_number(s: str):
    try:
        int(s)
        return True
    except:
        return False


def trim_txt(filename):
    os.makedirs("years_kv", exist_ok=True)
    writen = False
    with open(f'years_kv/{filename}', mode="w", encoding="utf-8") as f:
        with open(f'years_kv_src/{filename}', encoding="utf-8") as f2:
            for line in f2.readlines():
                if len(line) > 6 and is_number(line[0:6]):
                    if writen:
                        f.write("\n")
                    writen = True
                    entry = line.split("\t", maxsplit=3)
                    k = entry[0]
                    v = entry[1].strip(' \t\n')
                    f.write(f"{k}\t{v}")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        for _i in range(1, len(sys.argv)):
            trim_txt(sys.argv[_i])
    else:
        for txt_file in os.listdir("years_kv_src"):
            trim_txt(txt_file)

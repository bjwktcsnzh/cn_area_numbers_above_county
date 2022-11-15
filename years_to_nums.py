# -*- coding: UTF-8 -*-
from typing import List, Dict, Set
import os


def years_to_nums():
    """
    将文件夹kv中各年的数据合并起来，写入到 kv_merged.txt 中。格式示例如下
    110000 北京市:1980,1981,1982 北京区:2077
    """
    merged: Dict[int, Dict[str, Set[int]]] = {}
    for filename in os.listdir("years_kv"):
        year: int = int(filename[0: 4])
        with open(f"years_kv/{filename}", encoding="utf-8") as f:
            for line in f.readlines():
                split_res = line.split("\t")
                k = int(split_res[0])
                v = split_res[1].strip("\n")
                if merged.get(k) is None:
                    merged[k] = {}
                values = merged[k]
                if values.get(v) is None:
                    values[v] = set()
                values[v].add(year)
    os.makedirs("nums", exist_ok=True)
    for num, name2years in merged.items():
        with open(f"nums/{num}.txt", encoding="utf-8", mode="w") as f:
            first_line = True
            for name, years in name2years.items():
                years = list(years)
                years.sort()
                if not first_line:
                    f.write("\n")
                f.write(name)
                for year in years:
                    f.write("\t")
                    f.write(str(year))
                first_line = False


if __name__ == '__main__':
    years_to_nums()

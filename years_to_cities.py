# -*- coding: UTF-8 -*-
import os
from typing import Dict, Set


def years_to_cities():
    merged: Dict[str, Dict[int, Set[int]]] = {}
    for filename in os.listdir("years_kv"):
        year: int = int(filename[0: 4])
        with open(f"years_kv/{filename}", encoding="utf-8") as f:
            for line in f.readlines():
                split_res = line.split("\t")
                k = int(split_res[0])
                v = split_res[1].strip("\n")
                if merged.get(v) is None:
                    merged[v] = {}
                values = merged[v]
                if values.get(k) is None:
                    values[k] = set()
                values[k].add(year)
    os.makedirs("cities", exist_ok=True)
    for city, num2years in merged.items():
        with open(f"cities/{city}.txt", encoding="utf-8", mode="w") as f:
            first_line = True
            for num, years in num2years.items():
                years = list(years)
                years.sort()
                if not first_line:
                    f.write("\n")
                f.write(str(num))
                for year in years:
                    f.write("\t")
                    f.write(str(year))
                first_line = False


if __name__ == '__main__':
    years_to_cities()

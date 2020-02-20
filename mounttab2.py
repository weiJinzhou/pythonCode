#!/usr/bin/env python3
import os

def parse_mounts():
    """
    分析 /proc/mounts 并返回元组的列表
    """
    result = []
    file_path = '/proc/mounts'
    if os.path.exists(file_path):
        fd = open(file_path)
        for line in fd:
            line = line.strip()
            words = line.split()
            if len(words) > 5:
                res = (words[0], words[1], words[2], '({})'.format(' '.join(words[3:-2])))
            else:
                res = (words[0], words[1], words[2])
            result.append(res)
        fd.close()
    return result

def mount_details():
    """
    打印挂载详细信息
    """
    result = parse_mounts()
    for line in result:
        if len(line)  == 4:
            print('{} on {} type {} {}'.format(*line))
        else:
            print('{} on {} type {}'.format(*line))

if __name__ == '__main__':
    mount_details()

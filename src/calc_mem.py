#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math
import psutil
import subprocess as sh
# noinspection PyProtectedMember
from psutil._common import bytes2human


def total_mem():
    mem = psutil.virtual_memory()
    calc = getattr(mem, 'total')
    return (calc / 1024) / 1024


def total_swap():
    swap = psutil.swap_memory()
    return bytes2human(getattr(swap, 'total'))


def used_swap():
    swap = psutil.swap_memory()
    return bytes2human(getattr(swap, 'used'))


def status_swap():
    st = used_swap() + ' / ' + total_swap()
    if total_swap() == '0.0B':
        st += ' - disabled'
    else:
        st += ' - enabled'
    return st


def min_mem():
    if total_mem() < 1024:
        return total_mem()
    else:
        return int(math.sqrt(total_mem() / 1024) * 1024)


def rec_mem():
    if total_mem() < 1024:
        return total_mem() * 2
    else:
        return int(min_mem() + total_mem())


def max_mem():
    return int(total_mem() * 2)


def get_swappines():
    swp = sh.check_output('sysctl -n vm.swappiness', shell=True)
    return str(swp.decode()).strip('\n')

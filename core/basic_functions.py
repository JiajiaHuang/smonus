import random

import inspect


def DictMerge(dict1, dict2):
    """
    字典添加，相加
    :param dict1:
    :param dict2:
    :return:
    """
    res = {**dict1, **dict2}
    return res


def set_flow(count):
    base_int = random.randint(1, 100)
    base_code = str(base_int).zfill(3)
    count_str = str(count).zfill(6)
    return base_code + count_str


def get_variable_name(variable):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is variable]

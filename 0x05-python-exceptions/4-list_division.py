#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    CalcRe = None
    for i in range(list_length):
        try:
            CalcRe = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            CalcRe = 0
        except TypeError:
            print("wrong type")
            CalcRe = 0
        except ZeroDivisionError:
            print("division by zero")
            CalcRe = 0
        finally:
            result.append(CalcRe)
    return result

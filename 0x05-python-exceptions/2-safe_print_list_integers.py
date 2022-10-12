#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    cmpt = 0
    for index in range(x):
 ret = 0
    for i in range(0, x):
        try:
            print('{:d}'.format(my_list[index]), end='')
            cmpt += 1
        except IndexError:
            break
        except Exception:
            pass

    print('')
    return cmpt
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)

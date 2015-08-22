import time


# add month anomolies
def strconv(arg_str, increment):
    if len(arg_str) !=12:
        raise ValueError("Not enough values in date")

    time_list = [
        [arg_str[0:4], 9999], [arg_str[4:6], 12], [arg_str[6:8], 31], [arg_str[8:10], 23], [arg_str[10:], 59]
    ]
    final_list = []
    print "arg_str[:] ", arg_str[0:4], " ", arg_str[4:6], " ", arg_str[6:8], " ", arg_str[8:10], " ",arg_str[10:]

    arg_str = int(arg_str)

    for key in time_list:
        # print "element: ", element
        print "key[0]: ", key[0], "key[1]: ", key[1]
        final_list.append(convert(key[0], key[1], increment))
    print "initial final list: ", final_list
    final_list = "".join(final_list)
    print "final_list ", int(final_list)
    return int(final_list)

def convert(param, param_limit, increment):
    print "initial params: ", param," ", param_limit, " ", increment
    if param > param_limit:
        param =int(increment) - param_limit
        paramFinal = str(param)[-len(str(param))+1:]
        return paramFinal
    print "paramFinal :", paramFinal
    return param


def main():
    increment = 100
    generic = "201508211038"
    # strconv(generic)

    while 0 < 1:
        stringy = strconv(generic, increment)
        stringy += increment
        print "stringy: ", stringy
        time.sleep(5)


if __name__ == '__main__':
    main()
# probably best to chop up string into 5 manageable chunks
#all of these units are in base 10 but have limits on size.
# 2015, 08, 21, 10 38

# 2 0 1 5 0 8 2 1 1 0 3 8
# str[0,1,2,3,5,7,9],11 = base 10
# str[4] = base 2
# str[10] = base 7
# str[4 and 5] <= 12
# str[6] = base 4 #depending on the month
# str[8] = base 3
# str[8 and 9] <=23
# str[10 and 11] <= 60

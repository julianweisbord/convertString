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
    minutes = int(arg_str[10:])
    prev_increment = 0
    minutes +=increment
    # for list[x][0] run this and increment x to make adaptable for the other
    # time values.
    while minutes > time_list[4][1]:
        # numCheck(minutes,increment)
        if minutes > time_list[4][1]:
            minutes -= time_list[4][1]
        prev_increment+=1
        print "prev_increment: ", prev_increment
    print "minutes + increment: ", minutes

    # arg_str = int(arg_str)


# recursive call to check if num is greater than limit
# def numCheck(val,inc):
#     val += inc
#     if val > limit:
#         val = val - limit


    # else:
    #     valSmaller = True
    #     return valSmaller

#     for key in time_list:
#         # print "element: ", element
#         print "key[0]: ", key[0], "key[1]: ", key[1]
#         final_list.append(convert(key[0], key[1], increment))
#     print "initial final list: ", final_list
#     final_list = "".join(final_list)
#     print "final_list ", int(final_list)
#     return int(final_list)
#
# def convert(param, param_limit, increment):
#     print "initial params: ", param," ", param_limit, " ", increment
#     if param > param_limit:
#         param =int(increment) - param_limit
#         paramFinal = str(param)[-len(str(param))+1:]
#         return paramFinal
#     print "paramFinal :", paramFinal
#     return param


def main():
    increment = 100
    generic = "201508211038"
    # strconv(generic)
    stringy = strconv(generic, increment)
    print "stringy: ", stringy



if __name__ == '__main__':
    main()
# probably best to chop up string into 5 manageable chunks
#all of these units are in base 10 but have limits on size.
# 2015, 08, 21, 10 38
#take arg_str, convert to an integer, then increment by increment var.
# The increment will have to correspond to the right digit position.
# If that position is greater than the limit specified in time_list then the
# list must recursively go in reverse and increment the previous value by:
# 1 for each time you had to run the function that showed that the current value
# was greater than the limit.








# the (increment var)/limit,
# but only increment by first position
# ie: increment by 200 hours, 200/60 =3.333, so increment
# previous value by 3 then if next value plus 3 is greater than its limit say 30 +3
# then 33/31 (not all will be +1 ) = 1.064



# 2 0 1 5 0 8 2 1 1 0 3 8
# str[0,1,2,3,5,7,9],11 = base 10
# str[4] = base 2
# str[10] = base 7
# str[4 and 5] <= 12
# str[6] = base 4 #depending on the month
# str[8] = base 3
# str[8 and 9] <=23
# str[10 and 11] <= 60


#minute: 0-59, hour: 0-23, day: 1-31, month:1-12, year: 0-9999
# add month anomolies, leap year stuff
def strconv(arg_str, increment):
    if len(arg_str) !=12:
        raise ValueError("Not enough values in date")
#gives the default limits to each time chunk and the user input for each time chunk.
    time_list = [
        [arg_str[0:4], 9999], [arg_str[4:6], 11], [arg_str[6:8], 30], [arg_str[8:10], 23], [arg_str[10:], 59]
    ]

    final_list = []
    print "arg_str[:] ", arg_str[0:4], " ", arg_str[4:6], " ", arg_str[6:8], " ", arg_str[8:10], " ",arg_str[10:]

    times = int(time_list[4][0])
    prev_increment= 0

    x = 4
    for z in xrange (0, 5):
        #all but feb don't work
        if int(time_list[1][0]) == (4 or 6 or 9 or 11):
            time_list[2][1] = 29

        if int(time_list[1][0]) == 2:
            # for leap years
            if int(time_list[0][0])%4 ==0:
                time_list[2][1] = 28
            else:
                time_list[2][1] = 27

        while times +increment > time_list[x][1]:

            times =times - time_list[x][1] -1
            print time_list[x][1]

            prev_increment+=1
            print "prev_increment: ", prev_increment
        print "time + increment: ", times + increment
        final_list.append(times +increment)

        print "increment ", increment

        x-=1
        times= int(time_list[x][0])

        increment = prev_increment
        prev_increment = 0
    print "start date: ", arg_str.split()
    final_list= final_list[::-1]
    print "final date", final_list
    return str(final_list)
    # arg_str = int(arg_str)


def main():
    increment = 20000
    date = raw_input("Enter a 12 digit date: ")
    if date == None:
        date= "201602211038"
    # strconv(generic)
    stringy = strconv(date, increment)
    print "stringy: ", stringy



if __name__ == '__main__':
    main()
# probably best to chop up string into 5 manageable chunks
#all of these units are in base 10 but have limits on size.
# 2015, 08, 21, 10, 38
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

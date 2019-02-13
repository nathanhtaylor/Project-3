################################
#                              #
#        code graveyard        #
#                              #
################################







    # # open month files
    #
    # oct_log = open('Oct_Log.txt', "a+")
    # nov_log = open('Nov_Log.txt', "a+")
    # dec_log = open('Dec_Log.txt', "a+")
    # jan_log = open('Jan_Log.txt', "a+")
    # feb_log = open('Feb_Log.txt', "a+")
    # mar_log = open('Mar_Log.txt', "a+")
    # apr_log = open('Apr_Log.txt', "a+")
    # may_log = open('May_Log.txt', "a+")
    # jun_log = open('Jun_Log.txt', "a+")
    # jul_log = open('Jul_Log.txt', "a+")
    # aug_log = open('Aug_Log.txt', "a+")
    # sep_log = open('Sep_Log.txt', "a+")
    #
    # # working in 'AWS_Log.txt'
    # with open('AWS_Log.txt', 'r') as master_log:
    #     line = master_log.readline()
    #     error_total = 0
    #
    #     for line in master_log:
    #         # checking that line is valid local entry
    #         if (line[0:11] == 'local - - ['):
    #             dest = line[14:17] + '_Log.txt'
    #               ##########this doesnt work
    #             dest.write(line)
    #             line = master_log.readline()
    #
    #         # checking that line is valid remote entry
    #         elif (line[0:12] == 'remote - - ['):
    #             dest = line[15:18] + '_log.txt'
    #               ##########this doesnt work
    #             dest.write(line)
    #             line = master_log.readline()
    #
    #         # take count of error entries
    #         else:
    #             error_total += 1
    #             # print(error_total)
    #             line = master_log.readline()
    #
    #             close('Jan_Log.txt', "a+")
    #             close('Feb_Log.txt', "a+")
    #             close('Mar_Log.txt', "a+")
    #             close('Apr_Log.txt', "a+")
    #             close('May_Log.txt', "a+")
    #             close('Jun_Log.txt', "a+")
    #             close('Jul_Log.txt', "a+")
    #             close('Aug_Log.txt', "a+")
    #             close('Sep_Log.txt', "a+")
    #             close('Oct_Log.txt', "a+")
    #             close('Nov_Log.txt', "a+")
    #             close('Dec_Log.txt', "a+")
    #
    #
    #
    # return error_total

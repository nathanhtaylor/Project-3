################################
#                              #
#        code graveyard        #
#                              #
################################
# Here be dead code




    # # start the clock
    # start_time = time.process_time()
    # print('\nmain(): done in %s seconds' % round(time.process_time() - start_time, 3))
    #




# # take input 'lines' and write to 'AWS_Log.txt'
# def log_write(lines):
#     print('log_write(): Writing information to local log file...')
#     file = open('AWS_Log.txt', 'w+')
#     print(type(lines))
#     for e in lines:
#         #print(e)
#         file.write(e+'\n')
#     file.close()
#     return











# take 'AWS_Log.txt' and split in to 'Mon_Log.txt' files
# def month_split():
#     print('month_split(): Separating information by month...')
#
#     months = ['Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep','']
#     files = ['Oct_Log.txt', 'Nov_Log.txt', 'Dec_Log.txt', 'Jan_Log.txt', 'Feb_Log.txt', 'Mar_Log.txt', 'Apr_Log.txt', 'May_Log.txt', 'Jun_Log.txt', 'Jul_Log.txt', 'Aug_Log.txt','Sep_Log.txt']
#     total_count = 0
#
#     # start working in 'AWS_Log.txt'
#     with open('AWS_Log.txt', 'r') as master_log:
#         line = master_log.readline()
#         total_count += 1
#         # important for later
#         i = -1
#         # iterate through months
#         for mon in months:
#             # iterate
#             i += 1
#             # check if enough iterations have passed
#             if i == 12:
#                 ######## print('i=',i)
#                 break
#             # open relevant month file
#             with open(files[i], 'a+') as mon_log:
#                 # start iterating through lines that contain correct month
#                 while ('/'+months[i+1]+'/') not in line:
#                     print('month debug:')
#                     print(months[i])
#                     print(months[i+1])
#                     print(line)
#                     input()
#                     # check for errors
#                     if 'local -' not in line and 'remote -' not in line: #(line[0:11] != 'local -' and line[0:12] != 'remote -'):
#                         if(line == ''): # special case
#                             line = master_log.readline()
#                             total_count += 1
#                             break
#                         ######## print('error')
#                         print(line)
#                         line = master_log.readline()
#                         total_count += 1
#                     # write to file
#                     else:
#                         ######## print('print line')
#                         mon_log.write(line)
#                         line = master_log.readline()
#                         total_count += 1
#     return total_count











# months = ['Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep']
# i = 0
# while i < len(months):
#     print(months[i])
#     i += 1





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

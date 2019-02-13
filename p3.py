# Project 3
# Nathan Taylor
#
# How many total requests were made in the time period represented in the log?
# How many requests were made on each day? per week? per month?
# What percentage of the requests were not successful (any 4xx status code)?
# What percentage of the requests were redirected elsewhere (any 3xx codes)?
# What was the most-requested file?
# What was the least-requested file?


import urllib.request
import re



# fetch from URL and return content in variable 'lines'
def log_pull(inputurl):
    print('log_pull: Fetching log file')
    log = urllib.request.urlopen(inputurl)
    content = log.read()
    lines = content.decode()
    #print('lines: ',lines)
    log.close()
    return lines



# take input 'lines' and write to 'AWS_Log.txt'
def log_write(lines):
    print('log_write: Writing information to local log file')
    file = open('AWS_Log.txt', 'w+')
    file.write(lines)
    file.close()
    return



# take 'AWS_Log.txt' and split in to 'Mon_Log.txt' files
def month_split():
    print('month_split: Separating information by month')

    months = ['Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep','']
    files = ['Oct_Log.txt', 'Nov_Log.txt', 'Dec_Log.txt', 'Jan_Log.txt', 'Feb_Log.txt', 'Mar_Log.txt', 'Apr_Log.txt', 'May_Log.txt', 'Jun_Log.txt', 'Jul_Log.txt', 'Aug_Log.txt','Sep_Log.txt']

    # # working in 'AWS_Log.txt'
    with open('AWS_Log.txt', 'r') as master_log:
        line = master_log.readline()
        i = -1

        #for each month
        for mon in months:
            i += 1
            if i == 12:
                break
            print('i=',i)
            with open(files[i], 'a+') as mon_log:
                #start iterating through lines
                while ('/'+months[i+1]+'/') not in line:
                    if (line[0:11] != 'local - - [' and line[0:12] != 'remote - - ['):
                        if(line == ''):
                            line = master_log.readline()
                            break
                        print('error')
                        line = master_log.readline()
                    #write
                    else:
                        print('print line')
                        mon_log.write(line)
                        line = master_log.readline()










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
    return


# main
def main():
    print('main: Running program')
    lines = log_pull('https://s3.amazonaws.com/tcmg476/http_access_log')
    log_write(lines)
    month_split()


main()

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
from datetime import datetime
import os


# fetch from URL and return content in variable 'lines'
def log_pull(input_url):
    print('log_pull(): Fetching log file from ' + input_url + '...')

    # Put data on to lines variable
    log = urllib.request.urlopen(input_url)
    content = log.read()
    lines = content.decode()
    log.close()
    lines = lines.splitlines()

    # fill junk free list with lists of entry info
    junk_free = []
    for line in lines:
        # check that entry is in proper format
        parse = re.search('.* \[(.*?)\] .*? (.*?.*?.+) .*? (.+) (.+)', line)
        if parse:
            # add info to array and append to junk_free
            # junk_free = [ [time] , [filename] , [code1] , [code2] ]
            junk_free.append([parse.group(1),parse.group(2),parse.group(3),parse.group(4)])
        # else:
        #    print(line)
    return junk_free



# split up data by month and write it to month log files
def month_split(junk_free):
    print('month_split(): Separating information by month...')
    # junk_free = [ [time] , [filename] , [code1] , [code2] ]

    # Define a few things
    months = ['Oct','Nov','Dec','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep']
    files = ['Oct_Log.txt','Nov_Log.txt','Dec_Log.txt','Jan_Log.txt','Feb_Log.txt','Mar_Log.txt','Apr_Log.txt','May_Log.txt','Jun_Log.txt','Jul_Log.txt','Aug_Log.txt','Sep_Log.txt']
    total_count = 0
    i = -1
    j = 0

    # going through each month
    for month in months:
        # open the proper months file
        with open(month + '_Log.txt', 'w+') as file:
            # and write all of the entries that belong in that month
            while month in junk_free[j][0]:
                working = str(junk_free[j][0]) + ' ' + str(junk_free[j][1]) + ' ' + str(junk_free[j][2]) + ' ' + str(junk_free[j][3]) +'\n'
                file.write(working) #+ '\n')
                j += 1
                total_count += 1
    # return total length for later
    literal_total_count = len(junk_free)
    return literal_total_count



# read information and return information for report
def parse(junk_free, total_clean_lines):
    print('parse(): Parsing through data...')
    # junk_free = [ [time] , [filename] , [code1] , [code2] ]
    # results = [ Total Entries , [Weekdays] , [Months] , 3xx Total , 4xx Total , Most Req. , Least Req. ]
    results = [total_clean_lines,[0]*7,[0]*12,0,0,' ',' ',0,0]

    file_dict = {' ':5}

    for entry in junk_free:
        # check day of the week and month
        parsed_date = datetime.strptime(entry[0], '%d/%b/%Y:%H:%M:%S %z')
        results[1][parsed_date.weekday()] += 1
        results[2][parsed_date.month - 1] += 1

        # check error code
        if entry[2][0] == '3':
            results[3] += 1
        elif entry[2][0] == '4':
            results[4] += 1

        # check if file is in dictionary
        if entry[1] in file_dict:
            file_dict[entry[1]] += 1
            # update most requested file if needed
            if file_dict[entry[1]] > file_dict[results[5]]:
                results[5] = entry[1]
            # update least requested file if needed
            elif file_dict[entry[1]] < file_dict[results[5]]:
                results[6] = entry[1]
        # if not, add it
        else:
            file_dict[entry[1]] = 1
            # update most requested file if needed
            if file_dict[entry[1]] > file_dict[results[5]]:
                results[5] = entry[1]
            # update least requested file if needed
            elif file_dict[entry[1]] < file_dict[results[5]]:
                results[6] = entry[1]

    # add most/least totals to results
    results[7] = file_dict[results[5]]
    results[8] = file_dict[results[6]]

    return results



# clean up files afterwards
def clean_up():
    return



# main
def main():
    print('main(): Running program...')

    #run functions
    junk_free = log_pull('https://s3.amazonaws.com/tcmg476/http_access_log')
    total_clean_lines = month_split(junk_free)
    results = parse(junk_free, total_clean_lines)

    # print report
    print('='*30)
    print('=' + ' '*11 + 'REPORT' + ' '*11 + '=')
    print('='*30)
    print('\nTotal requests:\t', results[0])
    print('\tUnsuccessful requests (4xx codes): %d (%.2f%%)' % (results[4], (results[4]/results[0])*100) )
    print('\tRedirects (3xx codes): %d (%.2f%%)' % (results[3], (results[3]/results[0])*100) )
    print('\n Total requests per weekday:')
    print('\tMonday:  ',results[1][0])
    print('\tTuesday:  ',results[1][1])
    print('\tWednesday:  ',results[1][2])
    print('\tThursday:  ',results[1][3])
    print('\tFriday:  ',results[1][4])
    print('\tSaturday:  ',results[1][5])
    print('\tSunday:  ',results[1][6])
    print('\nThe most requested file was "%s" at %d requests' % (results[5], results[7]))
    print('\nThe least requested file was "%s" at %d requests' % (results[6], results[8]))

    print('main(): done')

    return

main()

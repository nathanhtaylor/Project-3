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
def log_pull(input_url):
    print('log_pull(): Fetching log file from',input_url,'...')
    log = urllib.request.urlopen(input_url)
    content = log.read()
    lines = content.decode()
    #print('lines: ',lines)
    log.close()
    return lines



# take input 'lines' and write to 'AWS_Log.txt'
def log_write(lines):
    print('log_write(): Writing information to local log file...')
    file = open('AWS_Log.txt', 'w+')
    file.write(lines)
    file.close()
    return



# take 'AWS_Log.txt' and split in to 'Mon_Log.txt' files
def month_split():
    print('month_split(): Separating information by month...')

    months = ['Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep','']
    files = ['Oct_Log.txt', 'Nov_Log.txt', 'Dec_Log.txt', 'Jan_Log.txt', 'Feb_Log.txt', 'Mar_Log.txt', 'Apr_Log.txt', 'May_Log.txt', 'Jun_Log.txt', 'Jul_Log.txt', 'Aug_Log.txt','Sep_Log.txt']

    # start working in 'AWS_Log.txt'
    with open('AWS_Log.txt', 'r') as master_log:
        line = master_log.readline()
        # important for later
        i = -1
        # iterate through months
        for mon in months:
            # iterate
            i += 1
            # check if enough iterations have passed
            if i == 12:
                ######## print('i=',i)
                break
            # open relevant month file
            with open(files[i], 'a+') as mon_log:
                # start iterating through lines that contain correct month
                while ('/'+months[i+1]+'/') not in line:
                    # check for errors
                    if (line[0:11] != 'local - - [' and line[0:12] != 'remote - - ['):
                        if(line == ''): # special case
                            line = master_log.readline()
                            break
                        ######## print('error')
                        line = master_log.readline()
                    # write to file
                    else:
                        ######## print('print line')
                        mon_log.write(line)
                        line = master_log.readline()
    return


# main
def main():
    print('main(): Running program...')
    lines = log_pull('https://s3.amazonaws.com/tcmg476/http_access_log')
    log_write(lines)
    month_split()
    return

main()

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
        parse = re.search('(.*?) - (.*) \[(.*?)\] \"GET\s(.*?)\s.*?\" (.+) (.+)', line)
        if parse:
            # add info to array and append to junk_free
            junk_free.append([parse.group(3),parse.group(4),parse.group(5),parse.group(6)])
    return junk_free



def month_split(lines):
    # print('month_split(): Separating information by month...')
    # months = ['Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep']
    # files = ['Oct_Log.txt', 'Nov_Log.txt', 'Dec_Log.txt', 'Jan_Log.txt', 'Feb_Log.txt', 'Mar_Log.txt', 'Apr_Log.txt', 'May_Log.txt', 'Jun_Log.txt', 'Jul_Log.txt', 'Aug_Log.txt','Sep_Log.txt']
    # total_count = 0

    #what on earth am i going to do with you

    return



def parse():
    return



# main
def main():
    print('main(): Running program...')
    junk_free = log_pull('https://s3.amazonaws.com/tcmg476/http_access_log')
    month_split(junk_free)
    print('Done')
    return

main()

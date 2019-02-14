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
    lines = lines.splitlines()
    return lines



# take input 'lines' and write to 'AWS_Log.txt'
def log_write(lines):
    print('log_write(): Writing information to local log file...')
    file = open('AWS_Log.txt', 'w+')
    print(type(lines))
    for e in lines:
        #print(e)
        file.write(e+'\n')
    file.close()
    return



def month_split():





    return



# main
def main():
    print('main(): Running program...')
    lines = log_pull('https://s3.amazonaws.com/tcmg476/http_access_log')
    log_write(lines)
    print('Total entries sorted:')
    return

main()

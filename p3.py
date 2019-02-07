# Project 3
# Nathan Taylor
#
# A script to collect and parse log information

import urllib.request

def log_pull(inputurl):
    #print('log_pull check')
    log = urllib.request.urlopen(inputurl)
    content = log.read()
    lines = content.decode()
    print('lines: ',lines)
    log.close()
    return lines

def log_write(lines):
    #print('log_write check')
    file = open('AWS_Log.txt', 'w+')
    file.write(lines)
    file.close()
    return

def main():
    #print('main check')
    lines = log_pull('https://s3.amazonaws.com/tcmg476/http_access_log')
    log_write(lines)
    return

main()

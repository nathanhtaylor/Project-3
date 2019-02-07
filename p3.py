# Project 3
# Nathan Taylor
#
# A script to collect and parse log information
import urllib.request

def log_pull():
    log = urllib.request.urlopen('https://s3.amazonaws.com/tcmg476/http_access_log')
    content = log.read()
    lines = content.decode()
    log.close()
    return lines

def write():
    return

def main():
    return

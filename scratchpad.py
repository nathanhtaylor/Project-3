import urllib.request

input_url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
print('log_pull(): Fetching log file from',input_url,'...')
log = urllib.request.urlopen(input_url)
content = log.read()
lines = content.decode()
#print('lines: ',lines)
log.close()
print(type(lines))

lines = lines.splitlines()
print(type(lines))
print(len(lines))

for i in lines:
    if 'Oct' in i:
        print(i)

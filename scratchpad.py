# How many total requests were made in the time period represented in the log?
# How many requests were made on each day? per week? per month?
# What percentage of the requests were not successful (any 4xx status code)?
# What percentage of the requests were redirected elsewhere (any 3xx codes)?
# What was the most-requested file?
# What was the least-requested file?


# WIP parse_2()
# def parse_2():
#
#
#     # results = [ Total Entries , [Weekdays] , [Months] , 3xx Total , 4xx Total , Most Req. , Least Req. ]
#     results
#
#     return results
#
# def main():
#     entry = ['01/Aug/1995:00:01:52 -0600', '276.html', '200', '1041']
#     parse
results = [100,[0]*7,[0]*12,0,0,' ',' ',0,0]
results[2][0] = 10000
results[2][2] = 100


print('\n'+'='*70)
print('=' + ' '*31 + 'REPORT' + ' '*31 + '=')
print('='*70)
print('\nTotal requests:\t', results[0])
print('\tUnsuccessful requests (4xx codes): %d (%.2f%%)' % (results[4], (results[4]/results[0])*100) )
print('\tRedirects (3xx codes): %d (%.2f%%)' % (results[3], (results[3]/results[0])*100) )
print('\nTotal requests per weekday:')
print('\nTotal requests per weekday:')
print('\tMonday:  \t', results[1][0])
print('\tTuesday:  \t', results[1][1])
print('\tWednesday:  \t', results[1][2])
print('\tThursday:  \t', results[1][3])
print('\tFriday:  \t', results[1][4])
print('\tSaturday:  \t', results[1][5])
print('\tSunday:  \t', results[1][6])
print('\nTotal Requests per Month:')
print('\tJan: %d\tFeb: %d' % (results[2][0], results[2][1]))
print('\tMar: %d\tApr: %d' % (results[2][2], results[2][3]))
print('\tMay: %d\tJun: %d' % (results[2][4], results[2][5]))
print('\tJul: %d\tAug: %d' % (results[2][6], results[2][7]))
print('\tSep: %d\tOct: %d' % (results[2][8], results[2][9]))
print('\tNov: %d\tDec: %d' % (results[2][10], results[2][11]))

print('\nThe most requested file was "%s" with %d requests' % (results[5], results[7]))
print('\nThe least requested file was "%s" with %d requests' % (results[6], results[8]))
print('\n' + '='*70)

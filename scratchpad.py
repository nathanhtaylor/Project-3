# How many total requests were made in the time period represented in the log?
# How many requests were made on each day? per week? per month?
# What percentage of the requests were not successful (any 4xx status code)?
# What percentage of the requests were redirected elsewhere (any 3xx codes)?
# What was the most-requested file?
# What was the least-requested file?

# results = [ Total Entries , [Weekdays] , [Months] , 3xx Total , 4xx Total , Most Req. , Least Req. , Most Total , Least Total]
results = [724063, [116166, 127990, 129250, 122010, 102477, 62232, 63938], [43599, 72007, 99562, 64947, 63692, 53632, 54892, 66038, 89063, 45766, 41147, 29718], 128067, 28333, 'index.html', '11459.html', 5, 2]

print('='*30)
print('=' + ' '*11 + 'REPORT' + ' '*11 + '=')
print('='*30)
print('\nTotal requests:\t', results[0])
print('\tUnsuccessful requests (4xx codes): %d (%.2f%%)' % (results[4], (results[4]/results[0])*100) )
print('\tRedirects (3xx codes): %d (%.2f%%)' % (results[3], (results[3]/results[0])*100) )
print('\nTotal requests per weekday:')
print('\tMonday:  ',results[1][0])
print('\tTuesday:  ',results[1][1])
print('\tWednesday:  ',results[1][2])
print('\tThursday:  ',results[1][3])
print('\tFriday:  ',results[1][4])
print('\tSaturday:  ',results[1][5])
print('\tSunday:  ',results[1][6])
print('\nThe most requested file was "%s" at %d requests' % (results[5], results[7]))
print('\nThe least requested file was "%s" at %d requests' % (results[6], results[8]))

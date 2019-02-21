# How many total requests were made in the time period represented in the log?
# How many requests were made on each day? per week? per month?
# What percentage of the requests were not successful (any 4xx status code)?
# What percentage of the requests were redirected elsewhere (any 3xx codes)?
# What was the most-requested file?
# What was the least-requested file?




# WIP parse_2()

file_dict = {}

def parse_2(entry):
    # entry = ['date','filename','code1', 'code2']
    # results = [ Total Entries , [Weekdays] , [Months] , 3xx Total , 4xx Total , Most Req. , Least Req. ]

    # increment weekday and month count
    parsed_date = datetime.strptime(entry[0], '%d/%b/%Y:%H:%M:%S %z')
    results[1][parsed_date.weekday()] += 1
    results[2][parsed_date.month - 1] += 1

    # check if file is in dictionary
    if entry[1] in file_dict:
        file_dict[entry[1]] += 1
        # update most requested file if needed
        if file_dict[entry[1]] > file_dict[results[5]]:
            results[5] = entry[1]
        # update least requested file if needed
        elif file_dict[entry[1]] < file_dict[results[5]]:
            results[6] = entry[1]
    # if not in dictionary, add it
    else:
        file_dict[entry[1]] = 1
        # update most requested file if needed
        if file_dict[entry[1]] > file_dict[results[5]]:
            results[5] = entry[1]
        # update least requested file if needed
        elif file_dict[entry[1]] < file_dict[results[5]]:
            results[6] = entry[1]

    # check error code
    if entry[2][0] == '3':
        results[3] += 1
    elif entry[2][0] == '4':
        results[4] += 1



    return results

        # # add most/least totals to results
        # results[7] = file_dict[results[5]]
        # results[8] = file_dict[results[6]]
        #needs to be added to main



def main():
    entry = ['01/Aug/1995:00:01:52 -0600', '276.html', '200', '1041']



    print(testdate)
    #parse_2(entry)

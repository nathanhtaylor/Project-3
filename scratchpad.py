# local - - [24/Oct/1994:13:41:41 -0600] "GET index.html HTTP/1.0" 200 150
# local - - [24/Oct/1994:13:41:41 -0600] "GET 1.gif HTTP/1.0" 200 1210
# local - - [24/Oct/1994:13:43:13 -0600] "GET index.html HTTP/1.0" 200 3185
# local - - [24/Oct/1994:13:43:14 -0600] "GET 2.gif HTTP/1.0" 200 2555
# local - - [24/Oct/1994:13:43:15 -0600] "GET 3.gif HTTP/1.0" 200 36403
# local - - [24/Oct/1994:13:43:17 -0600] "GET 4.gif HTTP/1.0" 200 441
# local - - [24/Oct/1994:13:46:45 -0600] "GET index.html HTTP/1.0" 200 3185
# local - - [24/Oct/1994:13:46:45 -0600] "GET 2.gif HTTP/1.0" 200 2555

dict = {'a':3, 'b':- 2, 'c':3}
if 'a' in dict:
    print('a')

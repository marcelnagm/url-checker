import sys
import requests

urllist_404 = []
resplist = []
code_list = []

count = 0
def get_url_status(urls):  # checks status for each url in list urls
    
    for url in urls:
        try:
            r = requests.get(url)
            print(url + "\tStatus: " + str(r.status_code))
        except Exception as e:
            print(url + "\tNA FAILED TO CONNECT\t" + str(e))
    return None

file1 = open(sys.argv[1], 'r')
Lines = file1.readlines()
get_url_status(Lines);
#for line in Lines:
#    count += 1
#    print("Line{}: {}".format(count, line.strip()))

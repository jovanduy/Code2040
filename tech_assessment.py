"""
Code2040 Tech Assessment script

Script completes each of the 5 registration steps,
printing to stdout every time a step has been completed.

@author: jovanduy (Jordan Van Duyne)

To run: python tech_assessment.py
"""

import urllib, urllib2, json, datetime
from pprint import pprint

URL = 'http://challenge.code2040.org/api/'
reg_args = {'token': 'a8c3fae224652713fcec9a0b14ebeae6', 'github': 'https://github.com/jovanduy/Code2040'}
token = {'token': 'a8c3fae224652713fcec9a0b14ebeae6'}

def post(url, data):
    """
    Given a url and a dictionary, encode the dictionary to a JSON
    to POST that JSON to the url. Returns the response.

    url: String representing a url
    data: dictionary to be POSTed as JSON
    """
    req = urllib2.Request(url, urllib.urlencode(data, True)) # doseq=True since some values of data are lists
    res = urllib2.urlopen(req).read()
    return res

def register():
    """
    Step 1: Register using the provided token and github link.
    Prints the result to inform user this step passed.
    """
    print post(URL + 'register', reg_args)

def step2():
    """
    Step 2: Reverse a string.
    Make a POST request for the string,
    then POST a JSON containing the token and reversed string.

    Prints the result to inform user this step passed.
    """
    # POST token to get string
    s = post(URL + 'reverse', token)

    # dictionary containing token and reversed string
    data = token.copy()
    data['string'] = s[::-1]

    res = post(URL + 'reverse/validate', data)
    print res

def step3():
    """
    Step 3: Needle in a haystack.
    Make a POST request for JSON with a needle string and a haystack array of strings.
    POST a JSON containing the token and the index of the needle in the array.

    Prints the result to inform user this step passed.
    """
    # POST to get JSON and convert to dictionary
    res = post(URL + 'haystack', token)
    res = json.loads(res)

    # get the needle and the haystack
    needle = res['needle']
    haystack = res['haystack']

    # dictionary containing token and index of needle in the haystack
    data = token.copy()
    data['needle'] = haystack.index(needle)

    res = post(URL + 'haystack/validate', data)
    print res

def step4():
    """
    Step 4: Prefix.
    Make a POST request for a JSON with a prefix string and an array of strings.
    POST a JSON containing the token and the strings in array that do not begin with prefix.

    Prints the result to inform user this step passed.
    """
    # POST to get JSON and convert to dictionary
    res = post(URL + 'prefix', token)
    res = json.loads(res)

    # get the prefix and list of words as str (not unicode) that do not start with the prefix
    prefix = res['prefix']
    words = [str(word) for word in res['array'] if not word.startswith(prefix)]

    # dictionary containing token and array of strings
    data = token.copy()
    data['array[]'] = words

    res = post(URL + 'prefix/validate', data)
    print res

def step5():
    """
    Step 5: The dating game.
    Make a POST request for a JSON with an ISO 8601 formatted string datestamp and a seconds interval.
    POST a JSON containing the token and a new datestamp that is the original 
    datestamp + the seconds interval.

    Prints the result to inform user this step passed.
    """
    # POST to get JSON and conver tot dictionary
    res = post(URL + 'dating', token)
    res = json.loads(res)

    # convert the datestamp string to a datetime object to add interval
    date = datetime.datetime.strptime(res['datestamp'], '%Y-%m-%dT%H:%M:%SZ')
    date += datetime.timedelta(seconds=res['interval'])

    # dictionary containing token and new datestamp string formatted as expected
    data = token.copy()
    data['datestamp'] = str(date.isoformat()) + 'Z'

    res = post(URL + 'dating/validate', data)
    print res

if __name__ == '__main__':
    register()
    step2()
    step3()
    step4()
    step5()

# -*- coding: utf-8 -*-
import chimpy
from pprint import pprint
import optparse
import csv
import os

SAMPLE_BATCH = [{'EMAIL': 'office@webmeisterei.com',
          'EMAIL_TYPE':'html', #needs to be present
          'Firma': u"A. Thaler Möbel für den Gast".encode('utf-8')},

         {'EMAIL': 'harald@webmeisterei.com',
          'EMAIL_TYPE':'html',
          'Firma': u"AEC-Irino AG"},
          ]

def csv2Batch(csvfilename):
    batch = []
    reader = csv.reader(open(csvfilename, 'rb'), delimiter=';', quotechar='"')

    #first line is column headings
    headings = reader.next()

    for values in reader:
        dataset = dict(EMAIL_TYPE='html')
        for i, val in enumerate(headings):
            dataset[val] = values[i]
        batch.append(dataset)
    return batch



def main():

    parser = optparse.OptionParser(usage="""%prog FILENAME

%prog imports datasets given in csv file FILENAME into mailchimp's subscriber list.

first row contains headers, EMAIL (note capital letters) column is required

example csv content:
"Some Value";"EMAIL";"Some other value";
"ACME Corp.";"john@acme.com";"Sales representative";

""")

    parser.add_option('-k', '--apikey',
                      dest='apiKey', default=None,
                      help="your mailchimp api key. obtain one with ``wget 'http://api.mailchimp.com/1.1/?output=json&method=login&password=xxxxxx&username=yyyyyyyy' -O apikey``")

    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.print_help()
        return

    if not options.apiKey:
        if not 'MAILCHIMP_APIKEY' in os.environ:
            parser.error("Either set the MAILCHIMP_APIKEY environment variable add the -k option (see -h for help).")
            return
        else:
            API_KEY = os.environ['MAILCHIMP_APIKEY']
    else:
        API_KEY = options.apiKey


    chimp = chimpy.Connection(API_KEY)


    availableLists = chimp.lists()
    if len(availableLists) < 1:
        print "no lists available to import into"
        return 1

    if len(availableLists) > 1:
        print "multiple lists available, no selection available atm - sorry"
        return 1

    mList = availableLists[0]

    batch = csv2Batch(args[0])

    print "importing %d datasets to list '%s'" % (len(batch), mList['name'])

    print "list members before import: %d" % len(chimp.list_members(mList['id']))

    result = chimp.list_batch_subscribe(mList['id'], batch, double_optin=False)

    print "list members after import: %d" % len(chimp.list_members(mList['id']))

    print "successfully imported %d, with %d errors" % (result['success_count'], result['error_count'])
    if result['error_count']:
        pprint(result['errors'])


if __name__ == "__main__":
    main()
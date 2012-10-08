Why?
====

mailchimp__ does not allow to import so called role addresses via the webinterface.

.. __: http://mailchimp.com

so ``info@``, ``support@``, ``office@`` and the like can't be imported but need to be inserted manually.
(see `What role addresses does MailChimp block`__)

.. __: http://kb.mailchimp.com/article/what-role-addresses-does-mailchimp-specifically-block-from-bulk-importing/


HOW?
====

this script allows to import subscriptions even though some or all emails are role addresses
using the mailchimp API `MCAPI`__.

.. __: http://apidocs.mailchimp.com/api/1.2/

type ``chimpimport --help`` for usage information::

    chimpimport imports datasets given in csv file FILENAME into mailchimp's subscriber list.

    first row contains headers, EMAIL (note capital letters) column is required

    example csv content:
    "Some Value";"EMAIL";"Some other value";
    "ACME Corp.";"john@acme.com";"Sales representative";



    Options:
      -h, --help            show this help message and exit
      -u, --updateExisting  if given, existing subscribers will be updated
      -k APIKEY, --apikey=APIKEY
                            your mailchimp api key. to obtain one:
                            http://kb.mailchimp.com/article/where-can-i-find-my-api-key``

Status
======

Successfully used for 1500 subscribers.

Supports custom fields (just add headers for them to the import csv)

Supports multiple subscriber list. If you have multiple lists, the script will prompt the list to import data into.
#!/usr/bin/python

import sys
import getopt
import logging


def parse_args(argh):
    print(argh)
    print(len(argh))
    # You need the "=" sign in the list of options to be tested, the shortlist parameter doesn't need to be filled
    opts, arguments = getopt.getopt(argh, '', ['affirm=', 'logging=', 'crap='])
    # opts is now a list of tuples - it's a static list - values don't change no matter what
    print(opts)
    # And now iterate through the options tuple - and use them - don't know why the arguments didn't come out before
    for opt in opts:
        if opt[0] == "--affirm":
            print(opt[1])
            # Do something with opt[1]
        if opt[0] == "--logging":
            print(opt[1])
            # Do something with opt[2]
        if opt[0] == "--crap":
            print(opt[1])
            # Do something with opt[3]
        if opt[0] == "--log"
            loglevel = opt[1]
            getattr(logging, loglevel)


if __name__ == "__main__":
    # Pull out all the command line parameters, except the filename, yes it's a list []
    args = sys.argv[1:]
    # Pass it into a function to parse all the arguments and assign system variables
    parse_args(args)


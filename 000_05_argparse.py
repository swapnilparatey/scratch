#!/usr/bin/python3.8
# https://www.golinuxcloud.com/python-argparse/
# differnt types of dest = store, store_const, store_true, store_false, append
# append_const, version

import argparse

## create the parser object
parser = argparse.ArgumentParser()
# Use different prefix - and then change all the prefixes eslewhere
# parser = argparse.ArgumentParser(prefix_chars='/')

## add arguments
# parse arguments without value
parser.add_argument('-q', '--quiet',
                    action='store_true',
                    dest='quiet',
                    help='Suppress Output'
                    )
parser.add_argument('-v', '--verbose',
                    action='store_true',
                    dest='verbose',
                    help='Verbose Output'
                    )

# use different prefix
# parser.add_argument('/q', '//quiet', - incase of a different prefix


# pass single value to argument
parser.add_argument('-H', '--host',
                    default='localhost',
                    dest='host',
                    help='Provide destination host. Defaults to localhost',
                    type=str
                    )

# pass multiple values to argumentt
parser.add_argument('--range',
                    default=[1-100],
                    dest='range',
                    help='Define the range. Default is 1-100',
                    type=int,
                    nargs=2         # exactly two arguments
                    #nargs='+'      # multiple arguments
                    #nargs='*'      # zero or more values
                    )


# mandatory arguments
parser.add_argument('-l', '--sleep',
                    required=True,
                    default=20,
                    dest='sleep',
                    help='Provide sleep timer',
                    type=int
                    )

# multiple choices - choose one
parser.add_argument('--color',
                    choices=('blue', 'black', 'brown'),
                    dest='color',
                    default='blue',
                    help='Guess my lucky color'
                    )

# read a file as an input for getting configs through argument
parser.add_argument('--file',
                    type=argparse.FileType('r'),
                    dest='myfile',
                    default='/home/linpaws/python_practice/config_file',
                    help='The config file to use'
                    )

# actions
parser.add_argument('-s', action='store', dest='simple_value', help='Store a simple value')
parser.add_argument('-c', action='store_const', dest='constant_value', const='value-to-store', help='Store a constant value')
parser.add_argument('-t', action='store_true', default=False, dest='boolean_t', help='Set a switch to true')
parser.add_argument('-f', action='store_false', default=True, dest='boolean_f', help='Set a switch to false')
parser.add_argument('-a', action='append', dest='collection', default=[], help='Add repeated values to a list')
parser.add_argument('-A', action='append_const', dest='const_collection', const='value-1-to-append', default=[], help='Added different values to list')
parser.add_argument('-B', action='append_const', dest='const_collection', const='value-2-to-append', help='Add different values to list')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')



## parse and print results
args = parser.parse_args()
print("quiet: ", args.quiet)
print("verbose: ", args.verbose)
print("host: ", args.host)
print("range: ", args.range)
print("sleep: ", args.sleep)
print("color: ", args.color)
print("file: ", args.myfile.read())

print('simple_value     = {!r}'.format(args.simple_value))
print('constant_value   = {!r}'.format(args.constant_value))
print('boolean_t        = {!r}'.format(args.boolean_t))
print('boolean_f        = {!r}'.format(args.boolean_f))
print('collection       = {!r}'.format(args.collection))
print('const_collection = {!r}'.format(args.const_collection))

# Import the argparse lib
from argparse import ArgumentParser
from argparse import HelpFormatter

class SmartFormatter(HelpFormatter):
	def _split_lines(self, text, width):
		if text.startswith("R|"):
			return text[2:].splitlines()  
        # this is the RawTextHelpFormatter._split_lines
		return HelpFormatter._split_lines(self, text, width)

# Create the parser
parser = ArgumentParser(description='test', formatter_class=SmartFormatter)


# Add the arguments

parser.add_argument('accname',
						metavar='username',
						type=str,
						help='the username of the desired account')
parser.add_argument('accpass',
						metavar='password',
						type=str,
						help='the password of the desired account')
parser.add_argument('url',
                       	metavar='url',
                       	type=str,
                       	help='the url of the activity')
parser.add_argument('-t',choices=['t', 'g', 'd'], default='t',
    help="R|The type of activity, where\n"
         " t -> Tickbox based\n"
         " g -> Gap-fill based\n"
         " d -> Dropdown")
		 
# Execute the parse_args() method
args = parser.parse_args()
print(args)
activityType = args.t
urldesired = args.url
accname = args.accname
accpass = args.accpass

print(activityType)
print(urldesired)
print(accname)
print(accpass)
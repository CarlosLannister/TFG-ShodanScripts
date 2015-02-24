import shodan 
import time 
from optparse import OptionParser


class palantirContext(object):

	def __init__(self):
		self.shodan_key = 'YOUR API KEY !!!!'
		self.output = 'results.txt'
		self.query = ''
		self.message = ''
		self.page = 1 

def get_cmd_line_args():
	context = palantirContext()

	opts = OptionParser()

	opts.add_option('--key', '-k', help='shodan api key', default=context.shodan_key, type="string",dest="key")
	opts.add_option('--output', '-o', help='output file name', default=context.output, type="string", dest="output")
	opts.add_option('--query', '-q', help='query Shodan Type', default=context.query, type="string", dest="query" )

	opts.add_option('--page', '-p', help='page namber of results', default=context.page, type="int", dest="page")

	(options, args) = opts.parse_args()

	context.shodan_key = options.key
	context.output = options.output
	context.query = options.query
	context.page = options.page

	return context

def main():
	context = get_cmd_line_args()

	api=shodan.Shodan(context.shodan_key)

	outfile = open(context.output, 'w')

	query = context.query
	
	page = context.page
	page_init = page
	try:
		results = api.search(query)

		print 'Results found: %s' % results['total']
		time.sleep(5)
		while (page * 100 <= results['total']):
			for result in results['matches']:
				ip = "%s \n" % result['ip_str']
				print 'Found IP: %s' % result['ip_str']
				outfile.write(ip)
				outfile.flush()		
			page = page + 1
			print 'Page %s' % page 
			results = api.search(query,page)
	except shodan.APIError, e:
		print 'Error %s' % e
		print ('Page init %s Current page %s ' % (page_init, page)) 

if __name__ == '__main__':
    main()




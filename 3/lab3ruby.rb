require 'net/http'
require 'json'
uri = URI('http://api.meetup.com/2/open_events.xml?zip=60290&format=json&text=python+hackathon+javascript&time=,1w&key=c3c5c5a3b2d537537d1553375c447')
source = Net::HTTP.get(uri)
fname = "page.html"
somefile = File.open(fname, "w")
parsed = JSON.parse(source)

	for x in parsed['results']
	somefile.puts "<h1><br> #{x['name']} </h1><br><br> #{x['venue']['city']} #{x['venue']['address_1']} <br> #{x['description']} <br><br>"	
	end
gets 

require 'net/http'
url = 'http://www.mosigra.ru'
uri = URI('http://www.mosigra.ru')
source = Net::HTTP.get(uri)
links = source.scan(/href="(\/[\w\.\-\/]+)/)
puts "links ="
puts links
allemails = []
for i in 5..7	
	uri = URI([url, links[i]].join)
	page = Net::HTTP.get(uri)
	emails = page.scan(/[\w\.\-]+@[\w\.\-]+/)
	allemails = allemails + emails
end
puts "emails"
allemails.uniq!
puts allemails
gets 

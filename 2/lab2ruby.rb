text = File.read("access.log")

ips = text.scan(/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/)
ips.uniq!
nets = Hash.new()
network = ""
sorted_ips = ips.sort_by { |ip| ip.split(".").map(&:to_i) }


for ip in sorted_ips
	newnetwork = ip.scan(/(\d{1,3}\.\d{1,3}\.\d{1,3})\.\d{1,3}/)
	if network!=newnetwork
		network=newnetwork
		sorted_ips.insert(sorted_ips.index(ip),network)
	end
end
puts sorted_ips
puts "done"
gets

#!/usr/bin/env ruby

# Input is expected to follow the form found in IdnaMappingTable.txt 
# from The Unicode Consortium

puts "# encoding: UTF-8\n\n"

map = {}
ARGF.each do |line|
  # Copy full comment lines to output
  puts line if line[0] == '#'

  s = line.strip.split('#').first
  next if s.nil?

  p = s.split(';').map{|s| s.strip}

  if p[1] == "ignored"
    p[1] = "mapped"
    p[2] = ""
  end

  next unless p[1] == "mapped" || p[1] == "disallowed_STD3_mapped"

  dst = p[2].split(/\s+/).map do |hex|
    hex.to_i(16)
  end
  if dst.length == 1
    dst = dst.first
  end

  if p[0].include?('..')
    a, b = p[0].split('..',2).map{|n|n.to_i(16)}
    (a..b).each do |n|
      map[n] = dst
    end
  else
    src = p[0].to_i(16)
    map[src] = dst
  end
end

# Output final mapping data
puts
puts 'module SimpleIDN'
puts '  UTS64MAPPING = {'
map.each do |k, v|
  puts "    #{k} => #{v},"
end
puts '  }'
puts 'end'

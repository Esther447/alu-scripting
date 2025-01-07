#!/usr/bin/env ruby
#Ensure an argument is passed
if ARGV.empty?
  puts "Usage: ./5-beginning_and_end.rd <inputs_string>"
  exit
end

puts ARGV[0].scan(/^h.n$/).join

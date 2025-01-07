#!/usr/bin/env ruby
#Ensure an argument is passed
if ARGV.empty?
  puts "Usage: ./7-OMG_WHY_ARE_YOU_SHOUTING.rb <input_string>"
  exit
end

puts ARGV[0].scan(/[A-Z]/).join


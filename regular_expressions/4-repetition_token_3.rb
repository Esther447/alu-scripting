#!/usr/bin/env ruby
#Ensure an argument is passed
if ARGV.empty?
  puts "Usage: ./4-repetition_token_2.rb <inputs_string>"
  exit
end

puts ARGV[0].scan(/hbt*n/).join

#!/usr/bin/env ruby
#Check if any argument is provided
if ARGV.empty?
  puts "Usage: ./1-repetition_token_0.rb <input_string>"
  exit
end

puts ARGV[0].scan(/hbt{2,5}n/).join

#!/usr/bin/env ruby
# Read the input from command line argument
input = ARGV[0]

# Regular expression to extract sender, reciever, and flags
regex = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/

# Match the input log line against the regex
match = input.match(regex)

# Extract and print the required fields in the specified format
if match 
  sender = match[1]
  reciever = match[2]
  flags = match[3]
  puts "#{sender},#{reciever},#{flags}"
else
  # Handle case where input doesn't match the expected format
  puts "No valid data found in input."
end

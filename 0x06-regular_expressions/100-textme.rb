#!/usr/bin/env ruby
# Text me

TEXT_REGEX = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/
puts ARGV[0].scan(TEXT_REGEX).join(',')

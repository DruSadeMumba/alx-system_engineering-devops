#!/usr/bin/env ruby
# A regular expression that matches a 10 digit phone number

VALID_NUMBER_REGEX = /\A\d{10}\Z/
puts ARGV[0].scan(VALID_NUMBER_REGEX).join

#!/usr/bin/env ruby

require 'net/http'
require 'net/ftp'
require 'open-uri'
require 'open_uri_redirections'
require 'date'
require 'mechanize'

$agent = Mechanize.new

$page = $agent.get('https://gamepress.gg/pokemongo/pokemon-list')

$index = Array[]
$index = $page.search('//tr[@class = "pokemon-row"]')
for i in $index do
    str = '('
    n = 0
    for a in i do
        if(n == 10)#def
            str += " " + a[1]
        elsif(n == 9)#att
            str += " " + a[1]
            str += ','
        elsif(n == 8)#stam
            str += " " + a[1]
            str += ','
        elsif(n == 7)#numdex
            str += " " + a[1]
            str += ','
        elsif(n == 3)#km/cand
            str += " " + a[1][6, 2]
            str += ','
        elsif(n == 1) #name
            str += a[1]
            str += ','
        end
        n += 1
    end
    str += '),' + "\n"
    puts str
end


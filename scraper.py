# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

#import the scraperwiki library to store data
import scraperwiki
import lxml.html

print "Hello World"
myname = "Gianluca"
print myname

# # Read in a page
html = scraperwiki.scrape("http://foo.com")
print html
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
print root
root.cssselect("div[align='left']")
selectstuff = root.cssselect("a")
print selectstuff

urltoscrape = "http://site.com/"
listylist = ["p1","p2","p3"]
for blah in listylist:
    print blah
    fullurl = urltoscrape+blah
    print fullurl
    
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

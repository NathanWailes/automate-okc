# automate-okc

To Do:

scrape_usernames:

scrape_profiles:
 - Scrape the profile pictures and have some fast way of deciding if you want to contact them, so you don't have to keep using QuickMatch.
 - Have some way of automatically re-scraping the site every night to get any new profiles that may have come online.
 - Make the program less likely to lose all the data when you quit it from the command line.
 - Handle cases where you run across a profile that 'doesn't exist' (was made hidden)

scrape_messages:
 - Scrape your messages so the program knows who has responded to your messages.






Done:
 - have the scraper capable of working bit-by-bit (saving data as it goes) instead of needing to do everyone at once before it saves anything
 - See if there's some kind of API that could help you get information.

Related projects:
 - Ruby - https://github.com/trek/lonely_coder
 - JavaScript - http://hungtran.co/online-dating-and-personal-data-discovering-okcupids-api/
 - http://www.wired.com/2014/01/how-to-hack-okcupid/all/
  - http://www.doctornerdlove.com/2014/01/how-to-hack-okcupid/

Overview of the project:
 - Scrape usernames every so often (every week? every day?) to find out about new OKCers
 - For all of the new OKCers, scrape their profile
 - Present these OKCers' info to me so I can decide who I'd like to reach out to.
 - Send those OKCers messages every so often
 - Alert me if any of those people respond
 - Keep track of stats so I can see if I should adjust my messages
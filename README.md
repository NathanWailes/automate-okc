# automate-okc

Overview of the project:
 - I should generalize this so that it isn't just about OKC, but about getting a date / gf. It should be a dashboard like Salesforce or Marketo or something. Then I can incorporate Tinder automation into it, and I can include the scraping of other websites to come up with date ideas.
 - Scrape usernames every so often (every week? every day?) to find out about new OKCers
 - For all of the new OKCers, scrape their profile
 - Present these OKCers' info to me so I can decide who I'd like to reach out to.
 - Send those OKCers messages every so often
 - Alert me if any of those people respond
 - Keep track of stats so I can see if I should adjust my messages

To Do:

general:
 - remove ghostdriver.log from the git repo
 - change the 'send' functions so you can call them both from the CLI and from other functions / modules

present_profiles:

scrape_usernames:
 - have some way to incorporate new usernames

scrape_profiles:
 - have some way to scrape profiles in parallel so it doesn't take so much time
 - Have some way of automatically re-scraping the site every night to get any new profiles that may have come online.
 - Make the program less likely to lose all the data when you quit it from the command line.
 - have some way of indicating which profiles were disabled when you came across them
 - add logging, so you know which profiles didn't have any info for them

scrape_messages:
 - Scrape your messages so the program knows who has responded to your messages.

send_message
 - have a list of different date ideas and corresponding invitations, and try sending each person all of the different invitations
 -- comedy club
 -- rock climbing gym
 -- EDM concert
 -- dancing (various venues)
 -- movie
 -- running event (5k), tough mudder, etc
 - it would be cool to try to use the person's profile to guess what kind of invitation to send first...




Done:
2015.08.28 - allow for a headless driver / screenless browser (which makes it easier to parallelize the scraping)
2015.08.21 - have some fast way of deciding if you want to contact a profile, so you don't have to keep using QuickMatch.
 - Scrape the profile pictures
 - have the scraper capable of working bit-by-bit (saving data as it goes) instead of needing to do everyone at once before it saves anything
 - See if there's some kind of API that could help you get information.





Related projects:
 - Ruby - https://github.com/trek/lonely_coder
 - JavaScript - http://hungtran.co/online-dating-and-personal-data-discovering-okcupids-api/
 - http://www.wired.com/2014/01/how-to-hack-okcupid/all/
  - http://www.doctornerdlove.com/2014/01/how-to-hack-okcupid/
 - [/r/ProgrammerHumor] Guy meets his girlfriend by writing JavaScript OKCupid spam bot
 - [/r/OkCupid] Feeling on the most efficient way to find out if the matches in your area are attracted to you?
 - [/r/javascript] And this piece of javascript is how I met my girlfriend through okCupid
 -- https://github.com/miguel-perez/OkCupidHack/blob/master/seekAndMessage.js



from scraper_1 import Bot

with Bot() as scraper:
    if scraper.readGoogleSheet(3):
        scraper.browser_init()
        scraper.main()
        scraper.updateGoogleSheet()
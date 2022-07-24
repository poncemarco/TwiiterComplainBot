from internet_speed_twitter_bot import InternetSpeedTwitterBot

selenium_path = "/home/marcoponce/Documents/Programas/Selenium/drivers/geckodriver-v0.31.0-linux64/geckodriver"


TWITTER_USER = "############"
TWITTER_PASSWORD = "#############"
PROMISED_UP = 10
PROMISED_DOWN = 150

bot = InternetSpeedTwitterBot(selenium_path)

bot.get_internet_speed()
if bot.down < PROMISED_DOWN & bot.up < PROMISED_UP:
    bot.tweet_at_provider(user=TWITTER_USER, password=TWITTER_PASSWORD)

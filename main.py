from PiCacher import MongoService, RedditService, JsonFileStore, PiCacher
import schedule
import time
from PiBlinkHandler import blink_led

def job(piCacher: PiCacher, timeFrame: str):
    try:
        piCacher.cache_posts(timeFrame)
    except Exception as e:
        print(f"Error with {piCacher.mongoService.name}: {e}")
        blink_led()
        while True:
            time.sleep(1)

if __name__ == '__main__':
    ip = 'localhost' 
    port = 27017
    db = 'testdb'

    coll_mod = 'TEST'

    mongoService = MongoService(ip, port, db, f'HourlyRedditStore{coll_mod}', 'HourConnection')
    day_mongoService = MongoService(ip, port, db, f'DailyRedditStore{coll_mod}', 'DayConnection')
    week_mongoService = MongoService(ip, port, db, f'WeeklyRedditStore{coll_mod}', 'WeekConnection')

    redditService = RedditService()
    
    hourJsonCache = JsonFileStore('hour_cache.json')
    dayJsonCache = JsonFileStore('day_cache.json')
    weekJsonCache = JsonFileStore('week_cache.json')

    hour_pc = PiCacher(mongoService, hourJsonCache, redditService)
    day_pc = PiCacher(day_mongoService, dayJsonCache, redditService)
    week_pc = PiCacher(week_mongoService, hourJsonCache, redditService)

    job(hour_pc, 'hour')
    job(day_pc, 'day')
    job(week_pc, 'week')

    schedule.every().hour.do(job, piCacher=hour_pc, timeFrame='hour')
    schedule.every().day.at("00:00").do(job, piCacher=day_pc, timeFrame='day')
    schedule.every().week.do(job, piCacher=week_pc, timeFrame='week')

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Script stopped by user")

from pybaseball import batting_stats_range
#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html_doc, 'html.parser')
from espn_api.baseball import League
from pybaseball import batting_stats
from pybaseball import pitching_stats

batting = batting_stats(2022)
pitching = pitching_stats(2022)

swid = '{DB2B01AE-27E1-45A1-AB01-AE27E1A5A170}'
espn_s2 = 'AEB%2FnoL1wdmiV3EpjNsrZYEG3q%2Bb4XJJVs%2BWgFuTsAuLziJ0obED6tcomtvR4WbTWTGcLO1AL9a%2Fnm96nJREwHaR7uuLrCsO5cJKHEItNRgz1FsvKcJHI9qawDTW5lQWy08MruA6bMfgzNu6XPAdS874YnMsc7VKY76jYs5CNnmqngcMAp3ROAd5kbO1wUhVvKIbrbh7zzOFDZVyMSaK%2FcnIT7c5XptG1sNnXjbUrckYOJ80jSCtlA7CN1Ew91gKVmcZTqswHb3LyAfKAUKpriVQ'
league = League(league_id=19937147, year=2022, espn_s2=espn_s2, swid=swid)
team = league.teams[4]
player = team.roster[1]
position = player.eligibleSlots

print(batting.Name)
#! python3

import pygame as pg
from os import path
import random, requests, time, calendar
from datetime import date
from newsapi.newsapi_client import NewsApiClient

# - Screen resolution & Colors
WIDTH = 1280
HEIGHT = 960
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# - Preferences
CITY = 'Centennial'
STATE = 'CO'
COUNTRY = 'us'
FONT_NAME = 'arial.ttf'
NEWS_SOURCE = 'ign'

# - API Keys
NEWS_KEY = 'paste-key-here'
WEATHER_KEY = 'paste-key-here'

def draw_text(self, text, font_name, size, color, x, y, align="nw"):
    pg.font.init()
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if align == 'nw':
        text_rect.topleft = (x, y)
    if align == 'ne':
        text_rect.topright = (x, y)
    if align == 'sw':
        text_rect.bottomleft = (x, y)
    if align == 'se':
        text_rect.bottomright = (x, y)
    if align == 'n':
        text_rect.midtop = (x, y)
    if align == 's':
        text_rect.midbottom = (x, y)
    if align == 'e':
        text_rect.midright = (x, y)
    if align == 'w':
        text_rect.midleft = (x, y)
    if align == 'center':
        text_rect.center = (x, y)
    self.screen.blit(text_surface, text_rect)

class MagicMirror:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.load_data()

    def load_data(self):
        self.home = path.dirname(__file__)
        font_dir = path.join(self.home, 'fonts')
        self.icon_dir = path.join(self.home, 'icons')
        self.news_font = path.join(font_dir, FONT_NAME)

    def new(self):
        self.get_news(NEWS_SOURCE)
        self.get_weather(CITY, STATE, COUNTRY)
        self.timer = 0
        self.run()

    def refresh(self):
        now = pg.time.get_ticks()
        if now - self.timer > 7000:
            self.timer = now
            self.get_news(NEWS_SOURCE)
            self.get_weather(CITY, STATE, COUNTRY)

    def dig_watch(self):
        self.today = date.today()
        self.weekday = calendar.day_name[self.today.weekday()]
        self.time_string = time.strftime('%H:%M:%S')
        if int(self.time_string[0:2]) < 12:
            self.time_string = str(time.strftime('%I:%M')) + ' AM'
        else:
            self.time_string = str(time.strftime('%I:%M')) + ' PM'

    def get_news(self, src):
        NEWS_API = NewsApiClient(api_key=NEWS_KEY)
        self.all_news = NEWS_API.get_top_headlines(sources=src)
        self.all_headlines = self.all_news
        self.snips = (self.all_headlines['articles'])
        rand_headline = random.randint(0, 9)
        self.headline = self.snips[rand_headline]

    def get_weather(self, city, state, country):
        self.city = city
        self.state = state
        self.temp_data = requests.get(
            'http://api.openweathermap.org/data/2.5/weather?q=' + self.city + ',' + country + '&units=imperial&APPID=' + WEATHER_KEY)
        # - Get Temperature
        self.json = self.temp_data.json()
        self.raw_temp = (self.json['main'])
        self.temp = str(self.raw_temp['temp'])[0:2]
        # - Get Conditions for Weather Icon
        self.tmp_cond = (self.json['weather'])
        self.condition = self.tmp_cond[0]
        self.icon_id = self.condition['id']
        if self.icon_id >= 200 and self.icon_id <= 232:
            self.cond_icon = '11d.png'
        if self.icon_id >= 300 and self.icon_id <= 321:
            self.cond_icon = '09d.png'
        if self.icon_id >= 500 and self.icon_id <= 531:
            self.cond_icon = '10d.png'
        if self.icon_id >= 600 and self.icon_id <= 622:
            self.cond_icon = '13d.png'
        if self.icon_id >= 701 and self.icon_id <= 781:
            self.cond_icon = '50d.png'
        if self.icon_id == 800:
            self.cond_icon = '01d.png'
        if self.icon_id >= 801:
            self.cond_icon = '02d.png'
        if self.icon_id >= 802:
            self.cond_icon = '03d.png'
        if self.icon_id >= 803 and self.icon_id <= 804:
            self.cond_icon = '04d.png'
        self.icon_img = pg.image.load(path.join(self.icon_dir, self.cond_icon)).convert_alpha()

    def draw(self):
        self.screen.fill(BLACK)
        # - Display Clock
        draw_text(self, self.weekday, self.news_font, 28, WHITE, WIDTH * .98, HEIGHT * .02, align='ne')
        draw_text(self, self.today.strftime('%b %d, %Y'), self.news_font, 20, WHITE, WIDTH * .98, HEIGHT * .05, align='ne')
        draw_text(self, self.time_string, self.news_font, 45, WHITE, WIDTH * .98, HEIGHT * .07, align='ne')
        # - Display News
        draw_text(self, self.headline['title'], self.news_font, 30, WHITE, WIDTH * .5, HEIGHT * .95, align='center')
        # - Display Weather Info
        draw_text(self, self.city + ', ' + self.state, self.news_font, 20, WHITE, WIDTH * .02, HEIGHT * .02, align='nw')
        draw_text(self, self.temp + '°', self.news_font, 90, WHITE, WIDTH * .02, HEIGHT * .04, align='nw')
        self.screen.blit(self.icon_img, (WIDTH * .13, HEIGHT * .04))
        pg.display.flip()

    def run(self):
        self.mirror = True
        while self.mirror:
            self.events()
            self.dig_watch()
            self.draw()
            self.refresh()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.mirror = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.mirror = False

mm = MagicMirror()
mm.new()
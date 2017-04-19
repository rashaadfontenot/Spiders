from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem


class SinglePlayerPage(BasePortiaSpider):
    name = "single-player-page"
    allowed_domains = [u'www.nba.com']
    start_urls = [u'http://www.nba.com/players']
    rules = [
        Rule(
            LinkExtractor(
                allow=(u'(?:www\\.nba\\.com/player).*'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [
        [
            Item(
                PortiaItem,
                None,
                u'player-detail',
                [
                    Field(
                        u'official_image',
                        u'.row > .small-12 > .nba-player-header__headshot > img::attr(src)',
                        []),
                    Field(
                        u'team',
                        u'.row > .small-12 > .nba-player-header__details > .nba-player-header__details-top > .nba-detail-header__team-logo *::text',
                        []),
                    Field(
                        u'jersey_number',
                        u'.row > .small-12 > .nba-player-header__details > .nba-player-header__details-top > .nba-player-header__jersey-number *::text',
                        []),
                    Field(
                        u'position',
                        u'.row > .small-12 > .nba-player-header__details > .nba-player-header__details-top > .nba-player-header__position *::text',
                        []),
                    Field(
                        u'first_name',
                        u'.row > .small-12 > .nba-player-header__details > .nba-player-header__details-bottom > .nba-player-header__first-name *::text',
                        []),
                    Field(
                        u'last_name',
                        u'.row > .small-12 > .nba-player-header__details > .nba-player-header__details-bottom > .nba-player-header__last-name *::text',
                        []),
                    Field(
                        u'height_ft',
                        u'.player-tabs-content > .is-active > .nba-player-vitals-video-wrapper > .nba-player-vitals > .nba-player-vitals__top > .nba-player-vitals__top-left > .nba-player-vitals__top-info-imperial > span:nth-child(1) *::text',
                        []),
                    Field(
                        u'height_in',
                        u'.player-tabs-content > .is-active > .nba-player-vitals-video-wrapper > .nba-player-vitals > .nba-player-vitals__top > .nba-player-vitals__top-left > .nba-player-vitals__top-info-imperial > span:nth-child(2) *::text',
                        []),
                    Field(
                        u'weight',
                        u'.player-tabs-content > .is-active > .nba-player-vitals-video-wrapper > .nba-player-vitals > .nba-player-vitals__top > .nba-player-vitals__top-right > .nba-player-vitals__top-info-imperial > span *::text',
                        []),
                    Field(
                        u'age',
                        u'.player-tabs-content > .is-active > .nba-player-vitals-video-wrapper > .nba-player-vitals > .nba-player-vitals__bottom > ul > li:nth-child(2) > .nba-player-vitals__bottom-info *::text',
                        []),
                    Field(
                        u'college',
                        u'.player-tabs-content > .is-active > .nba-player-vitals-video-wrapper > .nba-player-vitals > .nba-player-vitals__bottom > ul > li:nth-child(3) > .nba-player-vitals__bottom-info *::text',
                        [])])]]

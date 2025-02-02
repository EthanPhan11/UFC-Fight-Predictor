import scrapy

class StatScrapper(scrapy.Spider):
    name = 'fighter_stats'
    start_urls = ['http://www.ufcstats.com/statistics/fighters?char=a&page=all']
    
    
    def parse(self, response):
        for fighter in response.css('tr.b-statistics__table-row'):
            name = fighter.css('a.b-link.b-link_style_black::text').getall()
            height = fighter.css('td.b-statistics__table-col')[3].css('::text').get().replace('\"', ' ') if len(fighter.css('td.b-statistics__table-col')) > 3 else 'N/A'
            weight = fighter.css('td.b-statistics__table-col')[4].css('::text').get().replace('\"', ' ') if len(fighter.css('td.b-statistics__table-col')) > 4 else 'N/A'
            reach = fighter.css('td.b-statistics__table-col')[5].css('::text').get().replace('\"', ' ') if len(fighter.css('td.b-statistics__table-col')) > 5 else 'N/A'
            stance = fighter.css('td.b-statistics__table-col')[6].css('::text').get().replace('\"', ' ') if len(fighter.css('td.b-statistics__table-col')) > 6 else 'N/A'
            wins = fighter.css('td.b-statistics__table-col')[7].css('::text').get() if len(fighter.css('td.b-statistics__table-col')) > 7 else 'N/A'
            loss = fighter.css('td.b-statistics__table-col')[8].css('::text').get() if len(fighter.css('td.b-statistics__table-col')) > 8 else 'N/A'
            draw = fighter.css('td.b-statistics__table-col')[9].css('::text').get() if len(fighter.css('td.b-statistics__table-col')) > 9 else 'N/A'
            
            first_name = name[0] if len(name) > 0 else ' '
            last_name = name[1] if len(name) > 1 else ' '
            nickname = name[2] if len(name) > 2 else ' '
            
            
            yield {
                'first_name': first_name.strip(),
                'last_name': last_name.strip(),
                'nickname': nickname.strip(),
                'height': height.strip(),
                'weight': weight.strip(),
                'reach': reach.strip(),
                'stance': stance.strip(),
                'wins': wins.strip(),
                'loss': loss.strip(),
                'draw': draw.strip(),
            }
    
    #def link_parse(self, response):
        #for link in response.css('a.b-link::attr(href)'):
            #yield response.follow(link.get(), callback=self.parse_categories)

    #for fighter in response.css('div.b-list__info-box-left.clearfix'):
            #SigSPM = fighter.xpath('.//li[contains(@class, "b-list__box-list-item")]/i[contains(@class, "b-list__box-item-title_font_lowercase")]/following-sibling::text()').get().strip()
        
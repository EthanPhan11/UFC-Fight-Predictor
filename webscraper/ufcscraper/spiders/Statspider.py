import scrapy

class StatScrapper(scrapy.Spider):
    name = 'fighter_stats'
    start_urls = [
        'http://www.ufcstats.com/statistics/fighters?char=a&page=all',
        'http://www.ufcstats.com/statistics/fighters?char=b&page=all',
        'http://www.ufcstats.com/statistics/fighters?char=c&page=all',
        'http://www.ufcstats.com/statistics/fighters?char=d&page=all',
        'http://www.ufcstats.com/statistics/fighters?char=e&page=all',
        'http://www.ufcstats.com/statistics/fighters?char=f&page=all',
        'http://www.ufcstats.com/statistics/fighters?char=g&page=all',
        'http://www.ufcstats.com/statistics/fighters?char=h&page=all',
        'http://www.ufcstats.com/statistics/fighters?char=i&page=all',
        'http://www.ufcstats.com/statistics/fighters?char=j&page=all',
        'http://www.ufcstats.com/statistics/fighters?char=k&page=all',
        'http://www.ufcstats.com/statistics/fighters?char=l&page=all',
        'http://www.ufcstats.com/statistics/fighters?char=m&page=all',
        'http://www.ufcstats.com/statistics/fighters?char=n&page=all',
        'http://www.ufcstats.com/statistics/fighters?char=o&page=all',
        'http://www.ufcstats.com/statistics/fighters?char=p&page=all',
        'http://www.ufcstats.com/statistics/fighters?char=q&page=all',
        'http://www.ufcstats.com/statistics/fighters?char=r&page=all',
        'http://www.ufcstats.com/statistics/fighters?char=s&page=all',
        'http://www.ufcstats.com/statistics/fighters?char=t&page=all',
        'http://www.ufcstats.com/statistics/fighters?char=u&page=all',
        'http://www.ufcstats.com/statistics/fighters?char=v&page=all',
        'http://www.ufcstats.com/statistics/fighters?char=w&page=all',
        'http://www.ufcstats.com/statistics/fighters?char=x&page=all',
        'http://www.ufcstats.com/statistics/fighters?char=y&page=all',
        'http://www.ufcstats.com/statistics/fighters?char=z&page=all',
        ]
    
    def parse(self, response):
        for link in response.css('a.b-link.b-link_style_black::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_fighter)
            
    def parse_fighter(self, response): 
        name = response.css('span.b-content__title-highlight::text').get()
        nickname = response.css('p.b-content__Nickname::text').get()
        record = response.css('span.b-content__title-record::text').get().replace('Record:', '')
        height = response.xpath('//li[contains(@class, "b-list__box-list-item")]/i[contains(@class, "b-list__box-item-title") and contains(text(), "Height:")]/following-sibling::text()').get().replace("\"", ' ').replace("'", ' ')
        weight = response.xpath('//li[contains(@class, "b-list__box-list-item")]/i[contains(@class, "b-list__box-item-title") and contains(text(), "Weight:")]/following-sibling::text()').get()
        reach = response.xpath('//li[contains(@class, "b-list__box-list-item")]/i[contains(@class, "b-list__box-item-title") and contains(text(), "Reach:")]/following-sibling::text()').get().replace("\"", ' ')
        stance = response.xpath('//li[contains(@class, "b-list__box-list-item")]/i[contains(@class, "b-list__box-item-title") and contains(text(), "STANCE:")]/following-sibling::text()').get()
        dob = response.xpath('//li[contains(@class, "b-list__box-list-item")]/i[contains(@class, "b-list__box-item-title") and contains(text(), "DOB:")]/following-sibling::text()').get()
        SigSPM = response.xpath('//li[contains(@class, "b-list__box-list-item")]/i[contains(@class, "b-list__box-item-title") and contains(text(), "SLpM:")]/following-sibling::text()').get()
        StrAcc = response.xpath('//li[contains(@class, "b-list__box-list-item")]/i[contains(@class, "b-list__box-item-title") and contains(text(), "Str. Acc.:")]/following-sibling::text()').get()
        SApM = response.xpath('//li[contains(@class, "b-list__box-list-item")]/i[contains(@class, "b-list__box-item-title") and contains(text(), "SApM:")]/following-sibling::text()').get()
        StrDef = response.xpath('//li[contains(@class, "b-list__box-list-item")]/i[contains(@class, "b-list__box-item-title") and contains(text(), "Str. Def:")]/following-sibling::text()').get()
        TdAvg = response.xpath('//li[contains(@class, "b-list__box-list-item")]/i[contains(@class, "b-list__box-item-title") and contains(text(), "TD Avg.:")]/following-sibling::text()').get() 
        TdAcc = response.xpath('//li[contains(@class, "b-list__box-list-item")]/i[contains(@class, "b-list__box-item-title") and contains(text(), "TD Acc.:")]/following-sibling::text()').get() 
        TdDef = response.xpath('//li[contains(@class, "b-list__box-list-item")]/i[contains(@class, "b-list__box-item-title") and contains(text(), "TD Def.:")]/following-sibling::text()').get() 
        SubAvg = response.xpath('//li[contains(@class, "b-list__box-list-item")]/i[contains(@class, "b-list__box-item-title") and contains(text(), "Sub. Avg.:")]/following-sibling::text()').get() 
        RecFight = response.css('i.b-flag__text::text').get()
        
        
        yield {
            'name': name.split(),
            'nickname': nickname.strip(),
            'record': record.split() if record else 'Not Avaliable',
            'height': height.strip() if height else 'Not Avaliable',
            'weight': weight.strip() if weight else 'Not Avaliable',
            'reach': reach.strip() if reach else 'Not Avaliable',
            'stance': stance.strip() if stance != "" else 'Not Avaliable',
            'DOB': dob.strip() if dob else 'Not Avaliable',
            'significant strikes per min': SigSPM.strip() if SigSPM else 'Not Avaliable',
            'striking accuracy': StrAcc.strip() if StrAcc else 'Not Avaliable',
            'strikes absorbed per min': SApM.strip() if SApM else 'Not Avaliable',
            'strike defense': StrDef.strip() if StrDef else 'Not Avaliable',
            'takedown average': TdAvg.strip() if TdAvg else 'Not Avaliable',
            'takedown accuracy': TdAcc.strip() if TdAcc else 'Not Avaliable',
            'takedown defense': TdDef.strip() if TdDef else 'Not Avaliable',
            'submission average': SubAvg.strip() if SubAvg else 'Not Avaliable',
            'most recent fight': RecFight.strip(),        
        }
        
    

   
            
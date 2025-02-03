import scrapy


class StatScrapper(scrapy.Spider):
    # call this name to start a web crawl
    name = 'fighter_stats'
    # searches through every single fighter page alphabeticaly
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
    
   # this function parses through all of the main pages and opens up the indivdual fighter page
    def parse(self, response):
        for link in response.css('a.b-link.b-link_style_black::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_fighter)
            
   # parsing data from individual fighter
    def parse_fighter(self, response): 
        # All data classifications that dont require any additional functions
        name = response.css(
            'span.b-content__title-highlight::text'
        ).get()
        nickname = response.css(
            'p.b-content__Nickname::text'
        ).get()
        record = response.css(
            'span.b-content__title-record::text'
        ).get().replace('Record:', '').strip()
        height = response.xpath(
            '//li[contains(@class, "b-list__box-list-item")]/i[contains(text(), "Height:")]/following-sibling::text()'
        ).get().replace('"', '')
        weight = response.xpath(
            '//li[contains(@class, "b-list__box-list-item")]/i[contains(text(), "Weight:")]/following-sibling::text()'
        ).get().replace('.', '')
        reach = response.xpath(
            '//li[contains(@class, "b-list__box-list-item")]/i[contains(text(), "Reach:")]/following-sibling::text()'
        ).get().replace('"', '')
        stance = response.xpath(
            '//li[contains(@class, "b-list__box-list-item")]/i[contains(text(), "STANCE:")]/following-sibling::text()'
        ).get()
        dob = response.xpath(
            '//li[contains(@class, "b-list__box-list-item")]/i[contains(text(), "DOB:")]/following-sibling::text()'
        ).get().replace(',', '')
        SigSPM = response.xpath(
            '//li[contains(@class, "b-list__box-list-item")]/i[contains(text(), "SLpM:")]/following-sibling::text()'
        ).get()
        StrAcc = response.xpath(
            '//li[contains(@class, "b-list__box-list-item")]/i[contains(text(), "Str. Acc.:")]/following-sibling::text()'
        ).get()
        SApM = response.xpath(
            '//li[contains(@class, "b-list__box-list-item")]/i[contains(text(), "SApM:")]/following-sibling::text()'
        ).get()
        StrDef = response.xpath(
            '//li[contains(@class, "b-list__box-list-item")]/i[contains(text(), "Str. Def:")]/following-sibling::text()'
        ).get()
        TdAvg = response.xpath(
            '//li[contains(@class, "b-list__box-list-item")]/i[contains(text(), "TD Avg.:")]/following-sibling::text()'
        ).get() 
        TdAcc = response.xpath(
            '//li[contains(@class, "b-list__box-list-item")]/i[contains(text(), "TD Acc.:")]/following-sibling::text()'
        ).get() 
        TdDef = response.xpath(
            '//li[contains(@class, "b-list__box-list-item")]/i[contains(text(), "TD Def.:")]/following-sibling::text()'
        ).get() 
        SubAvg = response.xpath(
            '//li[contains(@class, "b-list__box-list-item")]/i[contains(text(), "Sub. Avg.:")]/following-sibling::text()'
        ).get() 
        
        
        # Here is where all data classifacations that require additional functions are grouped
        
        #                     | | | | | | | | | | | | | | | | | |                                                                               
        #                     | | | | | | | | | | | | | | | | | |  
        #                     | | | | | | | | | | | | | | | | | |
        #                     | | | | | | | | | | | | | | | | | | 
        #                     V V V V V V V V V V V V V V V V V V 
        
        # Displays if the match was won, lost, draw, or no contest
        RecFight = response.css(
            'td:nth-child(1) i.b-flag__text::text'
        ).get()
        
        # Handles cases where if the fighter has an upcoming fight, it will skip the row that displays it and move on to the next row
        if RecFight == 'next':
            RecFight = response.css(
                'tr:nth-child(3) td:nth-child(1) i.b-flag__text::text'
            ) .get()
         
        
        # Extracts every single text node from the 7th cell
        all_text = response.css(
            'table.b-fight-details__table tr:nth-child(2) td:nth-child(7) p *::text'
        ).getall()                                                                                            
        # gets rid of unessecary whitespace and characters, then takes the last text in the cell
        RecFightDate = [t.strip() for t in all_text if t.strip()]
        RecFightDate = RecFightDate[-1] if RecFightDate else "--"
        
        
        # stores every individual row in a variable      
        row = response.css('tr.b-fight-details__table-row.b-fight-details__table-row__hover.js-fight-details-click')

        # Benchmark values
        KOwin = 0
        SubWin = 0
        UDecWin = 0
        SDecWin = 0
        
        # Iterates through every single fight, then stores each method of victory in its respective variable
        for fight in row:
            result = fight.css('td:nth-child(1) i.b-flag__text::text').get()
            if result:
                result = result.strip()
                if result.lower() == 'win':
                    method = fight.css('td:nth-child(8) p.b-fight-details__table-text::text').get()
                    if method:
                        method = method.strip()
                        if 'KO/TKO' in method:
                            KOwin += 1
                        elif 'SUB' in method:
                            SubWin += 1
                        elif 'U-DEC' in method:
                            UDecWin += 1
                        elif 'S-DEC' in method:
                            SDecWin += 1

        
        # Displays if a fighter is currently on a winstreak (3 fights won in a row)
        # Similar logic for collecting win methods
        CurrWStreak = 0
        for fight in row:
            result = fight.css('td:nth-child(1) i.b-flag__text::text').get()
            if result:
                result = result.strip()
                if result.lower() == 'win':
                    CurrWStreak += 1
                elif result.lower() == 'loss' or 'draw':
                    break
        
        # Will not display number if fighter has 2 or less wins in a row        
        if CurrWStreak < 3:
            CurrWStreak = "--"            
                          

        # Breaks up the fighter record into wins, losses, or draw and no contest
        wins, losses, drawsandNC = '--', '--', '--'
        if record:
            record_parts = record.split('-')
            wins = record_parts[0].strip() if len(record_parts) > 0 else '--'
            losses = record_parts[1].strip() if len(record_parts) > 1 else '--'
            drawsandNC = record_parts[2].strip() if len(record_parts) > 2 else '--'
        
        
        # Breaks up name into first and last names
        first_name, last_name = '--', '--'
        if name:
            name_parts = name.strip().split(' ')
            first_name = name_parts[0] if len(name_parts) > 0 else '--'
            last_name = ' '.join(name_parts[1:]).strip() if len(name_parts) > 1 else '--'
            
        
        # prints data onto a csv file
        yield {
            'first name': first_name if first_name else '--',
            'last name': last_name if last_name else '--',
            'nickname': nickname.strip() if nickname and not nickname.isspace() else '--',
            'wins': wins,
            'losses': losses,
            'draws and no contest': drawsandNC,
            'current winstreak': CurrWStreak,
            'KO wins': KOwin,
            'Submission wins': SubWin,
            'U-DEC wins': UDecWin,
            'S-DEC wins': SDecWin,
            'height': height.strip() if height else '--',
            'weight': weight.strip() if weight else '--',
            'reach': reach.strip() if reach else '--',
            'stance': stance.strip() if stance and not stance.isspace() else '--',
            'DOB': dob.strip() if dob else '--',
            'significant strikes per min': SigSPM.strip() if SigSPM else '--',
            'striking accuracy': StrAcc.strip() if StrAcc else '--',
            'strikes absorbed per min': SApM.strip() if SApM else '--',
            'strike defense': StrDef.strip() if StrDef else '--',
            'takedown average': TdAvg.strip() if TdAvg else '--',
            'takedown accuracy': TdAcc.strip() if TdAcc else '--',
            'takedown defense': TdDef.strip() if TdDef else '--',
            'submission average': SubAvg.strip() if SubAvg else '--',
            'most recent fight': RecFight.strip() if RecFight else '--',
            'recent fight date': RecFightDate,        
        }
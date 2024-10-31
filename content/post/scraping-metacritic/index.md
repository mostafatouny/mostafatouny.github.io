---
title: "Scraping Data of 2019 Best PS4 Games on Metacritic"
subtitle: Mining the new oil
summary: Mining the new oil
date: "2020-02-01T00:17:00Z"
cover:
    image: "featured.png"
---

### Introduction
The post you are currently reading shall demonstrate how far our data published on social media is being heavily gathered for data analysis. The demonstration holds as a beginner kid like me is going to scrape data, i.e store data on a file, after only two weeks of learning. Not only the code I built works solely on the website I shall be presenting but rather on any website! However, It is not robust enough to rely upon except for simple cases.

___

### Contents
- [Introduction](#introduction)
- [Motivation](#motivation)
- [Code on Github](#code-on-github)
- [How The Code Works?](#how-the-code-works)

___

### Motivation
Machine learning, The prettiest-looking AI nowadays, does not work without data. In fact, one of the fundamental pillars of AI's success is the availability of right data. Unfortunately, industries do not like to share them. Most probably, due to the sensitivity of competition, as rivals would always favor to stay ahead of their competitors. So, what do you do if you needed data for research, business, or even for a hobbyist-project but could not find it? Buying data costs you too much, and not everyone has tight relationships with industries whose platforms generate desired data. Scraping websites, i.e gathering data on web into a readable format by the computer, is a highly recommended skill for data analysts.  

### Code on Github
[Here](https://github.com/mostafatouny/data-scraper) is the scraper I built. Even-though its design is not restricted to a specific website, I only test it on metacritic. The code contains an example on scraping [metacritic's 2019 best PS4 games](https://www.metacritic.com/browse/games/score/metascore/year/ps4/filtered?year_selected=2019).

### How The Code Works?
The following is a brief illustration of metacritic's example on github's repo. If you checked out metacritic's link, you would see a list of games, each with its own score and release date. First, Let's take a look on what your machine actually reads in order to render that page.

```
<ol class="list_products list_product_condensed"
  <li class="product game_product">
    ...
  </li>
  <li class="product game_product">
    ...
  </li>
  <li class="product game_product">
    ..
</ol>
```
each `li` tag corresponds to some game on the list. While `ol` tag corresponds to a wrapper of all games on the list. Here is a sample of what is inside each game's tag.

```
<li class="product game_product">
  <div class="product_wrap">
    <div class="basic_stat product_title">
      <a href="/game/playstation-4/nier-automata---game-of-the-yorha-edition"
        NieR: Automata - Game of the YoRHa Edition
      </a>
    </div>
  </div>
</li>
```

Now, How does the program scrapes data of websites? There are three steps to get the code working, (I) enter the link which contains data intended to be scraped,
```
mainURL = "https://www.metacritic.com"
subURL = "/browse/games/score/metascore/year/ps4/filtered?year_selected=2019"
```

(II) specify the tags' path from root up to the tag which wraps all games list,
```
listNodeSequence = tagSequence.tagSequence([('ol', {"class":"list_products list_product_condensed"}), ('div', {"class":"product_condensed"}), ('div', {"class": "body_wrap" ..
```

then (III) for each data desired to be scraped, alike game name, game score, game release date, specify the path from the game's tag up to that data. make sure not to type any game-specific data like the href of _nier: automata_
```
columns_paths = tagsPaths.tagsPaths(
    [
    ('title', [('a',), ('div', {"class":"basic_stat product_title"}), ('div', {"class":"product_wrap"})], -1),

    ('critic_rating', [('div',), ('div', {"class":"product_score"}), ('div', {"class":"product_wrap"})], -1),

    ('user_rating', [('span', {"class":"textscore"}), ('li', {"class":"product_avguserscore"}), ('ul',), ('div', {"class":"condensed_stats"}), ('div', {"class":"product_wrap"})], -1),

    ('release_date', [('span', {"class":"data"}), ('li', {"class":"release_date"}), ('ul',), ('div', {"class":"condensed_stats"}), ('div', {"class":"product_wrap"})], -1)
    ]
    )
```

after running the program, you should obtain a list of containing all games, not just one of them.

```
[
	{
		"critic_rating": "91",
		"release_date": "Jul  2, 2019",
		"title": "Final Fantasy XIV: Shadowbringers",
		"user_rating": "8.3"
	},
	{
		"critic_rating": "91",
		"release_date": "Feb 26, 2019",
		"title": "NieR: Automata - Game of the YoRHa Edition",
		"user_rating": "8.4"
	},
  ...
```
The remaining of the code sample are available in the github's repo. They are named _metacritic2019_main.py_, _metacritic2019_functions.py._ and _metacritic2019_data.json_

that's it! for any website, just provide the link which contains data, and the two paths, one from root up to wrapper tag, and the other from each record's tag up to desired data.

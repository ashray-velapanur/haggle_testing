class _HaggleCategory():
    def __init__(self, name, max_checkins, description=None):
        self.name = name
        self.max_checkins = max_checkins
        self.description = name if description is None else description

HAGGLE_CUISINES = [BBQ,
                   Bar,
                   Burgers,
                   Cafe,
                   Chinese,
                   Dessert,
                   French,
                   Indian,
                   Italian,
                   Mexican,
                   MiddleEastern,
                   Pizza,
                   Seafood,
                   Steakhouse,
                   Japanese,
                   Vegetarian,
                   SandwichSalad,
                   American,
                   Other] = [_HaggleCategory("BBQ",60.0,"BBQ Places"),
                                  _HaggleCategory("Bar",48.0,"Bars"),
                                  _HaggleCategory("Burgers",72.0,"Burger Joints"),
                                  _HaggleCategory("Cafe",60.0, "Cafes"),
                                  _HaggleCategory("Chinese",120.0, "Chinese Places"),
                                  _HaggleCategory("Dessert",60.0, "Dessert Places"),
                                  _HaggleCategory("French",48.0, "French Restaurants"),
                                  _HaggleCategory("Indian",60.0, "Indian Restaurants"),
                                  _HaggleCategory("Italian",60.0, "Italian Restaurants"),
                                  _HaggleCategory("Mexican",60.0, "Mexican Restaurants"),
                                  _HaggleCategory("Middle Eastern",60.0, "MiddleEastern Restaurants"),
                                  _HaggleCategory("Pizza",48.0, "Pizza places"),
                                  _HaggleCategory("Seafood",96.0, "Seafood Places"),
                                  _HaggleCategory("Steakhouse",60.0, "Steakhouses"),
                                  _HaggleCategory("Japanese",48.0, "Japanese Restaurants"),
                                  _HaggleCategory("Vegetarian",96.0, "Vegetarian Places"),
                                  _HaggleCategory("Sandwiches & Salads",60.0, "Sandwiches & Salad Places"),
                                  _HaggleCategory("American",96.0, "American Restaurants"),
                                  _HaggleCategory("Other",52.0, "")]

_bar_empty = {'category': Bar,
              'tags': []}

HARMONIZED_CATEGORIES = {
"bar & grill":{'category':Bar, 'tags':['bar & grill']},
"barbecue restaurant":{'category':BBQ, 'tags':['barbecue restaurant']},
"taiwanese restaurant":{'category':Other, 'tags':['taiwanese restaurant']},
"cocktail bar":{'category':Bar, 'tags':['cocktail bar']},
"sports bar":{'category':Bar, 'tags':['sports bar']},
"lounge":{'category':Bar, 'tags':['lounge']},
"sake bar":{'category':Bar, 'tags':['sake bar', 'japanese', 'sushi']},
"gastropub":{'category':Bar, 'tags':['gastropub']},
"vineyard":{'category':Bar, 'tags':['vineyard']},
"karaoke bar":{'category':Bar, 'tags':['karaoke bar']},
"wine shop":{'category':Bar, 'tags':['wine shop']},
"night club":{'category':Bar, 'tags':['night club']},
"piano bar":{'category':Bar, 'tags':['piano bar']},
"beer garden":{'category':Bar, 'tags':['beer garden']},
"hotel bar":{'category':Bar, 'tags':['hotel bar']},
"dive bar":{'category':Bar, 'tags':['dive bar']},
"wine bar":{'category':Bar, 'tags':['wine bar']},
"pub":{'category':Bar, 'tags':['pub']},
"jazz club":{'category':Bar, 'tags':['jazz club']},
"lounges":{'category':Bar, 'tags':['lounges']},
"hookah bar":{'category':Bar, 'tags':['hookah bar']},
"whisky bar":{'category':Bar, 'tags':['whisky bar']},
"bar":{'category':Bar, 'tags':['bar']},
"winery/vineyard":{'category':Bar, 'tags':['winery/vineyard']},
"nightclub":{'category':Bar, 'tags':['nightclub']},
"gay bar":{'category':Bar, 'tags':['gay bar']},
"wineries":{'category':Bar, 'tags':['wineries']},
"winery":{'category':Bar, 'tags':['winery']},
"dumpling restaurant":{'category':Chinese, 'tags':['dumpling restaurant', 'chinese', 'asia']},
"dim sum restaurant":{'category':Chinese, 'tags':['dim sum restaurant', 'chinese', 'asia']},
"chinese restaurant":{'category':Chinese, 'tags':['chinese restaurant',  'asia']},
"mongolian restaurant":{'category':Chinese, 'tags':['mongolian restaurant', 'asia']},
"ramen /  noodle house":{'category':Chinese, 'tags':['ramen /  noodle house']},
"sandwich shop":{'category':SandwichSalad, 'tags':['sandwich shop']},
"sandwich place":{'category':SandwichSalad, 'tags':['sandwich place']},
"salad place":{'category':SandwichSalad, 'tags':['salad place']},
"salad":{'category':SandwichSalad, 'tags':['salad']},
"salad shop":{'category':SandwichSalad, 'tags':['salad shop']},
"cupcake shop":{'category':Dessert, 'tags':['cupcake shop']},
"ice cream parlor":{'category':Dessert, 'tags':['ice cream parlor']},
"dessert shop":{'category':Dessert, 'tags':['dessert shop']},
"donut shop":{'category':Dessert, 'tags':['donut shop']},
"ice cream shop":{'category':Dessert, 'tags':['ice cream shop']},
"vegetarian/vegan restaurant":{'category':Vegetarian, 'tags':['vegetarian/vegan restaurant']},
"vegetarian / vegan restaurant":{'category':Vegetarian, 'tags':['vegetarian / vegan restaurant']},
"vegetarian & vegan restaurant":{'category':Vegetarian, 'tags':['vegetarian & vegan restaurant']},
"japanese restaurant":{'category':Japanese, 'tags':['japanese restaurant', 'asia', 'sushi']},
"sushi restaurant":{'category':Japanese, 'tags':['sushi restaurant', 'japan', 'asia']},
"french restaurant":{'category':French, 'tags':['french restaurant', 'europe']},
"pizza place":{'category':Pizza, 'tags':['pizza place']},
"burger restaurant":{'category':Burgers, 'tags':['burger restaurant']},
"burger joint":{'category':Burgers, 'tags':['burger joint']},
"wings joint":{'category':American, 'tags':['wings joint']},
"american restaurant":{'category':American, 'tags':['american restaurant']},
"fast food restaurant":{'category':American, 'tags':['fast food restaurant']},
"new american restaurant":{'category':American, 'tags':['new american restaurant']},
"cajun / creole restaurant":{'category':American, 'tags':['cajun / creole restaurant']},
"fried chicken joint":{'category':American, 'tags':['fried chicken joint']},
"hot dog joint":{'category':American, 'tags':['hot dog joint']},
"snack place":{'category':American, 'tags':['snack place']},
"mac & cheese joint":{'category':American, 'tags':['mac & cheese joint']},
"greek restaurant":{'category':Other, 'tags':['greek restaurant', 'europe', 'Mediterranean']},
"local business":{'category':Other, 'tags':['local business']},
"caribbean restaurant":{'category':Other, 'tags':['caribbean restaurant']},
"bagel shop":{'category':Other, 'tags':['bagel shop']},
"australian restaurant":{'category':Other, 'tags':['australian restaurant']},
"southern / soul food restaurant":{'category':Other, 'tags':['southern / soul food restaurant']},
"eastern european restaurant":{'category':Other, 'tags':['eastern european restaurant']},
"paella restaurant":{'category':Other, 'tags':['paella restaurant']},
"cuban restaurant":{'category':Other, 'tags':['cuban restaurant']},
"food & grocery":{'category':Other, 'tags':['food & grocery']},
"food truck":{'category':Other, 'tags':['food truck']},
"food stand":{'category':Other, 'tags':['food stand']},
"tapas restaurant":{'category':Other, 'tags':['tapas restaurant']},
"food & restaurant":{'category':Other, 'tags':['food & restaurant']},
"filipino restaurant":{'category':Other, 'tags':['filipino restaurant']},
"juice bar":{'category':Other, 'tags':['juice bar']},
"malaysian restaurant":{'category':Other, 'tags':['malaysian restaurant']},
"food court":{'category':Other, 'tags':['food court']},
"portuguese restaurant":{'category':Other, 'tags':['portuguese restaurant']},
"soup place":{'category':Other, 'tags':['soup place']},
"food/grocery":{'category':Other, 'tags':['food/grocery']},
"gourmet shop":{'category':Other, 'tags':['gourmet shop']},
"brazilian restaurant":{'category':Other, 'tags':['brazilian restaurant']},
"food/beverages":{'category':Other, 'tags':['food/beverages']},
"gluten-free restaurant":{'category':Other, 'tags':['gluten-free restaurant']},
"vietnamese restaurant":{'category':Other, 'tags':['vietnamese restaurant']},
"peruvian restaurant":{'category':Other, 'tags':['peruvian restaurant']},
"deli / bodega":{'category':Other, 'tags':['deli / bodega']},
"german restaurant":{'category':Other, 'tags':['german restaurant', 'europe']},
"arepa restaurant":{'category':Other, 'tags':['arepa restaurant']},
"food & drink shop":{'category':Other, 'tags':['food & drink shop']},
"food":{'category':Other, 'tags':['food']},
"argentinian restaurant":{'category':Other, 'tags':['argentinian restaurant']},
"hotel":{'category':Other, 'tags':['hotel']},
"african restaurant":{'category':Other, 'tags':['african restaurant']},
"thai restaurant":{'category':Other, 'tags':['thai restaurant']},
"indonesian restaurant":{'category':Other, 'tags':['indonesian restaurant']},
"swiss restaurant":{'category':Other, 'tags':['swiss restaurant']},
"molecular gastronomy restaurant":{'category':Other, 'tags':['molecular gastronomy restaurant']},
"kosher restaurant":{'category':Other, 'tags':['kosher restaurant']},
"south american restaurant":{'category':Other, 'tags':['south american restaurant']},
"bakeries":{'category':Other, 'tags':['bakeries']},
"buffet restaurant":{'category':Other, 'tags':['buffet restaurant']},
"diner":{'category':Other, 'tags':['diner']},
"fish & chips shop":{'category':Other, 'tags':['fish & chips shop']},
"restaurant":{'category':Other, 'tags':['restaurant']},
"korean restaurant":{'category':Other, 'tags':['korean restaurant']},
"latin american restaurant":{'category':Other, 'tags':['latin american restaurant']},
"breakfast & brunch restaurant":{'category':Other, 'tags':['breakfast & brunch restaurant']},
"spanish restaurant":{'category':Other, 'tags':['spanish restaurant']},
"chicken restaurant":{'category':Other, 'tags':['chicken restaurant']},
"bakery":{'category':Other, 'tags':['bakery']},
"moroccan restaurant":{'category':Other, 'tags':['moroccan restaurant']},
"family style restaurant":{'category':Other, 'tags':['family style restaurant']},
"cheese shop":{'category':Other, 'tags':['cheese shop']},
"scandinavian restaurant":{'category':Other, 'tags':['scandinavian restaurant']},
"food/beverage":{'category':Other, 'tags':['food/beverage']},
"steakhouse":{'category':Steakhouse, 'tags':['steakhouse']},
"indian restaurant":{'category':Indian, 'tags':['indian restaurant']},
"mediterranean restaurant":{'category':MiddleEastern, 'tags':['mediterranean restaurant']},
"falafel restaurant":{'category':MiddleEastern, 'tags':['falafel restaurant']},
"afghan restaurant":{'category':MiddleEastern, 'tags':['afghan restaurant']},
"middle eastern restaurant":{'category':MiddleEastern, 'tags':['middle eastern restaurant']},
"ethiopian restaurant":{'category':MiddleEastern, 'tags':['ethiopian restaurant']},
"turkish restaurant":{'category':MiddleEastern, 'tags':['turkish restaurant']},
"burrito place":{'category':Mexican, 'tags':['burrito place']},
"taco place":{'category':Mexican, 'tags':['taco place']},
"mexican restaurant":{'category':Mexican, 'tags':['mexican restaurant']},
"cafeteria":{'category':Cafe, 'tags':['cafeteria']},
"coffee shop":{'category':Cafe, 'tags':['coffee shop']},
"college cafeteria":{'category':Cafe, 'tags':['college cafeteria']},
"cafe":{'category':Cafe, 'tags':['cafe']},
"breakfast spot":{'category':Cafe, 'tags':['breakfast spot', 'Deli']},
"restaurant/cafe":{'category':Cafe, 'tags':['restaurant/cafe']},
u"caf\xe9":{'category':Cafe, 'tags':[u'caf\xe9', 'cafe']},
"tea room":{'category':Cafe, 'tags':['tea room']},
"seafood restaurant":{'category':Seafood, 'tags':['seafood restaurant']},
"bbq joint":{'category':BBQ, 'tags':['bbq joint']},
"italian restaurant":{'category':Italian, 'tags':['italian restaurant', 'europe']},
"inn":{'category':Other, 'tags':['inn']}
}

BLACK_LIST = set([
    "accessories store",
    "airport",
    "airport gate",
    "airport lounge",
    "airport terminal",
    "airport tram",
    "airports",
    "arcade",
    "art gallery",
    "arts & entertainment",
    "art & entertainment",
    "art museum",
    "bands & musicians",
    "band & musician",
    "bank",
    "basketball stadium",
    "beach",
    "beach resort",
    "beach",
    "bike shop",
    "boats or ferries",
    "boat or ferry",
    "book store",
    "bookstore",
    "bowling alley",
    "breweries",
    "brewery",
    "bridge",
    "building",
    "bus line",
    "bus station",
    "business center",
    "business service",
    "butcher",
    "camera store",
    "campground",
    "church",
    "city",
    "clothing store",
    "college academic building",
    "college arts building",
    "college auditorium",
    "college residence hall",
    "college stadium",
    "college/university",
    "community & government",
    "concert hall",
    "concert venue",
    "convention center",
    "corporate office",
    "cosmetics shop",
    "coworking space",
    "dance studio",
    "department store",
    "distillery",
    "drugstores / pharmacies",
    "drugstore / pharmacy",
    "education",
    "educational camp",
    "educational research",
    "electronics store",
    "embassies / consulate",
    "entertainment service",
    "episcopal church",
    "event space",
    "ferry/boat",
    "field",
    "flea market",
    "farmers market",
    "fish market",
    "football stadium",
    "franchising service",
    "furniture / home store",
    "gas stations / garages",
    "gas station / garage",
    "general colleges & universities",
    "general college & university",
    "general entertainment",
    "general travel",
    "golf course",
    "government building",
    "grocery store",
    "gym",
    "gym or fitness center",
    "harbor / marina",
    "high school",
    "hiking trail",
    "historic site",
    "historical place",
    "history museum",
    "home (private)",
    "hospital",
    "hostel",
    "hot spring",
    "housing development",
    "indie movie theater",
    "indie theater",
    "internet cafe",
    "jewelry store",
    "jewelry supplier",
    "landmark",
    "library",
    "light rail",
    "liquor store",
    "lodging",
    "mall",
    "market",
    "medical & health",
    "monument / landmark",
    "motel",
    "movie theater",
    "movie theatre",
    "multiplex",
    "museum",
    "music store",
    "music venues",
    "national park",
    "neighborhood",
    "office",
    "opera house",
    "other great outdoor",
    "outdoor",
    "outdoor & recreation",
    "park",
    "parking",
    "performing arts venue",
    "plaza",
    "professional & other place",
    "professional service",
    "public place & attraction",
    "racetrack",
    "real estate service",
    "recreation center",
    "rental car location",
    "residence & other",
    "residential building (apartment / condo)",
    "rest area",
    "river",
    "road",
    "salon / barbershop",
    "scenic lookout",
    "school",
    "shoe store",
    "shopping & retail",
    "shopping district",
    "shopping mall",
    "skating rink",
    "ski area",
    "soccer stadium",
    "spa / massage",
    "speakeasies",
    "speakeasy",
    "sporting goods shop",
    "sports venue/stadium",
    "stadium",
    "surf spot",
    "tattoo parlor",
    "tech startup",
    "temple",
    "tennis court",
    "tennis stadium",
    "theater",
    "trade school",
    "train station",
    "train",
    "university",
    "water park",
    "wedding planning",
    "women's store",
    "workplace/office",
    "yoga & pilates",
    "yoga studio",
    "candy store",
    "casino",
    "dance club",
    "pool hall",
    "rock club",
    "comedy club",
    "dance club",
    "nightlife spot",
    "other nightlife",
    "miscellaneous shop",
    "none",
    "unknown",
    "college administrative building",
    "men's store",
    "public school",
    "subway",
    "train station",
    "club",
    "arts/entertainment/nightlife",
    "consulting/business services",
    "community",
    "embassy / consulate",
    "gym / fitness center",
    "music venue",
    "non-profit organization",
    "other great outdoors",
    "professional services",
    "public places & attractions",
    "tourist attraction",
    "outdoors & recreation",
    "professional & other places",
    "public places & attractions",
    "business services",
    "convenience store",
    "tours/sightseeing",
    "attractions/things to do",
    "community organization",
    "community/government",
    "event planning/event services",
    "gift shop",
    "legal/law",
    "organization",
    "shopping/retail",
    "smoke shop",
    'taxi', 
    'spas/beauty/personal care', 
    'public places', 
    'laundry service', 
    'public relations', 
    'sports & recreation', 
    'health/medical/pharmaceuticals', 
    'toy / game store', 
    'hospital/clinic', 
    'outdoors', 
    'ferry & boat', 
    'college lab', 
    'travel/leisure', 
    'thrift / vintage store', 
    'health/wellness website', 
    'outdoor gear/sporting goods', 
    'government organization', 
    'school sports team', 
    'arts & crafts store', 
    'meeting room', 
    'farming/agriculture', 
    'ski chalet', 
    'courthouse', 
    'small business', 
    'martial arts dojo', 
    'radio station', 
    'buddhist temple', 
    'lighthouse', 
    'lake', 
    'platform', 
    'sculpture garden', 
    'playground', 
    'museum/art gallery', 
    'sports club', 
    'ski lodge', 
    'health/beauty', 
    'pet store', 
    'record label', 
    'transportation', 
    'health/medical/pharmacy', 
    'theatre', 
    'science museum', 
    'automotive', 
    'company', 
    'church/religious organization', 
    'moving target', 
    'flower shop', 
    'concert tour',
    'tour company', 
    'retail and consumer merchandise', 
    'student center', 
    'pet services', 
    'event venue', 
    'media/news/publishing', 
    'internet/software', 
    'baseball stadium', 
    'strip club', 
    'construction service & supply', 
    'home improvement', 
    'college & university', 
    'gun store', 
    'professional sports team', 
    'real estate', 
    'sports/recreation/activities', 
    'bank/financial services', 
    'non-governmental organization (ngo)',
    'resort',
    'religious center',
    'sports venue & stadium',
    'optical shop',
    'video game store',
    'home',
    'event',
    'photographic services & equipment',
    'orchestra',
    'physical fitness',
    'zoo & aquarium',
    'apartment & condo building',
    'nail salon',
    'performance venue',
    'fitness center',
    'highway',
    'nightlife',
    'automotive shop',
    'dance instruction',
    'car rental',
    'theme park',
    'cash advance service',
    'investing service',
    'repair service',
    'karaoke',
    'pool',
    'soccer field',
    'island',
    'region',
    'travel & transportation',
    'just for fun',
    'transportation service',
    'auto body shop',
    'environmental conservation',
    'rodeo',
    'airline',
    'car wash',
    "doctor's office",
    'lingerie store',
    'paper / office supplies store',
    'tourist information center',
    'aquarium',
    'health food store',
    'fair',
    'mosque',
    'fire station',
    'vintage store',
    'mobile phone shop',
    'college football field',
    'dog run',
    'conference room',
    'voting booth',
    'law school',
    'photography lab',
    'boutique',
    'cemetery',
    'design studio',
    'athletic & sport',
    'college soccer field',
    'college rec center',
    'farm',
    'garden',
    'funeral home',
    'track',
    'record shop',
    'college bookstore',
    'plane',
    'college gym',
    'newsstand',
    'elementary school',
    'college theater',
    'hobby shop',
    'medical center',
    'hotel pool',
    'college classroom',
    'college communications building',
    'beauty salon',
    'hardware store',
    'skate park',
    'post office',
    'college library',
    'college quad',
    'financial or legal service',
    'antique shop',
    'board shop',
    'zoo',
    'web design'
])

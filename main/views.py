from main.models import Mysore
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def tours(request):
    return render(request,'tours.html')
def contact(request):
    return render(request,'contact.html')
def test1(request):
    coorg= {
            'Dubare elephant camp':'''Dubare is known for its elephant camp, a forest camp on the banks of the river Kaveri in the district of Kodagu,Karnataka.''',
            'Talakaveri':'''Talakaveri is the place that is considered as birth place of the river Kaveri . It is located on Brahmagiri hills near Bhagamandala in Coorg.''',
            'Malalli falls':'''Malalli Falls is situated in the northern region of Kodagu District, Karnataka. The Kumaradhara River is the main watercourse for this waterfall.''',
            'Kumaraparvatha':'''Kumara Parvatha, at 1,712 metres, is the highest peak in Pushpagiri Wildlife Sanctuary in the Western Ghats of Karnataka. It is 4th highest peak of Karnataka.''',
            'Mandalpatti':'''Mandalpatti is  as an amazing location in Coorg. It is the place where the sky mates with the earth. To be simple a mountain range with spectacular views.''',
            'Tadiandamol':'''Tadiandamol  Trek Tadiandamol is the highest peak in Kodagu district. This mountain forms a part of the Western Ghats and is famous for trekking.''',
            'Abbey falls':'''The  waterfall is on the early reaches of the river Kaveri, located between private coffee plantations with coffee bushes and trees entwined with pepper vines.'''
        }
    return render(request,'test1.html',{'places':coorg})
def test2(request):
    chikmagalur= {
            'Rani Jhari':'''you might have gotten bored of the usual attractions that are bustling with lots of tourists and maybe thinking of exploring more of the offbeat destinations around Chikmagalur''',
            'Kudremukh' :'''Kudremukh literally means horse’s face in Kannada. This name is because of the distinctive shape of the peak. It is situated at an altitude of 6,207 ft and is the 3rd highest peak of Karnataka''',
            'EthinaBhuja' :'''A unique structure of the peak that looks like Ox’s shoulder or hump. Trekking inside the forest is the most thrilling part of the trek. The birds calling in the background and the leaves rustling in the wind''',
            'Kemmangundi':'''Kemmanagundi is a beautiful hill station in Karnataka.No wonder that Kemmanagundi is called the Ooty of Karnataka.''',
            'Baba budangiri':'''Trekking enthusiasts have a lot to look forward to on the Budangiri hike. Trails snake through dark forests of shola trees, occasional moraine-filled rocky stretches''',
            'Khythanamakki':'''Owning a 4*4 is not enough to get you there, you really need to have some nerves of steel to tackle the ruts and sharp turns that take you to the top of this beautiful hill.''',
            'Devaramane':'''Devaramane offers a number of variations that make it an ideal trekking spot for both beginners and hardcore trekkers. From a height of 3000 ft, the roar of the river flowing beneath can be heard. The famous Kapila fishing camp is located nearly 15 km from Devaramane.''',
            }
    return render(request,'test1.html',{'places':chikmagalur})
def test3(request):
    vijayanagara={
            'TB dam':'''The Tungabhadra Dam also known as Pampa Sagar is constructed across the Tungabhadra River, a tributary of the Krishna River.Is located in Hospet''',
            'Virupaksha temple':'''It is part of the Group of Monuments at Hampi, designated as a UNESCO World Heritage Site. The temple is dedicated to Lord Virupaksha, a form of Shiva.''',
            'Sasivekalu Ganesha':'''One of the major landmarks in the heritage city of Hampi, this temple houses a huge statue of Lord Ganesha, carved out of a single block of rock.''',
            'Lotus mahal':'''Lotus Mahal literally means " Palace of Lotus". This structure was made for the Royal family of the Vijayanagara Empire.Now is a historical monument''',
            'Tenali Rama pavilion':'''The pavilion still reminds people about Tenali Ramakrishna, the witty and impressive court-poet of King Krishnadevaraya of the Vijayanagara Empire.''',
            'Stone Chariot':'''The Stone Chariot as it is often referred is the flagship tourist attraction of Hampi. This is not chariot ,as the name suggests, rather built like a chariot.''',
            'Octagonal bath':'''This structure, as the name indicates, is a gigantic bathing area made in the shape of an Octagon.'''
        }
    return render(request,'test1.html',{'places':vijayanagara})
def test4(request):
    manglore={
            'Kudroli Temple':''' Kudroli Sri Gokarnanatha Kshetra, is in the Kudroli area of Mangalore in Karnataka, India. It was consecrated by Narayana Guru. It is dedicated to Gokarnanatha, a form of Lord Shiva. This temple was built in 1912 by Adhyaksha HoigeBazar Koragappa.''',
            'New Mangalore Port':'''New Mangalore Port is a small water af, all-weather port at Panambur, Mangalore in Karnataka, which is the deepest inner harbour on the west coast. It is the only major port of Karnataka and the seventh largest port in India. It is operated by New Mangalore Port Trust.''',
            'Mangaladevi Temple':'''The Mangaladevi Temple is a Hindu temple at Bolara in the city of Mangalore, situated about three km southwest of the city centre. The temple is dedicated to Hindu god Shakti in the form of Mangaladevi. The city of Mangalore is named after the presiding deity, Mangaladevi.''',
            'Ullal Beach':'''Ullal Beach is situated on the southwestern seaboard of the Indian sub-continent, adjacent to Ullal town, 10 km south of the city of Mangalore. Attractions are its picturesque stretch of Coconut trees, fishermen's lane, the ruined fort of Abbakka Devi and 16th century Jain temples.''',
            'Surathkal Beach':'''NITK Beach is situated in Surathkal, the northern part of Mangalore city. This beach is also known as Surathkal beach. It was later named after the nearby NITK (National Institute of Technology, Karnataka). It is a private beach. Sunset at NITK Beach, Mangalore. A lighthouse constructed in the year 1972 is very near to this beach.''',
            'Pilikula Nisargadhama':'''Pilikula Nisargadhama is a multi-purpose tourist attraction, at Vamanjoor, eastern part of Mangalore city in Karnataka, managed by the District Administration of Dakshina Kannada. It is a major tourist attraction of Mangalore. It attracts large number of tourists due to the availability of multiple facilities.''',
            'Panambur Beach':'''Panambur Beach is a beach in the city of Mangalore. This beach is on the shores of Arabian sea and is credited as one of the safest and best maintained beaches of India. It is the most popular, well connected and the most visited beach of Karnataka.'''
        }
    return render(request,'test1.html',{'places':manglore})
def test5(request):
    mysore={
            'Mysore Palace':'''Mysore is described as the 'City of Palaces', and there are seven palaces including this one .This historical palace  with more than 6 million annual visitors.''',

            'Chamundi Hill' : '''During Dussehra festival, a view of Mysore from top of the Chamundi hills is like a dream that makes you wonder at immense beauty of the fully lit up city.''',

            'St Philomena’s Cathedral':'''St. Philomena’s Cathedral is a remarkable example of Gothic architecture.  also boasts of being the second largest church in Asia. It is a Holy place for Christians''',

            'Mysore Sand Sculpture Museum':''' displays around 150 sculptures of sand in 16 different themes, which have been placed over an area of 13500 sq. feet. These sand sculptures have been created using more than 115 truckloads of sand. ''',

            'Talakad':'''Talakad is derived from two local chieftains called Tala and Kada is a desert-like town on left bank of Kaveri river. It once had over 30 temples, most of which now lay buried in sand. Talakad is a popular pilgrimage site for Hindus.''',

            'Sri Chamarajendra Zoological Gardens':'''One of the oldest and most popular zoos in India with 157 acre, and is home to a wide range of species and is one of the city's most popular attractions.''',

            'Brindavan Gardens':'''Undeniably one of the best terrace gardens in the world with its illuminated fountains, botanical park, extensive varieties of plants and fulfilled boating. Visited by close to 2 million tourists per year. '''
        }
    return render(request,'test1.html',{'places':mysore})
def test6(request):
    food={
            'Mysore Masala Dosa':'''Type: veg
 About: Krishnaraja Wadiyar IV who is also regarded as the originator of the masala dosa in its modern form. It is made from rice, lentils, potato, fenugreek, ghee and curry leaves, and served with chutneys and sambar.
availibilty :morning and evening
Best place:Vinayaka mylari hotel''',
            'Mysore Pak':'''Type : dessert
About:Mysore pak is an Indian sweet prepared in ghee.Former Mysore king Krishnaraja Wadiyar IV (1902-1940) was known to be was a food connoisseur. It originated in the city of Mysuru. It is made of generous amounts of ghee, sugar, gram flour, and often cardamom. The texture of this sweet is similar to a buttery and dense cookie.
available -until night(8AM-10PM) 
Best place:guru sweets''',
            'Mysore Mallige Idli':'''Type:break fast
About:In Mysore it is named after mallige (jasmine), the other thing that is popular here. The epithet has to do with both colour and texture—the idlis are rather white and very soft. It probably has to do with the fact that a local variety of rice and beaten rice are used in the batter, which results in soft and fluffy idlis. The best accompaniment to these idlis is coconut chutney, while sambhar is an afterthought.
Availability:morning and evening
Best place:Gayatri tiffin room''',
            'Filter Coffee':'''Type :beverage
About:Mysoreans believe coffee is the time for meeting and sharing and hence the evolution of the by-two coffee. But having said that, there are places where you can relish the brew. Needless to say, it has to be frothy, aromatic, steaming and served in stainless cup and dabara combination for the best experience.
Availability:until night
Place:Hotel Siddharta''',
            'Mys Bisi Bele Bath':'''Type : breakfast 
About: bisi bele bath is a spicy, rice-based dish with origins in the state of Karnataka, India. It is said to have originated in the Mysore Palace. Famous as one pot vegetarian rice dish because of its taste and aroma.
Availability:until night
Place:Mahesh Prasad''',
            'Pulao':'''Type:non-veg
About:Mysore preparing the non veg food items with the same old formula formulated by Sri Man Hanumanthu and he was the founder & Initiator.finest Non Veg Items especially for chicken palav and mutton palav.They serve the food items cooked by Firewood in an open air. 
Availibilty:morning to night
(Not available on Mondays) 
Place :Hotel Hanumanthu Original1930'''
        }
    return render(request,'food.html',{'foods':food})
def test(request):
    try:
        if request.POST['place']=='mysore':
            mysore={
                'Mysore Palace':'''Mysore is described as the 'City of Palaces', and there are seven palaces including this one .This historical palace  with more than 6 million annual visitors.''',

            'Chamundi Hill' : '''During Dussehra festival, a view of Mysore from top of the Chamundi hills is like a dream that makes you wonder at immense beauty of the fully lit up city.''',

            'St Philomena’s Cathedral':'''St. Philomena’s Cathedral is a remarkable example of Gothic architecture.  also boasts of being the second largest church in Asia. It is a Holy place for Christians''',

            'Mysore Sand Sculpture Museum':''' displays around 150 sculptures of sand in 16 different themes, which have been placed over an area of 13500 sq. feet. These sand sculptures have been created using more than 115 truckloads of sand. ''',

            'Talakad':'''Talakad is derived from two local chieftains called Tala and Kada is a desert-like town on left bank of Kaveri river. It once had over 30 temples, most of which now lay buried in sand. Talakad is a popular pilgrimage site for Hindus.''',

            'Sri Chamarajendra Zoological Gardens':'''One of the oldest and most popular zoos in India with 157 acre, and is home to a wide range of species and is one of the city's most popular attractions.''',

            'Brindavan Gardens':'''Undeniably one of the best terrace gardens in the world with its illuminated fountains, botanical park, extensive varieties of plants and fulfilled boating. Visited by close to 2 million tourists per year. '''
        }
            return render(request,'test1.html',{'places':mysore})

        if request.POST['place']=='manglore':
            manglore={
            'Kudroli Temple':''' Kudroli Sri Gokarnanatha Kshetra, is in the Kudroli area of Mangalore in Karnataka, India. It was consecrated by Narayana Guru. It is dedicated to Gokarnanatha, a form of Lord Shiva. This temple was built in 1912 by Adhyaksha HoigeBazar Koragappa.''',
            'New Mangalore Port':'''New Mangalore Port is a small water af, all-weather port at Panambur, Mangalore in Karnataka, which is the deepest inner harbour on the west coast. It is the only major port of Karnataka and the seventh largest port in India. It is operated by New Mangalore Port Trust.''',
            'Mangaladevi Temple':'''The Mangaladevi Temple is a Hindu temple at Bolara in the city of Mangalore, situated about three km southwest of the city centre. The temple is dedicated to Hindu god Shakti in the form of Mangaladevi. The city of Mangalore is named after the presiding deity, Mangaladevi.''',
            'Ullal Beach':'''Ullal Beach is situated on the southwestern seaboard of the Indian sub-continent, adjacent to Ullal town, 10 km south of the city of Mangalore. Attractions are its picturesque stretch of Coconut trees, fishermen's lane, the ruined fort of Abbakka Devi and 16th century Jain temples.''',
            'Surathkal Beach':'''NITK Beach is situated in Surathkal, the northern part of Mangalore city. This beach is also known as Surathkal beach. It was later named after the nearby NITK (National Institute of Technology, Karnataka). It is a private beach. Sunset at NITK Beach, Mangalore. A lighthouse constructed in the year 1972 is very near to this beach.''',
            'Pilikula Nisargadhama':'''Pilikula Nisargadhama is a multi-purpose tourist attraction, at Vamanjoor, eastern part of Mangalore city in Karnataka, managed by the District Administration of Dakshina Kannada. It is a major tourist attraction of Mangalore. It attracts large number of tourists due to the availability of multiple facilities.''',
            'Panambur Beach':'''Panambur Beach is a beach in the city of Mangalore. This beach is on the shores of Arabian sea and is credited as one of the safest and best maintained beaches of India. It is the most popular, well connected and the most visited beach of Karnataka.'''
        }
            return render(request,'test1.html',{'places':manglore})

        if request.POST['place']=='coorg':
            coorg= {
            'Dubare elephant camp':'''Dubare is known for its elephant camp, a forest camp on the banks of the river Kaveri in the district of Kodagu,Karnataka.''',
            'Talakaveri':'''Talakaveri is the place that is considered as birth place of the river Kaveri . It is located on Brahmagiri hills near Bhagamandala in Coorg.''',
            'Malalli falls':'''Malalli Falls is situated in the northern region of Kodagu District, Karnataka. The Kumaradhara River is the main watercourse for this waterfall.''',
            'Kumaraparvatha':'''Kumara Parvatha, at 1,712 metres, is the highest peak in Pushpagiri Wildlife Sanctuary in the Western Ghats of Karnataka. It is 4th highest peak of Karnataka.''',
            'Mandalpatti':'''Mandalpatti is  as an amazing location in Coorg. It is the place where the sky mates with the earth. To be simple a mountain range with spectacular views.''',
            'Tadiandamol':'''Tadiandamol  Trek Tadiandamol is the highest peak in Kodagu district. This mountain forms a part of the Western Ghats and is famous for trekking.''',
            'Abbey falls':'''The  waterfall is on the early reaches of the river Kaveri, located between private coffee plantations with coffee bushes and trees entwined with pepper vines.'''
        }
            return render(request,'test1.html',{'places':coorg})

        if request.POST['place']=='chikmagalur':
            chikmagalur= {
            'Rani Jhari':'''you might have gotten bored of the usual attractions that are bustling with lots of tourists and maybe thinking of exploring more of the offbeat destinations around Chikmagalur''',
            'Kudremukh' :'''Kudremukh literally means horse’s face in Kannada. This name is because of the distinctive shape of the peak. It is situated at an altitude of 6,207 ft and is the 3rd highest peak of Karnataka''',
            'EthinaBhuja' :'''A unique structure of the peak that looks like Ox’s shoulder or hump. Trekking inside the forest is the most thrilling part of the trek. The birds calling in the background and the leaves rustling in the wind''',
            'Kemmangundi':'''Kemmanagundi is a beautiful hill station in Karnataka.No wonder that Kemmanagundi is called the Ooty of Karnataka.''',
            'Baba budangiri':'''Trekking enthusiasts have a lot to look forward to on the Budangiri hike. Trails snake through dark forests of shola trees, occasional moraine-filled rocky stretches''',
            'Khythanamakki':'''Owning a 4*4 is not enough to get you there, you really need to have some nerves of steel to tackle the ruts and sharp turns that take you to the top of this beautiful hill.''',
            'Devaramane':'''Devaramane offers a number of variations that make it an ideal trekking spot for both beginners and hardcore trekkers. From a height of 3000 ft, the roar of the river flowing beneath can be heard. The famous Kapila fishing camp is located nearly 15 km from Devaramane.''',
            }
            return render(request,'test1.html',{'places':chikmagalur})

        if request.POST['place']=='vijayanagara':
            vijayanagara={
            'TB dam':'''The Tungabhadra Dam also known as Pampa Sagar is constructed across the Tungabhadra River, a tributary of the Krishna River.Is located in Hospet''',
            'Virupaksha temple':'''It is part of the Group of Monuments at Hampi, designated as a UNESCO World Heritage Site. The temple is dedicated to Lord Virupaksha, a form of Shiva.''',
            'Sasivekalu Ganesha':'''One of the major landmarks in the heritage city of Hampi, this temple houses a huge statue of Lord Ganesha, carved out of a single block of rock.''',
            'Lotus mahal':'''Lotus Mahal literally means " Palace of Lotus". This structure was made for the Royal family of the Vijayanagara Empire.Now is a historical monument''',
            'Tenali Rama pavilion':'''The pavilion still reminds people about Tenali Ramakrishna, the witty and impressive court-poet of King Krishnadevaraya of the Vijayanagara Empire.''',
            'Stone Chariot':'''The Stone Chariot as it is often referred is the flagship tourist attraction of Hampi. This is not chariot ,as the name suggests, rather built like a chariot.''',
            'Octagonal bath':'''This structure, as the name indicates, is a gigantic bathing area made in the shape of an Octagon.'''
        }
            return render(request,'test1.html',{'places':vijayanagara})

        if request.POST['place']=='None':
            return render(request,'index.html')
    except:
        return render(request,'index.html')
    
def food(request):
    try:
        if request.POST['place']=='None':
            return render(request,'index.html')
        if request.POST['place']=='coorg':
            food={
        'Akki Roti With Ellu Pajji':'''Akki roti with “Ellu Pajji” (sesame seeds chutney) is a popular breakfast among the kodavas. Cooked rice is used as an ingredient for making the akki roti. Hot white delicious akki rotis with chutney or panda curry taste heavenly.Type:Veg 
        Place Suggested: Rain tree, Coorg Pavilion
        ''',
        'Bamboo Shoot Curry': '''These are rice balls or steamed rice dumplings. Kadambattu is an important part of Kodava cuisine, including all the festivals and weddings. Rice worshiping Coorgies include rice as an ingredient in most of the recipes. Kadambattu is best paired with panda curry or chicken curry.Which can be consumed with kodava special chicken curry or pandi curry.Type:veg as well as non-veg
        Place Suggested:Kodagu Fried Chicken, Hotel Hill Palace''',
        'Kadambattu':''' These are rice balls or steamed rice dumplings. Kadambattu is an important part of Kodava cuisine, including all the festivals and weddings. Rice worshiping Coorgies include rice as an ingredient in most of the recipes. Kadambattu is best paired with panda curry or chicken curry.Which can be consumed with kodava special chicken curry or pandi curry.Type:veg as well as non-veg
        Place Suggested:Kodagu Fried Chicken, Hotel Hill Palace''',
        'Kulae Puttu':'''Coorg Style Kulae Puttu is a traditional Coorgi dish made from seasonal fruit - Jackfruit. Jackfruits cakes are steam cooked wrapped in a banana leaf. Soft and flavourful with distinct aroma of jackfruit, they taste just divine. They are best had steaming hot with ghee on top and / or honey on side.Type:veg
        Place Suggested:coorg cuisine
        ''',
        'Pandi Curry':'''Panda curry or pork curry is another dish from a coorg thali. Akki roti or kadambattu give this pandi curry the best company. Spices from Coorg increase the taste and smell of the curry.Type:Non-Veg
        Place Suggested:Hotel Le-Fortune,
        ''',
        'Paputtu':'''Paputtu is another rice-based dish that shows the love that the Kodavas have towards their staple crop. Paputtu is a steamed rice and coconut cake that is coated with a generous helping of coconut flakes. The recipe for paputtu is quite simple and involves only three ingredients—broken rice, shredded coconut and milk. The three are mixed and the mixture is dolloped into greased plates.
        Type:Veg
        Place Suggested:Taste of Coorg, Coffee Blossom Restaurant
        '''
        }
            return render(request,'food.html',{'foods':food})
    
        if request.POST['place']=='manglore':
            food={
        'Fish Food':'''About : The Fish Thali here is a must-try, and is comprised of a portion of red rice, a vegetable dish, a curry made largely from fish bones and spares, and a thick Konkani-styled yellow dal. Other recommendations include the fried anjal (kingfish) and prawns, pomfret tawa fry, ghee roasts and their prawn biryani. Best place : Machli.''',
        'Kappa Rotti':'''About : Kappa rutti or Kappa rotti – This soft in the center and crispy on the sides 4-ingredient dosa or pancake from Mangalore is a culinary delight. Kappa rutti is a popular breakfast dish from Mangalore (a city in the southern part of India). It is a type of dosa (pancake) made by grinding soaked rice with freshly grated coconut, flattened rice (poha), methi seeds and a tad bit of salt.Best place : Shetty's Kori Rotti''',
        'Kori Rotti':'''Type : morning and evening(can be eaten with veg curry or non veg curry) About : Kori rotti is a spicy dish of Tulu Udupi-Mangalorean cuisine, a combination of red-chili based chicken curry and crisp, dry wafers made from boiled rice. Kori means chicken in Tulu.Best place : Shetty's Kori Rotti''',
        'Mangalore Buns':'''About : Mangalore Buns is a popular breakfast or tea time snacks in the Udupi-Mangalore region of Karnataka, India. This food belongs to Tulu Mangalorean cuisine or Udupi cuisine. The buns are mild sweet, soft fluffy puris made using all purpose flour and banana. These buns are also called as banana buns or pooris. Typically served with a spicy coconut chutney and sambar, but they also taste great without any accompaniment. They're known for their deliciousness.Best place : New Tajmahal Cafe''',
        'Neer Dosa':'''About : Neer dosa, literally meaning water dosa in Tulu, is a crêpe prepared from rice batter. Neer dosa is a delicacy from Tulu Nadu region, and part of Udupi - Mangalorean cuisine. Usually neer dosa is served with coconut chutney, sambar, saagu and non vegetarian curries like chicken, mutton, fish and egg curry.Best place : Ideal Cafe''',
        'Chicken Ghee Roast':'''About : Chicken ghee roast is a popular Tuluva Mangalorean Chicken recipe whose origins go back to a town, Kundapur, close to Udupi. Chicken ghee roast has a fiery red, tangy and spicy with a flavor of ghee roasted spices Best place : Maharaja Family Restaurant'''
            }
            return render(request,'food.html',{'foods':food})
    
        if request.POST['place']=='chikmagalur':
            food={
            'Cheenikayi-Kadubu':'''One of the specialty Malnad dishes is Cheenikayi kadubu also called Pumpkin Idli. Prepared using grated pumpkin and rice rava, this breakfast dish is typically prepared during the first day of Diwali festival.
        Malnad cuisines open up a new world of sensory experiences to you. The simplicity in its ingredients and the use of fresh spices makes it completely different from all other cuisines in Karnataka. The cuisine of Malnad draws its inspiration from their culture and traditions and locally grown food ingredients.
        Type:veg''',
            'Pathrode':'''One of the most popular and typical Malnad food is Pathrode. It is also known by the name Patravadi and consists of key ingredients like colocasia leaves commonly known among the locals as pathrode leaves, rice, coconut paste, tamarind, and spices.
        Type:veg''',
            'Chicken Curry':'''type : non veg
        About : The classic Malnad-style Koli Saaru, prepared with khus-khus (poppy seeds) and roasted coconut might look like a common or garden chicken curry, but it's sure to surprise you with its robustly spicy taste
        best place : Maharaja Restaurant''',
            'Halasina Kaddubu':'''Type: veg
        About:As known by its name, the hero of the Malnadu Cuisine is the seasonal fruit, jackfruit which adds a typical aroma and flavour to the dish. To add the cherry on top of the cake, the idlis are steamed in banana leaves which makes the dish more sumptuous and flavoursome. Traditionally, over ripe jackfruit is used in its making, and they are served with dripping ghee on top. They will indeed make your salivary glands to rush!
        Place:River Mist resort''',
            'Holige':'''Type:veg  About:This appetizing and finger-licking dish is actually a coconut stuffed flatbread. It is famous in Karnataka, Andhra Pradesh and Tamil Nadu. Every traditional cuisine begins with relishing this dish. It provides an ethereal experience to the guests and is served with butter or ghee.
        Place:krishna sweets''',
            'Huli Avalakki':'''about: Huli Avalakki or Gojjavalakki is a scrumptious breakfast Malnad cuisine. The recipe has different variants, but the basic recipe involves boiling the water and adding salt, tamarind, jaggery which is then mixed by gram dal and urad dal powder and roasted red chilli. This flavoursome and succulent dish explodes with a variety of sensory flavours in your mouth.'''}
            return render(request,'food.html',{'foods':food})

        if request.POST['place']=='vijayanagara':
            food={
            'Girmit':'''About: Also known as Karnataka Bhel. Now, this is not a dry man dak ki This cannot be stored.  A paste sort of prepared which is called gojju which contains onion, tomato, chillies and curry leaves if needed. This mixture is mixed with puffed rice and usually served with Mirchi baiji or some people even prefer to eat with curd.
Best place:Aishwarya hotel''',
            'Chole bhature':'''This traditional dish is a combination of fried bread and chole.
        The fried bread is called Bhatoora and hence the name of the dish.
        This dish is mainly had for breakfast and is heavy.Since it is a heavy dish, it is generally accompanied by lassi.
        type:veg
        place suggested:Naivedyam''',
            'Methi-Kadabu':'''Type:break fast
About:Mentee kadabu is not as famous as all the other North-Karnataka dishes, but it still is a treat for any foody. Kadabu is made of rice or sometimes even with wheat flour and then steamed, till cooked. Later this kadabus are stir – fried with menthe soppu, otherwise known as fenugreek leaves which are finely chopped and added with a tadka of mustard seeds and as well as jeera seeds and to give a different flavour even onion and curry leaves are added.
place suggested:Naivedyam''',
            'Jolada Roti':'''jowar roti is very healthy roti recipe as it is made from jola da hittu or jowar ka atta or bajra flour.
        In north karnataka and in maharashtra it is very popular.
        It is often eaten with ennegayi recipe or you can even try the jolada rotti with dry garlic chutney.
        type:veg
        place suggested:sri manjunath hotel''',
        'Moong Dal Halwa':'''Moong dal Halwa is another famous sweet in Hospet.
        As the name implies, this sweet is made using Moong dal.
        This dish is considered very healthy too, and helps in keeping a person's body warm and so it is consumed mostly during winter.
        It takes a good time for preparation. Saffron is one of the ingredients as it gives out a pleasant smell and taste.
        type:veg
        place suggested:mango tree''',
            'Shenga-Chutney':'''About:Shenga as mentioned earlier means groundnut. So this is basically chutney prepared from groundnut. It is very tasty, savoured with idlies, rotti or paddu.
Place:aishwarya hotel'''
        }
            return render(request,'food.html',{'foods':food})

        if request.POST['place']=='mysore':
            food={
            'Mysore Masala Dosa':'''Type: veg
 About: Krishnaraja Wadiyar IV who is also regarded as the originator of the masala dosa in its modern form. It is made from rice, lentils, potato, fenugreek, ghee and curry leaves, and served with chutneys and sambar.
availibilty :morning and evening
Best place:Vinayaka mylari hotel''',
            'Mysore Pak':'''Type : dessert
About:Mysore pak is an Indian sweet prepared in ghee.Former Mysore king Krishnaraja Wadiyar IV (1902-1940) was known to be was a food connoisseur. It originated in the city of Mysuru. It is made of generous amounts of ghee, sugar, gram flour, and often cardamom. The texture of this sweet is similar to a buttery and dense cookie.
available -until night(8AM-10PM) 
Best place:guru sweets''',
            'Mysore Mallige Idli':'''Type:break fast
About:In Mysore it is named after mallige (jasmine), the other thing that is popular here. The epithet has to do with both colour and texture—the idlis are rather white and very soft. It probably has to do with the fact that a local variety of rice and beaten rice are used in the batter, which results in soft and fluffy idlis. The best accompaniment to these idlis is coconut chutney, while sambhar is an afterthought.
Availability:morning and evening
Best place:Gayatri tiffin room''',
            'Filter Coffee':'''Type :beverage
About:Mysoreans believe coffee is the time for meeting and sharing and hence the evolution of the by-two coffee. But having said that, there are places where you can relish the brew. Needless to say, it has to be frothy, aromatic, steaming and served in stainless cup and dabara combination for the best experience.
Availability:until night
Place:Hotel Siddharta''',
            'Mys Bisi Bele Bath':'''Type : breakfast 
About: bisi bele bath is a spicy, rice-based dish with origins in the state of Karnataka, India. It is said to have originated in the Mysore Palace. Famous as one pot vegetarian rice dish because of its taste and aroma.
Availability:until night
Place:Mahesh Prasad''',
            'Pulao':'''Type:non-veg
About:Mysore preparing the non veg food items with the same old formula formulated by Sri Man Hanumanthu and he was the founder & Initiator.finest Non Veg Items especially for chicken palav and mutton palav.They serve the food items cooked by Firewood in an open air. 
Availibilty:morning to night
(Not available on Mondays) 
Place :Hotel Hanumanthu Original1930'''
        }
            return render(request,'food.html',{'foods':food})
    except:
        return render(request,'index.html')

from cats import add

# ---------------- SIGHTS ----------------
add("sights","Leicester Cathedral","St Martin's, LE1 5PZ",
 "A city-centre cathedral where Richard III was reburied in 2015, with a striking modern tomb of Swaledale stone. It reopened in late 2023 after a major transformation.",
 "Free; donations welcome",web="https://leicestercathedral.org",geo="Leicester Cathedral")
add("sights","Haymarket Memorial Clock Tower","Clock Tower, LE1 5YA",
 "The Victorian clock tower of 1868 at the heart of the city, with statues of four Leicester benefactors including Simon de Montfort. Everyone meets here.",
 "Your base for walking times",ta=True,geo="Haymarket Memorial Clock Tower, Leicester",ll=(52.63640,-1.13308))
add("sights","The Golden Mile","Belgrave Road, LE4 5AT",
 "Belgrave Road is a mile of sari shops, gold jewellers, sweet marts and vegetarian Gujarati restaurants, built up from the 1970s by East African Asian families. It hosts one of the largest Diwali celebrations outside India.",
 "Go hungry; a 20-minute walk or short bus ride north",ta=True,far=False,geo="Belgrave Road, Leicester",ll=(52.6460,-1.1250))
add("sights","Bow Bridge","Bow Bridge, LE3 5BA",
 "The river crossing where, legend says, Richard III's spur struck the bridge on his way to Bosworth, and his head struck it on the way back. A plaque tells the story.",
 "A 10-minute walk from the Cathedral",ta=False,geo="Bow Bridge, Leicester",ll=(52.6335,-1.1430))
add("sights","Richard III statue","Cathedral Gardens, LE1 5PZ",
 "James Butler's bronze of the king brandishing his crown, now standing in the Cathedral gardens beside his tomb.",
 "Photo stop between the Visitor Centre and the Cathedral",ta=False,geo="Richard III statue, Leicester",ll=(52.6345,-1.1372))
add("sights","Phoenix","4 Midland Street, LE1 1TG",
 "The city's independent cinema and digital-art centre in the Cultural Quarter, with a good café-bar.",
 "Combine with the LCB Depot and Curve next door",web="https://www.phoenix.org.uk",geo="Phoenix, Midland Street, Leicester")

# ---------------- MUSEUMS ----------------
add("museums","King Richard III Visitor Centre","4A St Martin's, LE1 5DB",
 "Built over the spot where the king's skeleton was found under a council car park in 2012. You can look down on the grave site itself, and the story of the dig and the identification is told brilliantly.",
 "Allow 90 minutes; combined tickets with Jewry Wall",web="https://kriii.com",geo="King Richard III Visitor Centre")
add("museums","Jewry Wall Museum","St Nicholas Walk, LE1 4LB",
 "One of the tallest surviving Roman walls in Britain, from a 2nd-century bath house, with a new museum that reopened in July 2025 after an eight-year transformation. Roman mosaics, a bronze bull's head and immersive displays.",
 "Paid entry · Sun–Fri 10:00–16:00, Sat 10:00–17:00",web="https://www.jewrywall.com",geo="Jewry Wall Museum")
add("museums","Leicester Guildhall","Guildhall Lane, LE1 5FQ",
 "A timber-framed medieval guildhall, begun around 1390, with a Great Hall, old cells and a library. Free and atmospheric, right beside the Cathedral.",
 "Free",geo="Leicester Guildhall")
add("museums","National Space Centre","Exploration Drive, LE4 5NS",
 "Rockets in a tall see-through tower, a planetarium and hands-on galleries about space. A big hit with all ages.",
 "Book online; 10 minutes' drive north",web="https://spacecentre.co.uk",far=True,geo="National Space Centre")

# ---------------- GALLERIES ----------------
add("galleries","Leicester Museum & Art Gallery","53 New Walk, LE1 7EA",
 "A free museum on New Walk with the country's best collection of German Expressionist art, Picasso ceramics given by Richard Attenborough, Egyptian galleries and dinosaurs.",
 "Free · pair with a walk along New Walk",web="https://www.leicestermuseums.org",geo="Leicester Museum and Art Gallery")
add("galleries","LCB Depot","31 Rutland Street, LE1 1RE",
 "A creative hub in a former bus depot in the Cultural Quarter, with a free gallery space, studios and a café.",
 "Check the exhibitions page; the café is good",web="https://lcbdepot.co.uk",geo="LCB Depot, Leicester")
add("galleries","Attenborough Arts Centre","Lancaster Road, LE1 7HA",
 "The University's arts centre, named after Richard and David Attenborough's family, with two galleries, a café and an inclusive arts programme.",
 "Free galleries; near Victoria Park",geo="Attenborough Arts Centre")

# ---------------- SHOPS ----------------
add("shops","The Lanes & St Martin's","St Martin's, LE1 5DB",
 "The narrow Victorian streets and arcades between the Cathedral and the Market, packed with independent shops, cafés and vintage, around Loseby Lane, Silver Street and St Martin's Square.",
 "Start at St Martin's Square",ta=False,geo="St Martins Square, Leicester",ll=(52.6352,-1.1360))
add("shops","Henshin","Silver Street, LE1 5ET",
 "A shop devoted to anime and Japanese culture, with figures, manga and geeky gifts.",
 "Silver Street has several more independents",ta=False,geo="Henshin, Silver Street, Leicester",ll=(52.6356,-1.1355))

# ---------------- RECORDS ----------------
add("records","Rockaboom","Malcolm Arcade, LE1 5FT",
 "Leicester's longest-running independent record shop, tucked inside the Victorian Malcolm Arcade, with new and second-hand vinyl and CDs.",
 "Check it's trading before a special trip",ta=False,geo="Rockaboom, Leicester",ll=(52.6349,-1.1336))

# ---------------- VINTAGE ----------------
add("vintage","The Wardrobe","Royal Arcade, LE1 5YW",
 "Leicester's longest-running vintage clothing shop, in the Royal Arcade, with rails of good-quality vintage for men and women.",
 "Above Ground is in the same arcade",ta=False,who=["m","w"],geo="The Wardrobe, Royal Arcade, Leicester",ll=(52.6346,-1.1334))
add("vintage","Above Ground","Royal Arcade, LE1 5YW",
 "A vintage shop that has been part of the city's scene for over ten years, formerly called Pink Pigeon Forever.",
 "Pair with The Wardrobe",ta=False,who=["m","w"],geo="Above Ground, Leicester",ll=(52.6346,-1.1335))
add("vintage","The Vintage Scene","Silver Street, LE1 5ET",
 "Vintage streetwear and sportswear: retro jackets, track tops and denim.",
 "Good for 80s and 90s sportswear",ta=False,who=["m","w"],geo="The Vintage Scene, Leicester",ll=(52.6357,-1.1356))

# ---------------- CHARITY ----------------
add("charity","Sue Ryder Vintage & Retro, Loseby Lane","14 Loseby Lane, LE1 5DR",
 "A specialist Sue Ryder charity shop in the Lanes with a big selection of vintage and retro clothing and accessories, plus books and records.",
 "Worth a look on any Lanes wander",ta=False,who=["m","w"],geo="Sue Ryder, Loseby Lane, Leicester",ll=(52.6349,-1.1347))

# ---------------- MARKETS ----------------
add("markets","Leicester Market","Market Place, LE1 5HQ",
 "Billed as the largest covered outdoor market in Europe, trading for more than 700 years, with fruit and veg, Asian and Caribbean produce, and a food hall in the Corn Exchange area.",
 "Saturday is busiest with the most stalls",geo="Leicester Market")

# ---------------- CAFÉS ----------------
add("cafes","Mrs Bridges","17 Loseby Lane, LE1 5DR",
 "A Leicester institution for afternoon tea in a building from 1723, run by the same family for over forty years. Breakfasts, lunches, cakes and a proper afternoon tea.",
 "Book afternoon tea at weekends",price=2,geo="Mrs Bridges, Loseby Lane, Leicester",ll=(52.6350,-1.1348))

# ---------------- EAT ----------------
add("mid","Kayal","153 Granby Street, LE1 6FE",
 "The original branch of the Keralan chain, serving coconut curries, seafood, dosas and thalis from South India. Leicester has repeatedly been named England's curry capital.",
 "Try the fish moilee",price=2,web="https://www.kayalrestaurant.com",geo="Kayal, Granby Street, Leicester")
add("cheap","Bobby's","154–156 Belgrave Road, LE4 5AT",
 "A pure-vegetarian Gujarati restaurant and sweet mart on the Golden Mile, open since the 1970s. Thalis, chaat and Indian sweets to take away.",
 "Buy a box of sweets on the way out",price=1,geo="Bobby's, Belgrave Road, Leicester")
add("cheap","Maurizio's","Hotel Street, LE1 5AW",
 "A small, much-loved pizza and pasta spot that recently moved to Hotel Street, often called one of Leicester's best-kept secrets.",
 "Small; book or go early",price=1,geo="Maurizio's, Hotel Street, Leicester",ll=(52.6339,-1.1350))
add("mid","Mowgli","10 St Martin's Square, LE1 5DF",
 "Indian street food in a buzzy, swing-seated dining room in the Lanes.",
 "The chat bombs are the thing",price=2,geo="Mowgli, Leicester",ll=(52.6351,-1.1361))

# ---------------- PUBS ----------------
add("pubs","The Blue Boar","16 Millstone Lane, LE1 5JN",
 "A small, friendly real-ale pub that won Leicester CAMRA's 2026 urban Pub of the Year, with a rotating range of cask beers.",
 "Millstone Lane has two more good pubs",price=1,geo="Blue Boar, Millstone Lane, Leicester")
add("pubs","The Criterion","44 Millstone Lane, LE1 5JN",
 "A long-standing real-ale and craft-beer pub with good pizzas, a few minutes from the Cathedral.",
 "Pizza and a pint",price=1,geo="Criterion, Millstone Lane, Leicester",ll=(52.6317,-1.1352))
add("pubs","The Ale Wagon","22 Rutland Street, LE1 1RE",
 "A classic 1930s corner pub in the Cultural Quarter, run by the Hoskins family brewers, with their own beers on cask.",
 "Handy before a show at Curve",price=1,geo="Ale Wagon, Leicester")
add("pubs","The Salmon","19 Butt Close Lane, LE1 4QA",
 "A traditional backstreet local near the Clock Tower with a good real-ale range and a friendly crowd.",
 "Three minutes from the Clock Tower",price=1,geo="The Salmon, Butt Close Lane, Leicester")
add("pubs","The Two-Tailed Lion","22 Millstone Lane, LE1 5JN",
 "A modern micropub named after the lion on Simon de Montfort's arms, with changing casks and craft beer.",
 "Do all three Millstone Lane pubs",price=1,geo="Two-Tailed Lion, Leicester")

# ---------------- MUSIC & THEATRE ----------------
add("music","De Montfort Hall","Granville Road, LE1 7RU",
 "Leicester's 2,200-seat concert hall, hosting live music for over a century, and the main venue for big-name comedy.",
 "Next to Victoria Park",web="https://www.demontforthall.co.uk",geo="De Montfort Hall")
add("music","O2 Academy Leicester","University Road, LE1 7RH",
 "A purpose-built gig venue on the university campus, with a 1,450-capacity main room and a 500-capacity second room.",
 "Comedy Store nights too",geo="O2 Academy Leicester")
add("music","Curve","60 Rutland Street, LE1 1SB",
 "A striking glass-fronted theatre in the Cultural Quarter, known for its own big musical productions, plus touring shows and comedy.",
 "Christmas musical runs through December",web="https://www.curveonline.co.uk",geo="Curve Theatre, Leicester")

# ---------------- THINGS TO DO ----------------
add("fun","Escape Leicester","Market Street & Horsefair Street, LE1",
 "Fourteen escape rooms across city-centre sites, plus a party space for bigger groups.",
 "Book ahead at weekends",geo="Escape Leicester",ll=(52.6340,-1.1335))
add("fun","ReRoll Board Game Café","36 Granby Street, LE1 1DE",
 "A board-game café with over 400 games, barista coffee, beer and made-to-order bagels. Screens and sport are kept out.",
 "Check it's open: few 2026 listings · over 400 games",geo="ReRoll, Granby Street, Leicester",ll=(52.6345,-1.1310))

# ---------------- PARKS ----------------
add("parks","New Walk","New Walk, LE1 7EA",
 "A traffic-free Georgian promenade laid out in 1785, lined with elegant houses and leading from the centre to the Museum and Victoria Park.",
 "Walk it to the Museum & Art Gallery",ta=True,geo="New Walk, Leicester",ll=(52.6305,-1.1290))
add("parks","Abbey Park","Abbey Park Road, LE4 5AQ",
 "A big Victorian park by the River Soar, with the ruins of Leicester Abbey, where Cardinal Wolsey died in 1530, boating lakes and a small farm.",
 "15 minutes' walk north of the Clock Tower",geo="Abbey Park, Leicester")
add("parks","Castle Gardens & the Newarke","Castle Gardens, LE1 5WW",
 "A quiet riverside garden below the remains of Leicester Castle's motte, next to the medieval Newarke gateway and Newarke Houses Museum.",
 "Peaceful spot after the Cathedral",ta=False,geo="Castle Gardens, Leicester")

# ---------------- SPORT ----------------
add("sport","King Power Stadium (Leicester City)","Filbert Way, LE2 7FL",
 "Home of the 2016 Premier League champions, one of football's greatest upsets. Stadium tours run on non-match days.",
 "20 minutes' walk south of the centre",far=True,geo="King Power Stadium")
add("sport","Welford Road (Leicester Tigers)","Aylestone Road, LE2 7TR",
 "Home of the Tigers, one of English rugby's most successful clubs, in one of the biggest club rugby grounds in the country.",
 "A 15-minute walk from the station",geo="Welford Road Stadium")

# ---------------- DAY TRIPS ----------------
add("trips","Bosworth Battlefield Heritage Centre","Ambion Lane, Sutton Cheney, CV13 0AD",
 "Where Richard III was killed in 1485, ending the Wars of the Roses. A heritage centre, a 2.2 km battlefield trail and a sundial memorial.",
 "Pair with the Richard III sites in the city",far=True,drive="30 min",geo="Bosworth Battlefield Heritage Centre")
add("trips","Bradgate Park","Newtown Linford, LE6 0HE",
 "830 acres of ancient deer park in Charnwood Forest, with red and fallow deer, the ruins of Lady Jane Grey's childhood home and Old John folly on the hilltop.",
 "Free entry; paid parking",far=True,drive="20 min",geo="Bradgate Park")
add("trips","Foxton Locks","Gumley Road, Foxton, LE16 7RA",
 "The largest flight of staircase locks in England: ten locks climbing a hill on the Grand Union Canal, with the remains of a Victorian boat lift, pubs and a café.",
 "Free to visit; pay for parking",far=True,drive="30 min",geo="Foxton Locks")
add("trips","Great Central Railway","Great Central Road, Loughborough, LE11 1RW",
 "Britain's only double-track main-line heritage railway, running steam trains between Loughborough and Leicester North.",
 "Steam services at weekends and holidays; check the timetable",web="https://www.gcrailway.co.uk",far=True,drive="25 min",geo="Loughborough Central station")
add("trips","Melton Mowbray","Ye Olde Pork Pie Shoppe, 10 Nottingham Street, Melton Mowbray, LE13 1NW",
 "England's 'rural capital of food', the home of the Melton Mowbray pork pie and Stilton. Ye Olde Pork Pie Shoppe still hand-raises pies the traditional way.",
 "Tuesday is market day",far=True,drive="30 min",geo="Ye Olde Pork Pie Shoppe")

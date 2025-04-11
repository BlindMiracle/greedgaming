from typing import Any
from django.shortcuts import render


def catalog(request) -> Any:
    context: set[str] = {
        "title": "Home - Каталог",
        "goods": [ 
        {'image': 'deps/images/goods/Space_Marine_II_cover_art.jpg',
         'name': 'Warhammer 40,000: Space Marine 2',
         'description': 'FOR THE EMPEROR',
         'price': 150.00},

        {'image': 'deps/images/goods/Battlefield_1.jpg',
         'name': 'Battlefield 1',
         'description': 'World War 1 ection fps shooter',
         'price': 150.00},

         {'image': 'deps/images/goods/56b86a914860844cc7894e0969787205.jpg',
         'name': 'PUBG',
         'description': 'Hungury games , and most popular battle royal',
         'price': 93.00},

         {'image': 'deps/images/goods/WJd8SY87zp3xUnCctOrulr5F.avif',
         'name': 'Silent Hill',
         'description': 'Remake of the legendary game',
         'price': 670.00},

         {'image': 'deps/images/goods/Resident_Evil_2_Remake_coverart.jpg',
         'name': 'Resident Evil 2',
         'description': 'One of the most popular part of the Resident Evil series',
         'price': 365.00},

         {'image': 'deps/images/goods/TheForest.webp',
         'name': 'The forest',
         'description': 'Single on the iceland with hanibals',
         'price': 430.00},

         {'image': 'deps/images/goods/Minecraft_Cover_Art.png',
         'name': 'Miencraft',
         'description': 'I really need to talk about this game?',
         'price': 610.00},

         {'image': 'deps/images/goods/lGNl1QrYl9IMzE-big.webp',
         'name': 'Garrys mod',
         'description': 'Its time to show , the real definition of word "PlayGround"',
         'price': 55.00},

         {'image': 'deps/images/goods/Squad_game_cover.jpeg',
         'name': 'Squad',
         'description': 'One of the best millsims ever created',
         'price': 190.00},

         {'image': 'deps/images/goods/MV5BOWQ1ZDdiMDItYTc2My00ZjZkLWJlMzktYTZmNGY5MWQwODU2XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg',
         'name': 'Fate/stay night',
         'description': 'Please Artoria step on me',
         'price': 30.00},

         {'image': 'deps/images/goods/rIgEHv7qojJncnH4Msler23l55pLwEJLMyxdC3fUNUT6SApDEJDDOoUhj6uhBOqUhK4arBQzd98ay70v29P_5dne.jpg',
         'name': 'Tsukihime',
         'description': 'Lets breed Arceuid',
         'price': 10.00},

         {'image': 'deps/images/goods/mahotsukai_no_yoru-916944997-large.jpg',
         'name': 'Witch on the Holy Night',
         'description': 'Just good VN',
         'price': 15.00},
        ]
    }
    return render(request, 'goods/catalog.html', context)



def product(request) -> Any:
    return render(request, 'goods/product.html')
# Create your views here.

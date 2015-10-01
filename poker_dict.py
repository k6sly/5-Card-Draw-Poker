facecard = {"A": 14, "K": 13, "Q": 12, "J": 11}
cards = ["As", "Ac", "Ah", "Ad","Ks", "Kc", "Kh", "Kd","Qs", "Qc", "Qh", "Qd","Js", "Jc", "Jh", "Jd","10s", "10c", "10h", "10d",
         "9s", "9c", "9h", "9d","8s", "8c", "8h", "8d","7s", "7c", "7h", "7d","6s", "6c", "6h", "6d","5s", "5c", "5h", "5d","4s",
         "4c", "4h", "4d","3s", "3c", "3h", "3d","2s", "2c", "2h", "2d"]
hands = {1: "High Card", 2: "One Pair", 3: "Two Pair", 4: "Three of a Kind", 5: "Strait", 6: "Flush", 7: "Full House",
         8: "Four of a Kind", 9: "Strait Flush", 10: "*** Royal Flush  ***"}
cardface = {14: "Ace", 13: "King", 12: "Queen", 11: "Jack"}
compNames = ["Margeret", "Roselia", "Tad", "Agueda", "Maegan", "Hilton", "Korey", "Velma", "Karan", "Nam", "Mauro", "Dolly",
             "Stefany", "Sudie", "Wilmer", "Katerine", "Mila", "Remedios", "Bret", "Jodie", "Meta", "Brice", "Fabiola", "Tawny",
             "Lucilla", "Christi", "Diedre", "Tricia", "Maxie", "Sanda", "Floyd", "Mardell", "Fran", "Katherina", "Jorge", "Cami",
             "Aubrey", "Renay", "Beata", "Buster", "Stella", "Yu", "Blanch", "Deshawn", "Collette", "Brook", "Junie", "Regine", "Lavada", "Alene"]		 
cardsGraph = {
"Ad":
"""
._____
|A .  |
| / \ |
| \ / |
|  . A|
`-----'
"""
   ,
"Kd":
"""
._____
|K .  |
| / \ |
| \ / |
|  . K|
`-----'
"""
   ,
"Qd":
"""
._____
|Q .  |
| / \ |
| \ / |
|  . Q|
`-----'
"""
   ,
"Jd":
"""
._____
|J .  |
| / \ |
| \ / |
|  . J|
`-----'
"""
   ,
"10d":
"""
._____
|T .  |
| / \ |
| \ / |
|  . T|
`-----'
"""
   ,
"9d":
"""
._____
|9 .  |
| / \ |
| \ / |
|  . 9|
`-----'
"""
   ,
"8d":
"""
._____
|8 .  |
| / \ |
| \ / |
|  . 8|
`-----'
"""
   ,
"7d":
"""
._____
|7 .  |
| / \ |
| \ / |
|  . 7|
`-----'
"""
   ,
"6d":
"""
._____
|6 .  |
| / \ |
| \ / |
|  . 6|
`-----'
"""
   ,
"5d":
"""
._____
|5 .  |
| / \ |
| \ / |
|  . 5|
`-----'
"""
   ,
"4d":
"""
._____
|4 .  |
| / \ |
| \ / |
|  . 4|
`-----'
"""
   ,
"3d":
"""
._____
|3 .  |
| / \ |
| \ / |
|  . 3|
`-----'
"""
   ,
"2d":
"""
._____
|2 .  |
| / \ |
| \ / |
|  . 2|
`-----'
"""
   ,
"As":
"""
._____
|A .  |
| / \ |
|(_._)|
|  | A|
`-----'
"""
   ,
"Ks":
"""
._____
|K .  |
| / \ |
|(_._)|
|  | K|
`-----'
"""
   ,
"Qs":
"""
._____
|Q .  |
| / \ |
|(_._)|
|  | Q|
`-----'
"""
   ,
"Js":
"""
._____
|J .  |
| / \ |
|(_._)|
|  | J|
`-----'
"""
   ,
"10s":
"""
._____
|T .  |
| / \ |
|(_._)|
|  | T|
`-----'
"""
   ,
"9s":
"""
._____
|9 .  |
| / \ |
|(_._)|
|  | 9|
`-----'
"""
   ,
"8s":
"""
._____
|8 .  |
| / \ |
|(_._)|
|  | 8|
`-----'
"""
   ,
"7s":
"""
._____
|7 .  |
| / \ |
|(_._)|
|  | 7|
`-----'
"""
   ,
"6s":
"""
._____
|6 .  |
| / \ |
|(_._)|
|  | 6|
`-----'
"""
   ,
"5s":
"""
._____
|5 .  |
| / \ |
|(_._)|
|  | 5|
`-----'
"""
   ,
"4s":
"""
._____
|4 .  |
| / \ |
|(_._)|
|  | 4|
`-----'
"""
   ,
"3s":
"""
._____
|3 .  |
| / \ |
|(_._)|
|  | 3|
`-----'
"""
   ,
"2s":
"""
._____
|2 .  |
| / \ |
|(_._)|
|  | 2|
`-----'
"""
   ,
"Ac":
"""
._____
|A _  |
| ( ) |
|(_._)|
|  | A|
`-----'
"""
   ,
"Kc":
"""
._____
|K _  |
| ( ) |
|(_._)|
|  | K|
`-----'
"""
   ,
"Qc":
"""
._____
|Q _  |
| ( ) |
|(_._)|
|  | Q|
`-----'
"""
   ,
"Jc":
"""
._____
|J _  |
| ( ) |
|(_._)|
|  | J|
`-----'
"""
   ,
"10c":
"""
._____
|T _  |
| ( ) |
|(_._)|
|  | T|
`-----'
"""
   ,
"9c":
"""
._____
|9 _  |
| ( ) |
|(_._)|
|  | 9|
`-----'
"""
   ,
"8c":
"""
._____
|8 _  |
| ( ) |
|(_._)|
|  | 8|
`-----'
"""
   ,
"7c":
"""
._____
|7 _  |
| ( ) |
|(_._)|
|  | 7|
`-----'
"""
   ,
"6c":
"""
._____
|6 _  |
| ( ) |
|(_._)|
|  | 6|
`-----'
"""
   ,
"5c":
"""
._____
|5 _  |
| ( ) |
|(_._)|
|  | 5|
`-----'
"""
   ,
"4c":
"""
._____
|4 _  |
| ( ) |
|(_._)|
|  | 4|
`-----'
"""
   ,
"3c":
"""
._____
|3 _  |
| ( ) |
|(_._)|
|  | 3|
`-----'
"""
   ,
"2c":
"""
._____
|2 _  |
| ( ) |
|(_._)|
|  | 2|
`-----'
"""
   ,
"Ah":
"""
._____
|A_ _ |
|( . )|
| \ / |
|  . A|
`-----'
"""
   ,
"Kh":
"""
._____
|K_ _ |
|( . )|
| \ / |
|  . K|
`-----'
"""
   ,
"Qh":
"""
._____
|Q_ _ |
|( . )|
| \ / |
|  . Q|
`-----'
"""
   ,
"Jh":
"""
._____
|J_ _ |
|( . )|
| \ / |
|  . J|
`-----'
"""
   ,
"10h":
"""
._____
|T_ _ |
|( . )|
| \ / |
|  . T|
`-----'
"""
   ,
"9h":
"""
._____
|9_ _ |
|( . )|
| \ / |
|  . 9|
`-----'
"""
   ,
"8h":
"""
._____
|8_ _ |
|( . )|
| \ / |
|  . 8|
`-----'
"""
   ,
"7h":
"""
._____
|7_ _ |
|( . )|
| \ / |
|  . 7|
`-----'
"""
   ,
"6h":
"""
._____
|6_ _ |
|( . )|
| \ / |
|  . 6|
`-----'
"""
   ,
"5h":
"""
._____
|5_ _ |
|( . )|
| \ / |
|  . 5|
`-----'
"""
   ,
"4h":
"""
._____
|4_ _ |
|( . )|
| \ / |
|  . 4|
`-----'
"""
   ,
"3h":
"""
._____
|3_ _ |
|( . )|
| \ / |
|  . 3|
`-----'
"""
   ,
"2h":
"""
._____
|2_ _ |
|( . )|
| \ / |
|  . 2|
`-----'
"""}
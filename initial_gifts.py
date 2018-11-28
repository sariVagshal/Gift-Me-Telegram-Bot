import settings
from gift_DB import giftList

#['Flowers', 'Balloons', 'Chocolates', 'Surprise Gift']
def initial():
    g = giftList(settings.HOST, settings.DB)
    g.add_gift('Flowers', "20$", "data:image/jpeg;base64,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")
    g.add_gift('Flowers', "40$", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXA7DP8Wx8WPl6hwLkxV0exVSX3LfszysZ49DETvC35vWZQsdfmw")
    g.add_gift('Flowers', "26$", "http://www.ofer-flowers.co.il/wp-content/uploads/2013/07/Fotolia_44012051_XS.jpg")
    g.add_gift('Flowers', "92$", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRq66uJYzhragmtvu0Ix-_2YpXXV18w0K7aTdN3p0WuXR4FNL6A")

    g.add_gift('Balloons', "47$", "https://www.balloonmonkey.co.uk/newimg/cache/5846/4.png")
    g.add_gift('Balloons', "80$", "https://cdn.shopify.com/s/files/1/1988/3711/products/Christmas-Layouts-3-F2_1200x.jpg?v=1542889042")
    g.add_gift('Balloons', "47$", "https://www.balloonmonkey.co.uk/newimg/cache/5846/4.png")

    g.add_gift('Chocolates', "26$", "https://pieceloveandchocolate.com/wp-content/uploads/2014/08/Gift-Baskets-Sm-Files-14.jpg")
    g.add_gift('Chocolates', "81$", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBXLgAMpwVFaqFTtM2_uBCds3H0Jl7--EnQ1YIdAhMXhenO5lZCw")
    g.add_gift('Chocolates', "48$", "https://cdn2.harryanddavid.com/wcsstore/HarryAndDavid/images/catalog/18_31816_30J_01ex.jpg?height=378&width=345&quality=70")

    g.add_gift('Surprise Gift', "90$", "https://image.freepik.com/free-vector/opened-surprise-gift-box_3446-340.jpg")



initial()


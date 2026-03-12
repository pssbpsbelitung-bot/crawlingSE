keywords = [

"order",
"open order",
"ready stock",
"jual",
"promo",
"diskon",
"harga",
"reseller",
"cod",
"wa"

]

def detect_business(text):

    text = text.lower()

    for k in keywords:

        if k in text:
            return True

    return False
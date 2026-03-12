locations = [

"belitung",
"tanjungpandan",
"sijuk",
"membalong",
"badau",
"selat nasik"

]

def is_belitung(text):

    text = text.lower()

    for loc in locations:

        if loc in text:
            return True

    return False
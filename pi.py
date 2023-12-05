text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
text_1 = [x.strip(",") for x in text.split()] #textを空白で区切りカンマを消去
text_2 = [x.strip(".") for x in text_1]       #ピリオドを消去
text_c = list(map(len, text_2))               #それぞれの文字数をカウント

result = str(text_c[0])
for i in range(1, len(text_c)):
    result += str(text_c[i])

print(result)
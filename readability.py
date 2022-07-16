text = input("Text: ")

letras = frases = 0
palavras = 1

for char in text:
    if char.isalpha():
        letras+=1
    if char.isspace():
        palavras+=1
    if char in['!' ,'.',  '?']:
        frases+=1

l = (letras*100.0)/palavras
f = (frases*100.0)/palavras
nivel= round((0.0588 * l - 0.296 * f - 15.8))

if nivel < 1:
    print("Before Grade 1")
if nivel > 16:
    print("Grade 16+")
else:
    print(f"Grade {nivel}")

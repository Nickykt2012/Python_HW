text = """She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells""".split()
set_result = set()
for i in text:
    set_result.add(i.lower())
print(len(set_result))

"""newSecondList = []
for i in someList:
if i not in newSecondList:
newSecondList.append(i)
print(len(newSecondList))"""

"""Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, 
слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
Output: 13"""
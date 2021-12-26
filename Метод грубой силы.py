def substring_search(text, substring):
    result = []

    def string_equals(text, substring, i):
        return substring == text[i:i + len(substring)]

    for i in range(len(text)-len(substring)):
        if string_equals(text, substring, i):
            result.append(i)

    return result


text = "Текст созданный только для проверки. Текст не используется где-то еще"
substring = "Текст"
s = substring_search(text, substring)
if s == []:
    print("Подстрока не найдена")
else:
    print("Подстрока  найдена")
print(s)



import re
adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# task 01 == Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
# треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", "")
print(adwentures_of_tom_sawer)
# task 02 == Замініть .... на пробіл
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)
# task 03 == Зробіть так, щоб у тексті було не більше одного пробілу між словами.
clean_text = re.sub(r'\s+', ' ', adwentures_of_tom_sawer).strip()
print("Normalized Text:")
print(clean_text)
# task 04 Виведіть, скількі разів у тексті зустрічається літера "h"
letter_count = clean_text.count("h")
print(f"Letter 'h' appears {letter_count} times")
# task 05 Виведіть, скільки слів у тексті починається з Великої літери?
words = clean_text.split()
capitalized_letters = len([w for w in words if re.match(r'^[A-Z]', w)])
print(f"Words srart with the capital letter {capitalized_letters}")
# task 06 Виведіть позицію, на якій слово Tom зустрічається вдруге - im not quite sure
# task 07 Розділіть змінну adwentures_of_tom_sawer по кінцю речення.Збережіть результат у змінній adwentures_of_tom_sawer_sentences
adwentures_of_tom_sawer_sentences = re.split(r'[.!?]\s+', clean_text)
print(adwentures_of_tom_sawer_sentences)
# task 08 Виведіть четверте речення з adwentures_of_tom_sawer_sentences. Перетворіть рядок у нижній регістр.
if len(adwentures_of_tom_sawer_sentences) >= 4:
    fourth_sentence = adwentures_of_tom_sawer_sentences[3].strip()
    fourth_sentence_lower = fourth_sentence.lower()
    print("Fourth sentence in lowercase:")
    print(fourth_sentence_lower)
else:
    print("There are not enough sentences in the text.")
# task 09 Перевірте чи починається якесь речення з "By the time".
pattern = r"/bBy the time/"
matches = [sentence for sentence in adwentures_of_tom_sawer_sentences if re.match(pattern, sentence)]
if matches:
    print("The text contains a sentence starting with 'By the time'.")
else:
    print("The text does not contain a sentence starting with 'By the time'.")
# task 10 Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.im not quite sure

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
# task 06 Виведіть позицію, на якій слово Tom зустрічається вдруге
finding_Tom1 = adwentures_of_tom_sawer.find("Tom")
finding_Tom2 = adwentures_of_tom_sawer.find("Tom", finding_Tom1 + 1)
print("Position where Tom appears second time is", finding_Tom2 )
# task 10 Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('.')
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('!')
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('?')
last_sentence = adwentures_of_tom_sawer_sentences[-1]
words_in_last_sentence = len(last_sentence)
print("Last sentence contains of ", words_in_last_sentence , "words")
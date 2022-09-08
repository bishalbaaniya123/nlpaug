from nlpaug.augmenter.word import BackTranslationAug

back_translation = BackTranslationAug()

test_text = 'the quick brown fox jumps over a lazy dog'
print(back_translation.substitute(test_text))

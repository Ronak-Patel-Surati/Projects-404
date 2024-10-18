from twttr import shorten

def test_cases():
   assert shorten("Ronit") == 'Rnt'
def test_cases1():
   assert shorten("RONIT") == 'RNT'
def test_cases2():
   assert shorten("ronit") == 'rnt'
def test_cases3():
   assert shorten("rOnit") == 'rnt'
def test_cases4():
   assert shorten("Apple") == 'ppl'

def test_cases5():
   assert shorten("$ 69.69") == '$ 69.69'

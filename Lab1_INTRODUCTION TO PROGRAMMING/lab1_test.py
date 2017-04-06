from unittest import TestCase

class IsogramTestCases(TestCase):
  def test_checks_for_isograms(self):
    word = 'abolishment'
    self.assertEqual(
      is_isogram(word),
      (word, True),
      msg="Isogram word, '{}' not detected correctly".format(word)
    )

  def test_returns_false_for_nonisograms(self):
    word = 'alphabet'
    self.assertEqual(
      is_isogram(word),
      (word, False),
      msg="Non isogram word, '{}' falsely detected".format(word)
    )

  def test_it_only_accepts_strings(self):
    with self.assertRaises(TypeError) as context:
      is_isogram(2)
      self.assertEqual(
        'Argument should be a string',
        context.exception.message,
        'String inputs allowed only'
      )
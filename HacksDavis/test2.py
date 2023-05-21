from keybert import KeyBERT
from PyPDF2 import PdfReader

#path = "/Users/dr1229/Desktop/HacksDavis/ChartrandPolimeniZhang.pdf"
path = "/Users/dr1229/Desktop/HacksDavis/Anth3_Workbook_Winter_2023.pdf"

reader = PdfReader(path)

text = ""

for i,page in enumerate(reader.pages):
    #if i < 40 and i > 30:
    text += page.extract_text()

doc = """
         Supervised learning is the machine learning task of learning a function that
         maps an input to an output based on example input-output pairs. It infers a
         function from labeled training data consisting of a set of training examples.
         In supervised learning, each example is a pair consisting of an input object
         (typically a vector) and a desired output value (also called the supervisory signal).
         A supervised learning algorithm analyzes the training data and produces an inferred function,
         which can be used for mapping new examples. An optimal scenario will allow for the
         algorithm to correctly determine the class labels for unseen instances. This requires
         the learning algorithm to generalize from the training data to unseen situations in a
         'reasonable' way (see inductive bias).
      """
kw_model = KeyBERT()
keywords = kw_model.extract_keywords(text)

print(keywords)
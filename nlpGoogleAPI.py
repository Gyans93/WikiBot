from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def language_analysis(text):
    client = language.LanguageServiceClient()

    document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)
    encoding_type = enums.EncodingType.UTF8

    # Detects the sentiment of the text
    sent_analysis = client.analyze_sentiment(document=document)
    sentiment = sent_analysis.document_sentiment
    

    # print(dir(sent_analysis))

    ent_response = client.analyze_entities(document, encoding_type=encoding_type)
    # print(ent_response)
    entities = ent_response.entities
    return sentiment, entities
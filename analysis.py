import nltk
import json
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the VADER lexicon and stop words for sentiment analysis
nltk.download('vader_lexicon')
nltk.download('stopwords')

# Get English stop words
stop_words = set(stopwords.words('english'))

# Function to categorize sentiment as Positive, Negative, or Neutral
def categorize_sentiment(score):
    if score >= 0.05:
        return 'Positive'
    elif score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Function to perform sentiment analysis on text
def analyze_sentiment(text):
    # Tokenize the text and remove stop words
    tokens = [word.lower() for word in nltk.word_tokenize(text) if word.isalpha() and word.lower() not in stop_words]

    # Join the tokens back into a string
    filtered_text = ' '.join(tokens)

    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(filtered_text)['compound']
    return categorize_sentiment(sentiment_score)

# Function to create the desired JSON structure
def create_output_json(data):
    # Combine text from all movies for overall sentiment analysis
    all_movies_text = ' '.join([' '.join([utterance['text'] for utterance in conv['utterances']]) for conv in data])
    overall_sentiment = analyze_sentiment(all_movies_text)

    output = {
        "moviesentiments": overall_sentiment,
        "movies": {}
    }

    for conv in data:
        movie_name = conv['metadata']['movie_name']

        characters_sentiments = {}

        for utterance in conv['utterances']:
            character_name = f"Character_{utterance['speaker_id']}"
            character_text = utterance['text']
            sentiment = analyze_sentiment(character_text)

            if movie_name not in output["movies"]:
                output["movies"][movie_name] = {
                    "charactersentiments": {}
                }

            if character_name not in output["movies"][movie_name]['charactersentiments']:
                output["movies"][movie_name]['charactersentiments'][character_name] = {}

            output["movies"][movie_name]['charactersentiments'][character_name] = sentiment

    return output

# Assuming your dataset is stored in a variable named 'data'
output_data = create_output_json(data)

# Write the output JSON to a file
with open('sentiment_output.json', 'w') as output_file:
    json.dump(output_data, output_file, indent=2)

print("Sentiment analysis completed. Output saved to 'sentiment_output.json'")
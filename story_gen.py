from textblob import TextBlob
from transformers import pipeline

# Load GPT-2 text generation pipeline
story_generator = pipeline("text-generation", model="gpt2")

def detect_emotion(text):
    """
    Analyze the input text and return an emotion tag.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.3:
        return "happy"
    elif polarity < -0.3:
        return "sad"
    else:
        return "neutral"

def generate_story(prompt, max_length=150):
    """
    Generate a story continuation based on a prompt.
    Returns the generated text and detected emotion.
    """
    generated = story_generator(prompt, max_length=max_length, num_return_sequences=1)
    story_text = generated[0]['generated_text']
    emotion = detect_emotion(story_text)
    return story_text, emotion

if __name__ == "__main__":
    sample_prompt = "Once upon a time, in a foggy forest, a lonely fox"
    story, emotion = generate_story(sample_prompt)
    print("Emotion detected:", emotion)
    print("Generated story:\n", story)

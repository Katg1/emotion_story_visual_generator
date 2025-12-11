
from story_gen import generate_story
from visual_gen import generate_visual
from utils import ensure_folder

def main():
    ensure_folder("samples")
    print("Welcome to the Emotion-Driven Story & Visual Generator!\n")
    
    prompt = input("Enter a short story prompt: ")
    story, emotion = generate_story(prompt)
    
    print("\n--- Generated Story ---")
    print(story)
    print(f"\nDetected Emotion: {emotion}")
    
    visual_path = generate_visual(emotion)
    print(f"Abstract visual saved to: {visual_path}")

if __name__ == "__main__":
    main()

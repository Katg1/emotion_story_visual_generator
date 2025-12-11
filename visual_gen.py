from PIL import Image, ImageDraw
import random

EMOTION_COLORS = {
    "happy": ["#FFD700", "#FF6347", "#00FF7F", "#1E90FF"],  # bright colors
    "sad": ["#1E3A5F", "#4B6C8B", "#708090", "#A9A9A9"],   # cool/muted
    "neutral": ["#C0C0C0", "#808080", "#D3D3D3", "#A9A9A9"] # neutral
}

def generate_visual(emotion, width=800, height=600, output_path="samples/sample_visual.png"):
    """
    Generate an abstract image based on the detected emotion.
    """
    colors = EMOTION_COLORS.get(emotion, EMOTION_COLORS["neutral"])
    img = Image.new("RGB", (width, height), color=random.choice(colors))
    draw = ImageDraw.Draw(img)

    # Draw random abstract shapes
    for _ in range(30):
        shape_type = random.choice(["ellipse", "rectangle", "line"])
        x0, y0 = random.randint(0, width//2), random.randint(0, height//2)
        x1, y1 = random.randint(width//2, width), random.randint(height//2, height)
        color = random.choice(colors)
        if shape_type == "ellipse":
            draw.ellipse([x0, y0, x1, y1], fill=color, outline=None)
        elif shape_type == "rectangle":
            draw.rectangle([x0, y0, x1, y1], fill=color, outline=None)
        else:
            draw.line([x0, y0, x1, y1], fill=color, width=random.randint(2, 6))

    img.save(output_path)
    print(f"Visual generated and saved to {output_path}")
    return output_path

if __name__ == "__main__":
    generate_visual("happy")

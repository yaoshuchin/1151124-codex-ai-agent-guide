import json

# Read enriched_slides.json
with open("enriched_slides.json", "r", encoding="utf-8") as f:
    slides = json.load(f)

# Convert to embedded JS string
slides_js = f"window.SLIDES_DATA = {json.dumps(slides, ensure_ascii=False, indent=2)};"
with open("deck_data.js", "w", encoding="utf-8") as f:
    f.write(slides_js)

print("Generated deck_data.js successfully.")

from PIL import Image, ImageEnhance, ImageFilter
import os

def photo_editor(input_path, output_path):
    # Create the output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    # Check if the input directory exists
    if os.path.exists(input_path):
        # Iterate over each file in the input directory
        for filename in os.listdir(input_path):
            if filename.lower().endswith((".jpg", ".jpeg", ".png")):  # Process only image files
                # Open the image
                img = Image.open(os.path.join(input_path, filename))

                # Convert the image to black and white
                edit = img.convert('L')

                # Apply sharpening filter
                edit = edit.filter(ImageFilter.SHARPEN)

                # Rotate the image by -90 degrees
                edit = edit.rotate(-90)

                # Enhance contrast
                contrast_factor = 1.5
                enhancer = ImageEnhance.Contrast(edit)
                edit = enhancer.enhance(contrast_factor)

                # Create the cleaned name for the output file
                clean_name = os.path.splitext(filename)[0]

                # Save the edited image to the output directory
                edit.save(os.path.join(output_path, f"{clean_name}_edited.jpg"))
    else:
        print(f"Error: Input directory '{input_path}' not found.")

# Example usage:
input_directory = r"C:\Users\amalh\OneDrive - MSFT\Desktop\Downloaded Images"  # Change this to your input directory
output_directory = r"C:\Users\amalh\OneDrive - MSFT\Desktop\Edited Images"  # Change this to your output directory

photo_editor(input_directory, output_directory)

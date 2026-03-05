import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

def generate_bulk_certificates():
    csv_file = "athletes.csv"
    template_path = "template.jpg"
    output_folder = "Completed_Certificates"
    photos_folder = "Photos"  # The folder where you drop photo1.jpg, photo2.jpeg, etc.

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        messagebox.showerror("Error", f"Could not find {csv_file}. Make sure it is in the same folder.")
        return

    # --- 1. FONT SETTINGS ---
    try:
        font_regular = ImageFont.truetype("ARIAL.TTF", 25) 
        font_large = ImageFont.truetype("ARIAL.TTF", 25) 
    except IOError:
        messagebox.showerror("Error", "Python cannot find 'ARIAL.TTF'!\nMake sure it is in the folder.")
        return 

    # --- 2. TEXT COORDINATES ---
    coords = {
        "sl_no": (307, 129), "name_header": (288, 167), "represented_header": (364, 210),
        "snatch_header": (310, 245), "clean_jerk_header": (608, 245), "total_header": (780, 245),
        "dob": (777, 210), "category_header": (1039, 210), "position_header": (1036, 245),
        
        "category_body": (441, 1190), "snatch_body": (928, 1192), 
        "clean_jerk_body": (928, 1244), "total_body": (928, 1294),
        "place": (422, 1246), "dob_body": (419, 1345)
    }

    center_x = 620
    awarded_to_y = 831  
    from_place_y = 932  

    # --- 3. PHOTO SETTINGS ---
    photo_box_1_xy = (61, 84)         
    photo_size_1 = (140, 185)         
    photo_box_2_xy = (966, 673)      
    photo_size_2 = (145, 185)          

    success_count = 0

    # --- 4. GENERATION LOOP ---
    for index, row in df.iterrows():
        try:
            img = Image.open(template_path)
            draw = ImageDraw.Draw(img)

            # Draw Header Text 
            draw.text(coords["sl_no"], str(row['slno']), fill="black", font=font_regular, anchor="ls")
            draw.text(coords["name_header"], str(row['name']), fill="black", font=font_regular, anchor="ls")
            draw.text(coords["represented_header"], str(row['represented']), fill="black", font=font_regular, anchor="ls")
            draw.text(coords["snatch_header"], str(row['snatch']), fill="black", font=font_regular, anchor="ls")
            draw.text(coords["clean_jerk_header"], str(row['clean_jerk']), fill="black", font=font_regular, anchor="ls")
            draw.text(coords["total_header"], str(row['total']), fill="black", font=font_regular, anchor="ls")
            draw.text(coords["dob"], str(row['dob']), fill="black", font=font_regular, anchor="ls")
            draw.text(coords["category_header"], str(row['category']), fill="black", font=font_regular, anchor="ls")
            draw.text(coords["position_header"], str(row['position']), fill="black", font=font_regular, anchor="ls")

            # Draw Center Text 
            main_name = str(row['name']).upper()
            represented_place = str(row['represented']).upper()
            
            draw.text((center_x, awarded_to_y), main_name, fill="black", font=font_large, anchor="ms")
            draw.text((center_x, from_place_y), represented_place, fill="black", font=font_large, anchor="ms")
            
            # Draw Bottom Text 
            draw.text(coords["category_body"], str(row['category']), fill="black", font=font_regular, anchor="ls")
            draw.text(coords["snatch_body"], str(row['snatch']), fill="black", font=font_regular, anchor="ls")
            draw.text(coords["clean_jerk_body"], str(row['clean_jerk']), fill="black", font=font_regular, anchor="ls")
            draw.text(coords["total_body"], str(row['total']), fill="black", font=font_regular, anchor="ls")
            draw.text(coords["place"], str(row['place']), fill="black", font=font_regular, anchor="ls")
            draw.text(coords["dob_body"], str(row['dob']), fill="black", font=font_regular, anchor="ls")

            # --- AUTOMATIC PHOTO LINKING (UPDATED) ---
            # Supports both .jpg and .jpeg automatically

            photo_path = None
            for ext in ["jpg", "jpeg", "png"]:
                photo_filename = f"photo{row['slno']}.{ext}"
                temp_path = os.path.join(photos_folder, photo_filename)
                if os.path.exists(temp_path):
                    photo_path = temp_path
                    break

            if photo_path:
                try:
                    original_photo = Image.open(photo_path)
                    
                    photo_1 = original_photo.resize(photo_size_1, Image.Resampling.LANCZOS)
                    img.paste(photo_1, photo_box_1_xy)
                    
                    photo_2 = original_photo.resize(photo_size_2, Image.Resampling.LANCZOS)
                    img.paste(photo_2, photo_box_2_xy)
                except Exception as e:
                    print(f"Error processing photo for {row['name']}: {e}")
            else:
                print(f"Warning: No image found for {row['name']}")

            # Save the final certificate
            safe_name = str(row['name']).replace(" ", "_")
            output_filename = os.path.join(output_folder, f"{row['slno']}_{safe_name}.jpg")
            img.save(output_filename)
            success_count += 1
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed on {row['name']}: {str(e)}")
            return

    # Show success popup when done!
    messagebox.showinfo("Success!", f"Successfully generated {success_count} certificates in the '{output_folder}' folder.")


# --- GRAPHICAL USER INTERFACE SETUP ---
root = tk.Tk()
root.title("Rakna Tech - Certificate Generator")
root.geometry("400x200")

label = tk.Label(root, text="Ensure athletes.csv, template.jpg, ARIAL.TTF,\nand a 'Photos' folder are in this directory.", pady=20)
label.pack()

generate_btn = tk.Button(root, text="Generate Certificates", command=generate_bulk_certificates, bg="green", fg="white", font=("Arial", 14, "bold"), pady=10, padx=20)
generate_btn.pack()

root.mainloop()
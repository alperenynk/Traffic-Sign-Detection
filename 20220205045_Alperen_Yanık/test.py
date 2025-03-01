from ultralytics import YOLO
import os

model = YOLO("best.pt")



# Kamera açıp denemek için
# model.predict(source="0", show=True)



# Tekli resim denemek için
# model.predict(source="imgs/30hiz1.jpg", save=True)



# Resimlerin hepsini loop'a alıp denemek için
"""
image_folder = "C:/Users/alper/PycharmProjects/20220205045_Alperen_Yanık/imgs"

for image_file in os.listdir(image_folder):
    if image_file.endswith(('.jpg', '.jpeg', '.png')):  
        image_path = os.path.join(image_folder, image_file)
        print(f"Processing {image_path}...")

        model.predict(source=image_path, save=True)

print("Processing completed.")
"""



# Videoların hepsini loop'a alıp denemek için
"""
video_folder = "C:/Users/alper/PycharmProjects/20220205045_Alperen_Yanık/videos"

for video_file in os.listdir(video_folder):
    if video_file.endswith(('.mp4', '.avi', '.mov')):
        video_path = os.path.join(video_folder, video_file)
        print(f"Processing {video_path}...")

        model.predict(source=video_path, save=True)

print("Processing completed.")
"""
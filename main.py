import cv2
import numpy as np

# Load test video
youtube_video = cv2.VideoCapture('youtube.mp4')  # Replace 'path_to_local_video.mp4' with your local video file path

# Load predicted data (e.g., gaze, emotions, engagement, object interactions)
# Replace the placeholders with actual prediction data
# Example: gaze_predictions[frame_index] = (x, y) coordinates of gaze
gaze_predictions = [(100, 200), (150, 220), (120, 180)]  # Sample gaze predictions
# Example: emotion_predictions[frame_index] = predicted emotion
emotion_predictions = ['Happy', 'Neutral', 'Sad']  # Sample emotion predictions
# Example: engagement_predictions[frame_index] = predicted engagement level
engagement_predictions = ['High', 'Medium', 'Low']  # Sample engagement predictions
# Example: object_predictions[frame_index] = predicted object interaction
object_predictions = ['Playing', 'Reading', 'Drawing']  # Sample object interaction predictions

# Define font and colors for overlay text
font = cv2.FONT_HERSHEY_SIMPLEX
text_color = (255, 255, 255)  # White color

# Process each frame of the video
frame_index = 0
while youtube_video.isOpened():
    print("entry")
    ret, frame = youtube_video.read()
    if not ret:
        break
    
    # Overlay gaze predictions
    print("gaze")
    gaze_x, gaze_y = gaze_predictions[frame_index]
    cv2.circle(frame, (gaze_x, gaze_y), 5, (0, 0, 255), -1)  # Red circle for gaze
    
    # Overlay emotion predictions
    emotion = emotion_predictions[frame_index]
    cv2.putText(frame, emotion, (20, 50), font, 1, text_color, 2, cv2.LINE_AA)
    
    # Overlay engagement predictions
    engagement = engagement_predictions[frame_index]
    cv2.putText(frame, f"Engagement: {engagement}", (20, 100), font, 1, text_color, 2, cv2.LINE_AA)
    
    # Overlay object interaction predictions
    object_interaction = object_predictions[frame_index]
    cv2.putText(frame, f"Object Interaction: {object_interaction}", (20, 150), font, 1, text_color, 2, cv2.LINE_AA)

    # Display the frame
    cv2.imshow('Video with Predictions', frame)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    
    frame_index += 1

# Release video capture and close windows
youtube_video.release()
cv2.destroyAllWindows()

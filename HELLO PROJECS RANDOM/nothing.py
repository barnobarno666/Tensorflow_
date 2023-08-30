



"""
THE CODE IS FULLY COPIED FROM CHATGPT ,SO THATS ALL 
"""
import mediapipe as mp
import cv2

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
cap = cv2.VideoCapture(0)

# Initialize variables for gesture detection
previous_palm_y = None
gesture_detected = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get the vertical position of the palm center
            palm_y = hand_landmarks.landmark[mp_hands.HandLandmark.PALM].y

            # Check if this is the first frame
            if previous_palm_y is None:
                previous_palm_y = palm_y
                continue

            # Calculate the difference in vertical position
            y_diff = palm_y - previous_palm_y

            # Set a threshold for gesture detection
            threshold = 0.05

            # Check for a "wave" gesture
            if y_diff < -threshold:
                gesture_detected = True
                print("Wave Gesture Detected!")

            # Check for a "clap" gesture
            elif y_diff > threshold:
                gesture_detected = True
                print("Clap Gesture Detected!")

            previous_palm_y = palm_y

    cv2.imshow('Gesture Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

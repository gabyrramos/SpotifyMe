import cv2
from deepface import DeepFace

def detect_emotion():
    cap = cv2.VideoCapture(0)
    emotion=None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        
        try:
            # Analyzing emotion
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            emotion = result[0]['dominant_emotion']
        
            # Displaying emotion on the screen
            cv2.putText(frame, f"Emotion: {emotion}", (10, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
            cv2.imshow('Emotion Detector', frame)

        except Exception as e:
            print(f"Error: {e}")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return emotion 
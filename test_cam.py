import cv2

def main():
    # Try opening the default camera
    cap = cv2.VideoCapture(0)

    # Check if camera opened successfully
    if not cap.isOpened():
        print("❌ Error: Could not open webcam.")
        return

    print("✅ Webcam opened successfully. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("❌ Failed to grab frame.")
            break

        # Show the frame
        cv2.imshow("Camera Feed - Press 'q' to exit", frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("👋 Quitting webcam preview.")
            break

    # Release everything
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

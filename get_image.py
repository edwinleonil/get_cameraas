import cv2


def find_cameras(max_tested=10):
    available_cameras = []

    print("Searching for available cameras...")
    for i in range(max_tested):
        cap = cv2.VideoCapture(i)
        if cap is not None and cap.isOpened():
            print(f"Camera found at index {i}")
            available_cameras.append(i)
            cap.release()
        else:
            print(f"No camera at index {i}")

    if not available_cameras:
        print("No cameras were found.")
    else:
        print(f"Available camera indices: {available_cameras}")

    return available_cameras


def display_camera_feed(camera_index):
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print(f"Unable to open camera at index {camera_index}")
        return

    print(
        f"Displaying camera feed from index {camera_index}. Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        cv2.imshow(f"Camera {camera_index}", frame)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    cameras = find_cameras()
    if cameras:
        try:
            selected_index = int(
                input("Enter the index of the camera you want to use: "))
            if selected_index in cameras:
                display_camera_feed(selected_index)
            else:
                print("Invalid camera index selected.")
        except ValueError:
            print("Please enter a valid integer.")

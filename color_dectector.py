import cv2
import numpy as np


def get_color_name(h, s, v):
    """Return a basic color name for a pixel in the HSV color space."""

    # Very dark pixels are usually black
    if v < 50:
        return "Black"

    # Low saturation helps us identify white and gray
    if s < 40 and v > 200:
        return "White"

    if s < 40:
        return "Gray"

    # Classify the remaining pixels by their hue
    if h < 10 or h > 170:
        return "Red"
    elif h < 22:
        return "Orange"
    elif h < 35:
        return "Yellow"
    elif h < 85:
        return "Green"
    elif h < 100:
        return "Cyan"
    elif h < 130:
        return "Blue"
    elif h < 150:
        return "Purple"
    else:
        return "Pink"


def main():
    # Open the default webcam
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Could not open the camera.")
        return

    try:
        while True:
            # Capture a frame from the webcam
            success, frame = camera.read()

            if not success:
                print("Error: Could not read a frame from the camera.")
                break

            # Flip the frame to create a mirror-like view
            frame = cv2.flip(frame, 1)

            # Convert the frame from BGR to HSV
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # Use a smaller copy to make color counting faster
            small = cv2.resize(hsv, (160, 120))

            # Turn the image into a list of HSV pixels
            pixels = small.reshape(-1, 3)

            # Count how many pixels belong to each color
            colors = {}

            for h, s, v in pixels:
                name = get_color_name(int(h), int(s), int(v))
                colors[name] = colors.get(name, 0) + 1

            # Sort colors from the most common to the least common
            sorted_colors = sorted(
                colors.items(),
                key=lambda item: item[1],
                reverse=True
            )

            # Add the project title to the frame
            cv2.putText(
                frame,
                "COLOR DETECTOR",
                (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2
            )

            # Display each detected color and its percentage
            y = 35

            for name, count in sorted_colors:
                if y > 450:
                    break

                percentage = count / len(pixels) * 100
                text = f"{name}: {percentage:.1f}%"

                cv2.putText(
                    frame,
                    text,
                    (20, y + 25),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )

                y += 35

            # Show the processed webcam frame
            cv2.imshow("COLOR DETECTOR", frame)

            # Press Q to quit
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:
        # Always release the webcam and close OpenCV windows
        camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

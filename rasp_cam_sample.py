import picamera
import picamera.array
import cv2

# Create a camera object
camera = picamera.PiCamera()

# Set camera resolution (adjust as needed)
camera.resolution = (640, 480)

# Create a numpy array to store the camera image
with picamera.array.PiRGBArray(camera) as output:
    try:
        # Capture a single frame from the camera
        camera.capture(output, format="bgr")
        frame = output.array

        # You can now use the 'frame' variable with OpenCV for further processing
        # For example, displaying the frame:
        cv2.imshow('Raspberry Pi Camera', frame)
        cv2.waitKey(0)  # Wait for a key press
        cv2.destroyAllWindows()

    finally:
        # Close the camera
        camera.close()

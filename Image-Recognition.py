import cv2
import pytesseract
import os

class AIRecognitionSystem:
    def __init__(self, tesseract_path=None):
        if tesseract_path:
            pytesseract.pytesseract.tesseract_cmd = tesseract_path

    def load_image(self, image_path):
        if not os.path.exists(image_path):
            raise FileNotFoundError("Image not found")
        return cv2.imread(image_path)

    def preprocess(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY)
        return thresh

    def extract_text(self, processed_image):
        return pytesseract.image_to_string(processed_image)

    def detect_faces(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        face_model = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

        faces = face_model.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

        return image, len(faces)

    def display(self, title, image):
        cv2.imshow(title, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def main():
    print("=== AI Image & Text Recognition System ===")

    system = AIRecognitionSystem(
        tesseract_path=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )

    image_path = input("Enter image path: ")

    try:
        image = system.load_image(image_path)

        system.display("Original Image", image)

        processed = system.preprocess(image)
        system.display("Processed Image", processed)

        text = system.extract_text(processed)
        print("\n--- Detected Text ---\n")
        print(text)

        face_img, count = system.detect_faces(image.copy())
        system.display("Face Detection", face_img)

        print(f"\nFaces Detected: {count}")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
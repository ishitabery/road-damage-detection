from ultralytics import YOLO
import cv2

# Load trained model
model = YOLO("best.pt")

# Image path
image_path = "test.jpg"

# Run inference
results = model(image_path)

# Plot results
annotated_frame = results[0].plot()

# Show output
cv2.imshow("Prediction", annotated_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save output
cv2.imwrite("output.jpg", annotated_frame)

print("Inference completed successfully!")

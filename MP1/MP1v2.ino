#define PIR_SENSOR_PIN 27  // Define the pin for the PIR motion sensor
#define LED_PIN 2         // Define the pin for the built-in LED on the ESP32

bool motionDetected = false;  // Variable to track motion detection status

void setup() {
  pinMode(PIR_SENSOR_PIN, INPUT_PULLDOWN);  // Set the PIR sensor pin as input with pull-down resistor
  pinMode(LED_PIN, OUTPUT);                 // Set the LED pin as output
  Serial.begin(115200);                     // Start the Serial communication
}

void loop() {
  bool currentMotionState = digitalRead(PIR_SENSOR_PIN);  // Read the PIR sensor state
  
  if (currentMotionState) {  // If motion is detected
    if (!motionDetected) {  // Check if it was not previously detected
      motionDetected = true;
      digitalWrite(LED_PIN, HIGH);  // Turn on LED when motion is detected
      Serial.println("Movement detected!");
    }
  } else {  // If no motion is detected
    if (motionDetected) {  // Check if it was previously detected
      motionDetected = false;
      digitalWrite(LED_PIN, LOW);  // Turn off LED when motion stops
      Serial.println("No movement.");
    }
  }
}

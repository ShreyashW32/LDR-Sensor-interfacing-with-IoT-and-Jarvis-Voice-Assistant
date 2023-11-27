// Libraries
#include <BoltIoT-Arduino-Helper.h>

// Define LDR Pin
const int ldrPin = A0;

void setup() {
  boltiot.begin(9600); // Initialize Bolt IoT module
  
  // Other setup code
  
}

void loop() {
  int ldrValue = analogRead(ldrPin); // Read LDR sensor value
  boltiot.analogWrite("LDR_Value", ldrValue); // Send LDR value to Bolt IoT platform
  
  // Other loop code
  
  delay(1000); // Delay for stability
}

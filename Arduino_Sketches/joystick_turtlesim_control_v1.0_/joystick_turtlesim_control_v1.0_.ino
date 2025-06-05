// Pin assignments
const int VRx = A0;
const int VRy = A1;
const int SW = 2;

void setup() {
  Serial.begin(9600);
  pinMode(SW, INPUT_PULLUP);
}

void loop() {
  int xValue = analogRead(VRx);
  int yValue = analogRead(VRy);
  int buttonState = digitalRead(SW);

  // Send tab-separated values for ROS
  Serial.print(xValue);
  Serial.print('\t');
  Serial.print(yValue);
  Serial.print('\t');
  Serial.println(buttonState == LOW ? 0 : 1023);

  delay(50);  // Adjust for responsiveness
}

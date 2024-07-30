#define RED_PIN 3
#define GREEN_PIN 2
#define IMG_BUT 5
#define BAR_BUT 6
#define SERVO_BUT 10

#include <Servo.h>
Servo myservo;

int pos = 0;
int imBut;
int caBut;

String cmd;

void servoOpen() {
  for (pos = 0; pos <= 90; pos += 1) {
    myservo.write(pos);
    delay(30);
  }
  delay(6000);
  for (pos = 90; pos >= 0; pos -= 1) {
    myservo.write(pos);
    delay(30);
  }
}
void setup() {
  pinMode(RED_PIN, OUTPUT); // green led
  pinMode(GREEN_PIN, OUTPUT); // red led
  pinMode(IMG_BUT, INPUT); // image button
  pinMode(BAR_BUT, INPUT); // barrier button

  myservo.attach(SERVO_BUT);

  Serial.begin(19200);
}

void loop() {
  imBut = digitalRead(IMG_BUT);
  if (imBut == 1){
    Serial.println("Image");
  }

  caBut = digitalRead(BAR_BUT);
  if (caBut == 1) {
    Serial.println("Barrier");
  }

  cmd = Serial.readStringUntil('\r');
  if (cmd == "GON") digitalWrite(GREEN_PIN, HIGH);
  else if (cmd == "GOF") digitalWrite(GREEN_PIN, LOW);
  else if (cmd == "RON") digitalWrite(RED_PIN, HIGH);
  else if (cmd == "ROF") digitalWrite(RED_PIN, LOW);
  else if (cmd == "OPEN") servoOpen();
}

#include <SoftwareSerial.h>
#include <Servo.h>
#include <ServoEasing.hpp>
ServoEasing servo01;
ServoEasing servo02;
ServoEasing servo03;
ServoEasing servo04;
ServoEasing servo05;
ServoEasing servo06;

SoftwareSerial Bluetooth(3, 4); // Arduino(RX, TX) - HC-05 Bluetooth (TX, RX)
int servo1Pos, servo2Pos, servo3Pos, servo4Pos, servo5Pos, servo6Pos; // current position
int servo1PPos, servo2PPos, servo3PPos, servo4PPos, servo5PPos, servo6PPos; // previous position
int servo01SP[50], servo02SP[50], servo03SP[50], servo04SP[50], servo05SP[50], servo06SP[50]; // for storing positions/steps
int speedDelay = 50; // 25
int index = 0;
String dataIn = "";
void setup() {
  
  servo01.attach(5);
  servo02.attach(6);
  servo03.attach(7);
  servo04.attach(11);
  servo05.attach(9);
  servo06.attach(10);
  Bluetooth.begin(115200); // Default baud rate of the Bluetooth module
  
  servo01.setSpeed(45);
  servo02.setSpeed(45);
  servo03.setSpeed(45);
  servo04.setSpeed(45);
  servo05.setSpeed(45);
  servo06.setSpeed(70);

 
  
  //Serial.begin(9600);
  //Bluetooth.setTimeout(1);
  delay(200);
  // Robot arm initial position
  servo1PPos = 100;
  servo01.write(servo1PPos);
  delay(200);
  servo2PPos = 85; //90
  servo02.write(servo2PPos);
  delay(200);
  servo3PPos = 92;
  servo03.write(servo3PPos);
  delay(200);
  servo4PPos = 40;
  servo04.write(servo4PPos);
  delay(200);
  servo5PPos = 70;
  servo05.write(servo5PPos);
  delay(200);
  servo6PPos = 50;
  //44
  servo06.write(servo6PPos);
  delay(100);
  //Serial.write("Done Initi");
  //Serial.println("");
}
void loop() {
  // Check for incoming data
  if (Bluetooth.available() > 0) {
    dataIn = Bluetooth.readString();  // Read the data as string
    
    // If "Waist" slider has changed value - Move Servo 1 to position
    if (dataIn.startsWith("s1")) {
      String dataInS = dataIn.substring(2, dataIn.length()); // Extract only the number. E.g. from "s1120" to "120"
      servo1Pos = dataInS.toInt();  // Convert the string into integer
      // We use for loops so we can control the speed of the servo
      // If previous position is bigger then current position
    servo01.setEasingType(EASE_QUADRATIC_IN_OUT);
      servo01.startEaseTo(servo1Pos);
      servo1PPos = servo1Pos;   // set current position as previous position
    }
    
    // Move Servo 2
    if (dataIn.startsWith("s2")) {
      String dataInS = dataIn.substring(2, dataIn.length());
      servo2Pos = dataInS.toInt();
      servo02.setEasingType(EASE_QUADRATIC_IN_OUT);
     servo02.startEaseTo(servo2Pos);
     servo2PPos = servo2Pos;
    }
    // Move Servo 3
    if (dataIn.startsWith("s3")) {
      String dataInS = dataIn.substring(2, dataIn.length());
      servo3Pos = dataInS.toInt();
      servo03.setEasingType(EASE_QUADRATIC_IN_OUT);
      servo03.startEaseTo(servo3Pos);
      servo3PPos = servo3Pos;
    }
    // Move Servo 4
    if (dataIn.startsWith("s4")) {
      String dataInS = dataIn.substring(2, dataIn.length());
      servo4Pos = dataInS.toInt();
      servo04.setEasingType(EASE_QUADRATIC_IN_OUT);
      servo04.startEaseTo(servo4Pos);
      servo4PPos = servo4Pos;
    }
    // Move Servo 5
    if (dataIn.startsWith("s5")) {
      String dataInS = dataIn.substring(2, dataIn.length());
      servo5Pos = dataInS.toInt();
      servo05.setEasingType(EASE_QUADRATIC_IN_OUT);
      servo05.startEaseTo(servo5Pos);
      servo5PPos = servo5Pos;
    }
    // Move Servo 6
    if (dataIn.startsWith("s6")) {
      String dataInS = dataIn.substring(2, dataIn.length());
      servo6Pos = dataInS.toInt();
      servo06.setEasingType(EASE_QUADRATIC_IN_OUT);
      servo06.startEaseTo(servo6Pos);
      servo6PPos = servo6Pos; 
    }
    // If button "SAVE" is pressed
    if (dataIn.startsWith("SAVE")) {
      servo01SP[index] = servo1PPos;  // save position into the array
      servo02SP[index] = servo2PPos;
      servo03SP[index] = servo3PPos;
      servo04SP[index] = servo4PPos;
      servo05SP[index] = servo5PPos;
      servo06SP[index] = servo6PPos;
      index++;                        // Increase the array index
    }
    // If button "RUN" is pressed
    if (dataIn.startsWith("RUN")) {
      runservo();  // Automatic mode - run the saved steps 
    }
    // If button "RESET" is pressed
    if ( dataIn == "RESET") {
      memset(servo01SP, 0, sizeof(servo01SP)); // Clear the array data to 0
      memset(servo02SP, 0, sizeof(servo02SP));
      memset(servo03SP, 0, sizeof(servo03SP));
      memset(servo04SP, 0, sizeof(servo04SP));
      memset(servo05SP, 0, sizeof(servo05SP));
      memset(servo06SP, 0, sizeof(servo06SP));
      index = 0;  // Index to 0
    }
  }
}
// Automatic mode custom function - run the saved steps
void runservo() {
  while (dataIn != "RESET") {   // Run the steps over and over again until "RESET" button is pressed
    for (int i = 0; i <= index - 2; i++) {  // Run through all steps(index)
      if (Bluetooth.available() > 0) {      // Check for incomding data
        dataIn = Bluetooth.readString();
        if ( dataIn == "PAUSE") {           // If button "PAUSE" is pressed
          while (dataIn != "RUN") {         // Wait until "RUN" is pressed again
            if (Bluetooth.available() > 0) {
              dataIn = Bluetooth.readString();
              if ( dataIn == "RESET") {     
                break;
              }
            }
          }
        }
        // If speed slider is changed
        if (dataIn.startsWith("ss")) {
          String dataInS = dataIn.substring(2, dataIn.length());
          speedDelay = dataInS.toInt(); // Change servo speed (delay time)
        }
      }
      // Servo 1
      if (servo01SP[i] == servo01SP[i + 1]) {
      }
      if (servo01SP[i] > servo01SP[i + 1]) {
        for ( int j = servo01SP[i]; j >= servo01SP[i + 1]; j--) {
          servo01.startEaseTo(j);
          delay(speedDelay);
        }
      }
      if (servo01SP[i] < servo01SP[i + 1]) {
        for ( int j = servo01SP[i]; j <= servo01SP[i + 1]; j++) {
          servo01.startEaseTo(j);
          delay(speedDelay);
        }
      }
      // Servo 2
      if (servo02SP[i] == servo02SP[i + 1]) {
      }
      if (servo02SP[i] > servo02SP[i + 1]) {
        for ( int j = servo02SP[i]; j >= servo02SP[i + 1]; j--) {
          servo02.startEaseTo(j);
          delay(speedDelay);
        }
      }
      if (servo02SP[i] < servo02SP[i + 1]) {
        for ( int j = servo02SP[i]; j <= servo02SP[i + 1]; j++) {
          servo02.startEaseTo(j);
          delay(speedDelay);
        }
      }
      // Servo 3
      if (servo03SP[i] == servo03SP[i + 1]) {
      }
      if (servo03SP[i] > servo03SP[i + 1]) {
        for ( int j = servo03SP[i]; j >= servo03SP[i + 1]; j--) {
          servo03.startEaseTo(j);
          delay(speedDelay);
        }
      }
      if (servo03SP[i] < servo03SP[i + 1]) {
        for ( int j = servo03SP[i]; j <= servo03SP[i + 1]; j++) {
          servo03.startEaseTo(j);
          delay(speedDelay);
        }
      }
      // Servo 4
      if (servo04SP[i] == servo04SP[i + 1]) {
      }
      if (servo04SP[i] > servo04SP[i + 1]) {
        for ( int j = servo04SP[i]; j >= servo04SP[i + 1]; j--) {
          servo04.startEaseTo(j);
          delay(speedDelay);
        }
      }
      if (servo04SP[i] < servo04SP[i + 1]) {
        for ( int j = servo04SP[i]; j <= servo04SP[i + 1]; j++) {
          servo04.startEaseTo(j);
          delay(speedDelay);
        }
      }
      // Servo 5
      if (servo05SP[i] == servo05SP[i + 1]) {
      }
      if (servo05SP[i] > servo05SP[i + 1]) {
        for ( int j = servo05SP[i]; j >= servo05SP[i + 1]; j--) {
          servo05.startEaseTo(j);
          delay(speedDelay);
        }
      }
      if (servo05SP[i] < servo05SP[i + 1]) {
        for ( int j = servo05SP[i]; j <= servo05SP[i + 1]; j++) {
          servo05.startEaseTo(j);
          delay(speedDelay);
        }
      }
      // Servo 6
      if (servo06SP[i] == servo06SP[i + 1]) {
      }
      if (servo06SP[i] > servo06SP[i + 1]) {
        for ( int j = servo06SP[i]; j >= servo06SP[i + 1]; j--) {
          servo06.startEaseTo(j);
          delay(speedDelay);
        }
      }
      if (servo06SP[i] < servo06SP[i + 1]) {
        for ( int j = servo06SP[i]; j <= servo06SP[i + 1]; j++) {
          servo06.startEaseTo(j);
          delay(speedDelay);
        }
      }
    }
  }
}

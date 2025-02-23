#include <SoftwareSerial.h>
#include <Servo.h>
Servo servo01;
Servo servo02;
Servo servo03;
Servo servo04;
Servo servo05;
Servo servo06;

int servo1Pos, servo2Pos, servo3Pos, servo4Pos, servo5Pos, servo6Pos; // current position
int servo1PPos, servo2PPos, servo3PPos, servo4PPos, servo5PPos, servo6PPos; // previous position
int servo01SP[50], servo02SP[50], servo03SP[50], servo04SP[50], servo05SP[50], servo06SP[50]; // for storing positions/steps
int speedDelay = 25;
int index = 0;
String dataIn = "";
void setup() {
  servo01.attach(5);
  servo02.attach(6);
  servo03.attach(7);
  servo04.attach(8);
  servo05.attach(9);
  servo06.attach(10);
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

  servo1Pos = servo1PPos;
  servo2Pos = servo2PPos+80;
  servo3Pos = servo2PPos;
  servo4Pos = servo4PPos;
  servo5Pos = servo5PPos;
  servo6Pos = servo6PPos;

  delay(1000);

}

void loop() {

      if (servo1PPos > servo1Pos) {
        for ( int j = servo1PPos; j >= servo1Pos; j--) {   // Run servo down
          servo01.write(j);
          delay(30);    // defines the speed at which the servo rotates
        }
      }
      // If previous position is smaller then current position
      if (servo1PPos < servo1Pos) {
        for ( int j = servo1PPos; j <= servo1Pos; j++) {   // Run servo up
          servo01.write(j);
          delay(20);
        }
      }
      servo1PPos = servo1Pos;   // set current position as previous position
    delay(1000);
    
    // Move Servo 2

      if (servo2PPos > servo2Pos) {
        for ( int j = servo2PPos; j >= servo2Pos; j--) {
          servo02.write(j);
          delay(60);
        }
      }
      if (servo2PPos < servo2Pos) {
        for ( int j = servo2PPos; j <= servo2Pos; j++) {
          servo02.write(j);
          delay(60);
        }
      }
      servo2PPos = servo2Pos;
    delay(1000);
    // Move Servo 3

      if (servo3PPos > servo3Pos) {
        for ( int j = servo3PPos; j >= servo3Pos; j--) {
          servo03.write(j);
          delay(40);
        }
      }
      if (servo3PPos < servo3Pos) {
        for ( int j = servo3PPos; j <= servo3Pos; j++) {
          servo03.write(j);
          delay(40);
        }
      }
      servo3PPos = servo3Pos;
    delay(1000);

    
    // Move Servo 4

      if (servo4PPos > servo4Pos) {
        for ( int j = servo4PPos; j >= servo4Pos; j--) {
          servo04.write(j);
          delay(40);
        }
      }
      if (servo4PPos < servo4Pos) {
        for ( int j = servo4PPos; j <= servo4Pos; j++) {
          servo04.write(j);
          delay(40);
        }
      }
      servo4PPos = servo4Pos;
    delay(1000);

    
    // Move Servo 5

      if (servo5PPos > servo5Pos) {
        for ( int j = servo5PPos; j >= servo5Pos; j--) {
          servo05.write(j);
          delay(40);
        }
      }
      if (servo5PPos < servo5Pos) {
        for ( int j = servo5PPos; j <= servo5Pos; j++) {
          servo05.write(j);
          delay(40);
        }
      }
      servo5PPos = servo5Pos;
    delay(1000);

    
    // Move Servo 6
      if (servo6PPos > servo6Pos) {
        for ( int j = servo6PPos; j >= servo6Pos; j--) {
          servo06.write(j);
          delay(40);
        }
      }
      if (servo6PPos < servo6Pos) {
        for ( int j = servo6PPos; j <= servo6Pos; j++) {
          servo06.write(j);
          delay(40);
        }
      }
      servo6PPos = servo6Pos; 
    delay(1000);
    
    }
  

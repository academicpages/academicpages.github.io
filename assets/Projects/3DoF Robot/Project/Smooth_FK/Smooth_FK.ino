#include <SoftwareSerial.h>
#include <Servo.h>
#include <ServoEasing.hpp>
ServoEasing servo01;
ServoEasing servo02;
ServoEasing servo03;
ServoEasing servo04;
ServoEasing servo05;
ServoEasing servo06;

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


  servo01.setSpeed(40);
  servo02.setSpeed(40);
  servo03.setSpeed(40);
  servo04.setSpeed(40);
  servo05.setSpeed(40);
  servo06.setSpeed(70);




  
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

    servo01.setEasingType(EASE_QUADRATIC_IN_OUT);
      servo01.startEaseTo(servo1Pos);
      servo1PPos = servo1Pos;   // set current position as previous position
    delay(1000);
    
    // Move Servo 2

           servo02.setEasingType(EASE_QUADRATIC_IN_OUT);
     servo02.startEaseTo(servo2Pos);
     
      servo2PPos = servo2Pos;
    delay(1000);
    // Move Servo 3

            servo03.setEasingType(EASE_QUADRATIC_IN_OUT);
      servo03.startEaseTo(servo3Pos);
      servo3PPos = servo3Pos;
    delay(1000);

    
    // Move Servo 4

      servo04.setEasingType(EASE_QUADRATIC_IN_OUT);
      servo04.startEaseTo(servo4Pos);
      servo4PPos = servo4Pos;
    delay(1000);

    
    // Move Servo 5

            servo05.setEasingType(EASE_QUADRATIC_IN_OUT);
      servo05.startEaseTo(servo5Pos);
      servo5PPos = servo5Pos;
    delay(1000);

    
    // Move Servo 6
    servo06.setEasingType(EASE_QUADRATIC_IN_OUT);
      servo06.startEaseTo(servo6Pos);
      servo6PPos = servo6Pos; 
    delay(1000);
    
    }
  

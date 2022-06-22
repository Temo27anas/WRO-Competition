//Taipan Arduino MEGA Code
//Copyright : Abderrahman ELARFAOUI & Anas Temouden 
//Al Akhawayn University in Ifrane - Machatronics Team
//June 25, 2022
//World Robots Olympiads
//Free to share


#include <Servo.h>

Servo servoR; 
Servo servoL;
Servo grip_servo;
Servo rot_servo;
Servo mServo1;
Servo mServo2;
Servo mServo3;
Servo mServo4;

int pos=90;
int grip_flag=0;

void setup() {
  servoR.attach(6);
  servoL.attach(5);
  grip_servo.attach(7);
  rot_servo.attach(8);
  mServo1.attach(4);
  mServo2.attach(1);
  mServo3.attach(2);
  mServo4.attach(3);

  
  grip_servo.write(90);
  rot_servo.write(90);
  delay(500);
  Serial.begin(9600);
}

void openStbs(){
  mServo1.write(180);
  mServo2.write(180);
  mServo3.write(180);
  mServo4.write(180);
  delay(500);
}

void closeStbs(){
  mServo1.write(0);
  mServo2.write(0);
  mServo3.write(0);
  mServo4.write(0);
  delay(500);
}


void loop() {

  char byte=0;
  while (true){
    Serial.readBytes(&byte, 1);
    if(byte== 'q'){
      servoR.write(180);
      delay(35);
      byte=0;
    }
    if(byte=='d'){
      servoR.write(0);
      delay(35);
      byte=0;
    }
    if(byte=='z'){
      servoL.write(0);
      delay(100);
      byte=0;
    }
    if(byte=='s'){
      servoL.write(180);
      delay(100);
      byte=0;
    }
    if(byte=='w'){
      if(grip_flag==0){
        grip_servo.write(155);
        Serial.println("Gripper Closed");
        delay(400);
        grip_flag=1;
        } else {
        grip_servo.write(90);
        Serial.println("Gripper Opened");
        delay(400);
        grip_flag=0;
        }
        byte=0;  
    }
    if(byte=='c' && pos < 180){
      pos+=10;
      rot_servo.write(pos);
      Serial.println("Griper turns left : " + String(pos) + "°");
      delay(30);
      byte=0;
    }
    if(byte=='v'&& pos> 0){
      pos-=10;
      rot_servo.write(pos);
      Serial.println("Griper turns right : " + String(pos) + "°");
      delay(30);
      byte=0;
    }
    if(byte==0){
      servoR.write(90);
      servoL.write(90);
      byte=0;
    }
    servoR.write(90);
    servoL.write(90);
  
  
  }
 
    
}

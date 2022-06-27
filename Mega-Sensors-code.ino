// FINAAAAAAAAAAAAAAAAAAAALLLLLLLLLLLLL



#include "DHT.h"
int sensorValueCO2;
#define USE_ARDUINO_INTERRUPTS true    
#include <PulseSensorPlayground.h>       

//  Variables
const int PulseWire = 3;       
const int LED13 = 13;          
int Threshold = 550; 
PulseSensorPlayground pulseSensor;

DHT dht(53, DHT11);
//

#include "Wire.h"

const int MPU_addr=0x68; int16_t AcX,AcY,AcZ,Tmp,GyX,GyY,GyZ;

int minVal=265; int maxVal=402;

double x; double y; double z;



void setup() {
  Serial.begin(9600);
//
Wire.begin();
Wire.beginTransmission(MPU_addr);
Wire.write(0x6B);
Wire.write(0);
Wire.endTransmission(true);
//
  dht.begin();
  pulseSensor.analogInput(PulseWire);   
  pulseSensor.blinkOnPulse(LED13);       //auto-magically blink Arduino's LED with heartbeat.
  pulseSensor.setThreshold(Threshold); 

   if (pulseSensor.begin()) {
    Serial.print("");  //This prints one time at Arduino power-up,  or on Arduino reset.  
  }
}

void loop() {


  float h = dht.readHumidity();
  float t = dht.readTemperature();
  sensorValueCO2 = analogRead(0)*5;

 int myBPM = pulseSensor.getBeatsPerMinute();


//
Wire.beginTransmission(MPU_addr);
Wire.write(0x3B);
Wire.endTransmission(false);
Wire.requestFrom(MPU_addr,14,true);
AcX=Wire.read()<<8|Wire.read();
AcY=Wire.read()<<8|Wire.read();
AcZ=Wire.read()<<8|Wire.read();
int xAng = map(AcX,minVal,maxVal,-90,90);
int yAng = map(AcY,minVal,maxVal,-90,90);
int zAng = map(AcZ,minVal,maxVal,-90,90);

x= RAD_TO_DEG * (atan2(-yAng, -zAng)+PI);
y= RAD_TO_DEG * (atan2(-xAng, -zAng)+PI);
z= RAD_TO_DEG * (atan2(-yAng, -xAng)+PI);

x = x - 193;
y = y- 175;
z=z-295;
//









Serial.print(myBPM);
  Serial.print(",");
  Serial.print(sensorValueCO2);
  Serial.print(",");
  Serial.print(t);
  Serial.print(",");
  Serial.print(h);
  Serial.print(",");
  Serial.print(x);
  Serial.print(",");
  Serial.print(y);
  Serial.print(",");
  Serial.print(z);
  Serial.println(",");
  
  delay(500);


}

#define USE_ARDUINO_INTERRUPTS true
#include <PulseSensorPlayground.h>


PulseSensorPlayground pulse_sensor; 

void setup() {
  Serial.begin(9600);
  pulse_sensor.analogInput(3); 
  pulse_sensor.blinkOnPulse(13); 
  pulse_sensor.setThreshold(513); 
  
  if (pulse_sensor.begin()) {
    //Serial.println("PulseSensor object created!");
  }

}

void loop() {

  //---------Random Data-----------
  int BPM = pulse_sensor.getBeatsPerMinute(); ;
  double CO2 = 7.5 ;
  double AmbientT= ((float) rand()/ RAND_MAX) ;
  double AmbientH= ((float) rand()/ RAND_MAX);
  double BodyT= ((float) rand()/ RAND_MAX) ;
  double Gyro= ((float) rand()/ RAND_MAX) ;
  double Speed= ((float) rand()/ RAND_MAX) ;


  //--------------BPM-----------------------
  
  Serial.println(BPM); 
  //----------------Send Data----------------
  /*Serial.print(BPM);
  Serial.print(",");
  Serial.print(CO2);
  Serial.print(",");
  Serial.print(AmbientT);
  Serial.print(",");
  Serial.print(AmbientH);
  Serial.print(",");
  Serial.print(BodyT);
  Serial.print(",");
  Serial.print(Gyro);
  Serial.print(",");
  Serial.print(Speed);
  Serial.print(",");
  Serial.println();*/



  delay(200);
}


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  //define temperature 
 
}

void loop() {
  // put your main code here, to run repeatedly:
  // Prdouble Temperature
  
 double Heartbeat = ((float) rand()/ RAND_MAX) ;
 double CO2 = ((float) rand()/ RAND_MAX) ;
 double AmbientT= ((float) rand()/ RAND_MAX) ;
 double AmbientH= ((float) rand()/ RAND_MAX) ;
 double BodyT= ((float) rand()/ RAND_MAX) ;
 double Gyro= ((float) rand()/ RAND_MAX) ;
 double Speed= ((float) rand()/ RAND_MAX) ;


  Serial.print(Heartbeat);
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

  


 //*******************************************************

  Serial.println();



}

 

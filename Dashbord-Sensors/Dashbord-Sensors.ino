
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  //define temperature 
 
}

void loop() {
  // put your main code here, to run repeatedly:
  // Prdouble Temperature
  
  //---------Random Data-----------
  double Heartbeat  = 80;
  //pulse_sensor.getBeatsPerMinute(); ;
  double CO2 = 534 ;
  double AmbientT= 24 ;
  double AmbientH= 56;
  double GyroX= 0.1;
  double GyroY= 0.1;
  double GyroZ= 0.1;
  double Speed= 0.9;


  //--------------BPM-----------------------
  
  //----------------Send Data----------------
  Serial.print(Heartbeat);
  Serial.print(",");
  Serial.print(CO2);
  Serial.print(",");
  Serial.print(AmbientT);
  Serial.print(",");
  Serial.print(AmbientH);
  Serial.print(",");
  Serial.print(GyroX);
  Serial.print(",");
  Serial.print(GyroY);
  Serial.print(",");
  Serial.print(GyroZ);
  Serial.print(",");
  Serial.print(Speed);
  Serial.print(",");
  
  
  
  
  
  Serial.println();
  delay(200);


}

 

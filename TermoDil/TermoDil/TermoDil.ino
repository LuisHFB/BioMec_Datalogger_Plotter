long randNumber;
long randNumber2;
long randNumber3;
void setup() {
  //Initialize serial and wait for port to open:
 Serial.begin(9600);
 while (!Serial) {
 ; // wait for serial port to connect. Needed for native USB port only
 randomSeed(analogRead(0));
  }
}
void loop() {
   randNumber = random(300);
   randNumber2 = random(17);
   randNumber3 = random(50);
   
  Serial.print("###");
  Serial.print(randNumber);
  Serial.print("T,");
  Serial.print(randNumber2);
  Serial.print("P1,");
  Serial.print(randNumber3);
  Serial.print("P2");
  Serial.println("\n");
  
  delay(100);
}

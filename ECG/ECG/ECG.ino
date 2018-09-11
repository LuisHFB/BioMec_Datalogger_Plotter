float randNumber;
void setup() {
  //Initialize serial and wait for port to open:
 Serial.begin(9600);
 while (!Serial) {
 ; // wait for serial port to connect. Needed for native USB port only
 randomSeed(analogRead(0));
  }
}
void loop() {
   randNumber = random(1, 500) / 100.0;
   
  Serial.print("###");
  Serial.print(randNumber);
  Serial.println("\n");
  
  delay(300);
}

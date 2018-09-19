#define core A0
#define pinECG 1
#define pin_FC 2


void setup() {
  Serial.begin (19200);
  pinMode(pin_FC, INPUT);
  }

void loop() {
  bool continua=true;
  bool Sensor_FC;
  float RR;
  float Fator_t=1.0; 
  bool PrimeiroValor=true;
  float T1=0;
  float T2;
  int cont=0;
  float  cora = analogRead(core);
  Serial.print("###");
  Serial.print(cora);
  Serial.println("\n");
   do {
    cora = analogRead(core);
    Serial.print("###");
    Serial.print(cora);
    Serial.println("\n");
      
     Sensor_FC=digitalRead(pin_FC);
     //Serial.print("Sensor_FC= ");   
     //Serial.println(Sensor_FC);
    if ((Sensor_FC)&&(PrimeiroValor)){
      T2=millis();
      PrimeiroValor=false;
      RR=Fator_t*(T2-T1)/1000;
      Serial.print("RRR");
      Serial.print(RR);
      Serial.println("\n");
      if(T1!=0.0){
        Serial.print("FFF");
        Serial.print(1/RR*60);
        Serial.println("\n");
      }
    }
    Sensor_FC=digitalRead(pin_FC);
    //Serial.print("Sensor_FC= ");   
    //Serial.println(Sensor_FC);
    if(!Sensor_FC){
      PrimeiroValor=true;
      T1=T2;
    }
  }while (continua);

}

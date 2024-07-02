/*int ledPin = 2;              
int inputPin = 27;            
int pirState = LOW;             
int val = 0;          
void setup() {
  pinMode(ledPin, OUTPUT);      
  pinMode(inputPin, INPUT);     

  Serial.begin(115200);
} 
void loop(){
  val = digitalRead(inputPin);    
  if (val == HIGH)  
  {            
    digitalWrite(ledPin, HIGH);  
  
    if (pirState == LOW) 
  {
      Serial.println("Motion detected!"); 
      pirState = HIGH;
    }
  } 
  else 
  {
    digitalWrite(ledPin, LOW); 
    if (pirState == HIGH)
  {
      Serial.println("Motion detection stopped.");  
      pirState = LOW;
    }
  }
}*/
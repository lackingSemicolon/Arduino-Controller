    const int buttonpin1=A0;
    const int buttonpin2=A1;
    int pot=A0;
    int potval=0;
    int buttonstate=0;
    int buttonstate2=0;
void setup() 
{
  // put your setup code here, to run once:
    pinMode(buttonpin1, INPUT);
    digitalWrite(buttonpin1,HIGH);
    pinMode(buttonpin2, INPUT);
    digitalWrite(buttonpin2,HIGH);
    Serial.begin(9600);
}

void loop() 
{
  // put your main code here, to run repeatedly:
    buttonstate=digitalRead(buttonpin1);
    buttonstate2=digitalRead(buttonpin2);
    potval=analogRead(pot);
    
//    Serial.println(buttonpin1);
//    Serial.println(buttonpin2);
    
    if (buttonstate == 1) // Check wires read should be on 1, + on 2, - on 3
    {
      Serial.println(1);
    }
    else if (buttonstate2 ==1) //button 2 right.
    {
      Serial.println(2);
    }
    delay(80); //lower number = more sensitive
}

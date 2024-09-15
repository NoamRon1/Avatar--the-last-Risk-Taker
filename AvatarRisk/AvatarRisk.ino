#include <Adafruit_NeoPixel.h>


int NeoPixelLedsNum = 12;
int NeoPixelPinTR = 3;
int NeoPixelPinTL = 5;
int NeoPixelPinBR = 6;
int NeoPixelPinBL = 9;
int a;
int b;
int c;
// TR = TopRight, TL = TopLeft, BR = ButtomRight, BL = ButtomLeft

Adafruit_NeoPixel NeoPixelTR = Adafruit_NeoPixel(NeoPixelLedsNum, NeoPixelPinTR, NEO_GRB + NEO_KHZ800); //make NEO_GRB to NEO_RGB if needed
Adafruit_NeoPixel NeoPixelTL = Adafruit_NeoPixel(NeoPixelLedsNum, NeoPixelPinTL, NEO_GRB + NEO_KHZ800); //make NEO_GRB to NEO_RGB if needed
Adafruit_NeoPixel NeoPixelBR = Adafruit_NeoPixel(NeoPixelLedsNum, NeoPixelPinBR, NEO_GRB + NEO_KHZ800); //make NEO_GRB to NEO_RGB if needed
Adafruit_NeoPixel NeoPixelBL = Adafruit_NeoPixel(NeoPixelLedsNum, NeoPixelPinBL, NEO_GRB + NEO_KHZ800); //make NEO_GRB to NEO_RGB if needed


bool last_stat = digitalRead(2);
int playerTurn = 0;
bool safecheck = false;


bool CheckButton(){
  bool stat = digitalRead(2);
  Serial.print("the thingy: ");
  Serial.println(digitalRead(2));
  if (stat == 1){
    if (safecheck == true){
      playerTurn++;
      if (playerTurn > 3){
        playerTurn = 0;
      safecheck = false;
      }
    }
    else{
      safecheck = true;
    }
  }
  Serial.println(playerTurn);
  last_stat = stat;
  delay(2000);
  }

void setup() {
  // put your setup code here, to run once:
  // inmode(3, OUTPUT);
  Serial.begin(9600);
  NeoPixelTR.begin();
  Serial.print(random(0, 255));
  pinMode(2, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(2), CheckButton, FALLING);
  Serial.println("Setupy Finished");

}


void loop() {
  // put your main code here, to run repeatedly:
  // Serial.println(digitalRead(2));
  switch (playerTurn){
    case 0: // TR
      Serial.print("TopRight Player Turn ");
      for (int i=0; i<12; i++){
        a = random(0, 255);
        b = random(0, 255);
        c = random(0, 255);
        NeoPixelTR.setPixelColor(i, NeoPixelTR.Color(a,b,c)); // Moderately bright green color.
      }
      NeoPixelTL.fill(NeoPixelTR.Color(255, 0, 0));
      NeoPixelBR.fill(NeoPixelTR.Color(255, 0, 0));
      NeoPixelBL.fill(NeoPixelTR.Color(255, 0, 0));
      NeoPixelTR.show();
      NeoPixelTL.show();
      NeoPixelBR.show();
      NeoPixelBL.show();
      Serial.print(a);
      Serial.print(" ");
      Serial.print(b);
      Serial.print(" ");
      Serial.print(c);
      Serial.print(" ");
      Serial.println(playerTurn);
      delay(250);
      break;
    case 1:
      Serial.print("TopLeft Player Turn ");
      for (int i=0; i<12; i++){
        a = random(0, 255);
        b = random(0, 255);
        c = random(0, 255);
        NeoPixelTL.setPixelColor(i, NeoPixelTR.Color(a,b,c)); // Moderately bright green color.
      }
      NeoPixelTR.fill(NeoPixelTR.Color(255, 0, 0));
      NeoPixelBR.fill(NeoPixelTR.Color(255, 0, 0));
      NeoPixelBL.fill(NeoPixelTR.Color(255, 0, 0));
      NeoPixelTR.show();
      NeoPixelTL.show();
      NeoPixelBR.show();
      NeoPixelBL.show();
      Serial.print(a);
      Serial.print(" ");
      Serial.print(b);
      Serial.print(" ");
      Serial.print(c);
      Serial.print(" ");
      Serial.println(playerTurn);
      delay(250);
      break;
    case 2:
      Serial.print("ButtonRight Player Turn ");
      for (int i=0; i<12; i++){
        a = random(0, 255);
        b = random(0, 255);
        c = random(0, 255);
        NeoPixelBR.setPixelColor(i, NeoPixelTR.Color(a,b,c)); // Moderately bright green color.
      }
      NeoPixelTL.fill(NeoPixelTR.Color(255, 0, 0));
      NeoPixelTR.fill(NeoPixelTR.Color(255, 0, 0));
      NeoPixelBL.fill(NeoPixelTR.Color(255, 0, 0));
      NeoPixelTR.show();
      NeoPixelTL.show();
      NeoPixelBR.show();
      NeoPixelBL.show();
      Serial.print(a);
      Serial.print(" ");
      Serial.print(b);
      Serial.print(" ");
      Serial.print(c);
      Serial.print(" ");
      Serial.println(playerTurn);      delay(250);
      break;
    case 3:
      Serial.print("ButtonLeft Player Turn ");
      for (int i=0; i<12; i++){
        a = random(0, 255);
        b = random(0, 255);
        c = random(0, 255);
        NeoPixelBL.setPixelColor(i, NeoPixelTR.Color(a,b,c)); // Moderately bright green color.
      }
      NeoPixelTL.fill(NeoPixelTR.Color(255, 0, 0));
      NeoPixelBR.fill(NeoPixelTR.Color(255, 0, 0));
      NeoPixelTR.fill(NeoPixelTR.Color(255, 0, 0));
      NeoPixelTR.show();
      NeoPixelTL.show();
      NeoPixelBR.show();
      NeoPixelBL.show();
      Serial.print(a);
      Serial.print(" ");
      Serial.print(b);
      Serial.print(" ");
      Serial.print(c);
      Serial.print(" ");
      Serial.println(playerTurn);
      delay(250);
      break;
  }


}

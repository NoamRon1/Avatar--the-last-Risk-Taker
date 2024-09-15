#include <Adafruit_NeoPixel.h>
#include "ButtonIRQ.h"


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


ButtonIRQ CircleButtons(2);

bool last_stat = CircleButtons.isTrue();
int playerTurn = 0;


bool CheckButton(){
  playerTurn++;
  Serial.println("yes");
  if (playerTurn > 3){
    playerTurn = 0;
  }
}

void setup() {
  // put your setup code here, to run once:
  // inmode(3, OUTPUT);
  Serial.begin(9600);
  NeoPixelTR.begin();
  Serial.print(random(0, 255));
  pinMode(2, INPUT);
  attachInterrupt(digitalPinToInterrupt(2), CheckButton, RISING);
  Serial.println("Setupy Finished");

}


void loop() {
  // put your main code here, to run repeatedly:
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
      Serial.println(c);
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
      Serial.println(c);
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
      Serial.println(c);
      delay(250);
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
      Serial.println(c);
      delay(250);
      break;
  }


}

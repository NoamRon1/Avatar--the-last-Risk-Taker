#include <Adafruit_NeoPixel.h>
#include "ButtonIRQ.h"


int NeoPixelLedsNum = 10;
int NeoPixelPinTR = 2;
int NeoPixelPinTL = 1;
int NeoPixelPinBR = 8;
int NeoPixelPinBL = 8;

// TR = TopRight, TL = TopLeft, BR = ButtomRight, BL = ButtomLeft

Adafruit_NeoPixel NeoPixelTR = Adafruit_NeoPixel(NeoPixelLedsNum, NeoPixelPinTR, NEO_GRB + NEO_KHZ800); //make NEO_GRB to NEO_RGB if needed
Adafruit_NeoPixel NeoPixelTL = Adafruit_NeoPixel(NeoPixelLedsNum, NeoPixelPinTL, NEO_GRB + NEO_KHZ800); //make NEO_GRB to NEO_RGB if needed
Adafruit_NeoPixel NeoPixelBR = Adafruit_NeoPixel(NeoPixelLedsNum, NeoPixelPinBR, NEO_GRB + NEO_KHZ800); //make NEO_GRB to NEO_RGB if needed
Adafruit_NeoPixel NeoPixelBL = Adafruit_NeoPixel(NeoPixelLedsNum, NeoPixelPinBL, NEO_GRB + NEO_KHZ800); //make NEO_GRB to NEO_RGB if needed


ButtonIRQ CircleButtons(2);

bool last_stat = CircleButtons.isTrue();
int playerTurn = 0;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.print(random(0, 255));

}

bool CheckButton(){
  bool stat = CircleButtons.isTrue();
  if (last_stat != stat){
    playerTurn++;
    if (playerTurn > 4){
      playerTurn = 0;
    }
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  switch (playerTurn){
    case 0: // TR
      Serial.print("TopRight Player Turn");
      NeoPixelTR.rainbow();
      NeoPixelTL.fill(255, 0, 0);
      NeoPixelBR.fill(255, 0, 0);
      NeoPixelBL.fill(255, 0, 0);
      break;
    case 1:
      Serial.print("ButtomRight Player Turn");
      NeoPixelBR.rainbow();
      NeoPixelTL.fill(255, 0, 0);
      NeoPixelTR.fill(255, 0, 0);
      NeoPixelBL.fill(255, 0, 0);
      break;
    case 2:
      Serial.print("ButtomLeft Player Turn");
      NeoPixelBL.rainbow();
      NeoPixelTL.fill(255, 0, 0);
      NeoPixelTR.fill(255, 0, 0);
      NeoPixelBR.fill(255, 0, 0);
      break;
    case 3:
      Serial.print("TopLeft Player Turn");
      NeoPixelBL.rainbow();
      NeoPixelBL.fill(255, 0, 0);
      NeoPixelTR.fill(255, 0, 0);
      NeoPixelBR.fill(255, 0, 0);
      break;
  }


}

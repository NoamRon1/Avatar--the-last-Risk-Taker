#include <Adafruit_NeoPixel.h>
#include <LiquidCrystal_I2C.h> // Library for LCD
#include <time.h>

int NeoPixelLedsNum = 12;
int NeoPixelPinTR = 3;
int NeoPixelPinTL = 5;
int NeoPixelPinBR = 6;
int NeoPixelPinBL = 9;
int a;
int b;
int c;
float start_time = 0;
// TR = TopRight, TL = TopLeft, BR = ButtomRight, BL = ButtomLeft

Adafruit_NeoPixel NeoPixelTR = Adafruit_NeoPixel(NeoPixelLedsNum, NeoPixelPinTR, NEO_GRB + NEO_KHZ800); //make NEO_GRB to NEO_RGB if needed
Adafruit_NeoPixel NeoPixelTL = Adafruit_NeoPixel(NeoPixelLedsNum, NeoPixelPinTL, NEO_GRB + NEO_KHZ800); //make NEO_GRB to NEO_RGB if needed
Adafruit_NeoPixel NeoPixelBR = Adafruit_NeoPixel(NeoPixelLedsNum, NeoPixelPinBR, NEO_GRB + NEO_KHZ800); //make NEO_GRB to NEO_RGB if needed
Adafruit_NeoPixel NeoPixelBL = Adafruit_NeoPixel(NeoPixelLedsNum, NeoPixelPinBL, NEO_GRB + NEO_KHZ800); //make NEO_GRB to NEO_RGB if needed
LiquidCrystal_I2C lcd (0x27, 20, 4); // I2C address 0x27, 20 column and 4 rows

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
  start_time = millis();
  }

void setup() {
  // put your setup code here, to run once:
  // inmode(3, OUTPUT);
  lcd.init(); //initialize the lcd
  lcd.backlight(); //open the backlight 
  lcd.setCursor(0, 0);
  
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
  playerprint(playerTurn);
}


void playerprint(int player){
  Serial.print("Player "); Serial.print(player); Serial.print(" Turn");
  lcd.clear();
  lcd.setCursor(1,0);
  lcd.print("Player "); lcd.print(player);
  lcd.setCursor(8, 1);
  lcd.print("Turn");
  lcd.setCursor(0, 2)
  lcd.print("Time Past: "); lcd.print((millis()-start_time)/1000); lcd.print(" Sec");
  for (int i=0; i<12; i++){
    a = random(0, 255);
    b = random(0, 255);
    c = random(0, 255);
    switch (player){
      case 0:
        NeoPixelTR.setPixelColor(i, NeoPixelTR.Color(a,b,c)); // Moderately bright green color.
        NeoPixelTL.fill(NeoPixelTR.Color(255, 0, 0)); // Moderately bright green color.
        NeoPixelBL.fill(NeoPixelTR.Color(255, 0, 0)); // Moderately bright green color.
        NeoPixelBR.fill(NeoPixelTR.Color(255, 0, 0)); // Moderately bright green color.
        break;
      case 1:
        NeoPixelTL.setPixelColor(i, NeoPixelTR.Color(a,b,c)); // Moderately bright green color.
        NeoPixelTR.fill(NeoPixelTR.Color(255, 0, 0)); // Moderately bright green color.
        NeoPixelBL.fill(NeoPixelTR.Color(255, 0, 0)); // Moderately bright green color.
        NeoPixelBR.fill(NeoPixelTR.Color(255, 0, 0)); // Moderately bright green color.
        break;
      case 2:
        NeoPixelBR.setPixelColor(i, NeoPixelTR.Color(a,b,c)); // Moderately bright green color.
        NeoPixelTL.fill(NeoPixelTR.Color(255, 0, 0)); // Moderately bright green color.
        NeoPixelBL.fill(NeoPixelTR.Color(255, 0, 0)); // Moderately bright green color.
        NeoPixelTR.fill(NeoPixelTR.Color(255, 0, 0)); // Moderately bright green color.
        break;
      case 3:
        NeoPixelBL.setPixelColor(i, NeoPixelTR.Color(a,b,c)); // Moderately bright green color.
        NeoPixelTL.fill(NeoPixelTR.Color(255, 0, 0)); // Moderately bright green color.
        NeoPixelTR.fill(NeoPixelTR.Color(255, 0, 0)); // Moderately bright green color.
        NeoPixelBR.fill(NeoPixelTR.Color(255, 0, 0)); // Moderately bright green color.
        break;
        }
  }
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
// TR = TopRight, TL = TopLeft, BR = ButtomRight, BL = ButtomLeft
}
#include <Adafruit_NeoPixel.h>
#include <LiquidCrystal_I2C.h> // Library for LCD
#include <time.h>

// TR = TopRight, TL = TopLeft, BR = ButtomRight, BL = ButtomLeft
// NeoPixel Conf:
int NeoPixelLedsNumSmall = 12;
int NeoPixelLedsNumBig = 20; //???
int NeoPixelPinTR = 3;
int NeoPixelPinTL = 5;
int NeoPixelPinBR = 6;
int NeoPixelPinBL = 9;

// Random Number Conf:
int a;
int b;
int c;

float start_time = 0; // Time Conf

bool last_stat = digitalRead(2); // Button IRQ Setup

int playerTurn = 0; // Turns Conf
bool safecheck = false; // makes the it will have to be clicked twice to register

// Neo Pixel Setup:
Adafruit_NeoPixel NeoPixelTR = Adafruit_NeoPixel(NeoPixelLedsNum, NeoPixelPinTR, NEO_GRB + NEO_KHZ800); //make NEO_GRB to NEO_RGB if needed
Adafruit_NeoPixel NeoPixelTL = Adafruit_NeoPixel(NeoPixelLedsNum, NeoPixelPinTL, NEO_GRB + NEO_KHZ800); //make NEO_GRB to NEO_RGB if needed
Adafruit_NeoPixel NeoPixelBR = Adafruit_NeoPixel(NeoPixelLedsNum, NeoPixelPinBR, NEO_GRB + NEO_KHZ800); //make NEO_GRB to NEO_RGB if needed
Adafruit_NeoPixel NeoPixelBL = Adafruit_NeoPixel(NeoPixelLedsNum, NeoPixelPinBL, NEO_GRB + NEO_KHZ800); //make NEO_GRB to NEO_RGB if needed

// Screens Setup:
LiquidCrystal_I2C lcd (0x27, 20, 4);
LiquidCrystal_I2C lcd2 (0x27, 20, 4);

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

void lcd_begin():
  lcd.init(); //initialize the lcd
  lcd.backlight(); //open the backlight 
  lcd.setCursor(0, 0);
  lcd2.init();
  lcd2.backlight();
  lcd2.setCursor(0, 0);


void setup() {
  lcd_begin();
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
  lcd2.clear();
  lcd2.setCursor(1,0);
  lcd2.print("Player "); lcd.print(player);
  lcd2.setCursor(8, 1);
  lcd2.print("Turn");
  lcd2.setCursor(0, 2)
  lcd2.print("Time Past: "); lcd.print((millis()-start_time)/1000); lcd.print(" Sec");
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
        //////////////////////////////////////////////////////
       // Name: microntroller.ino                          //
      // Author: Aditya Sakhuja                           //
     // Date: Monday, 20 June 2016                       //
    // Description: Receives 6-bit braille code from    //
   // Raspberry Pi over via a serial connection and    //
  // sends digital signals from OUT pins to           //
 // actuate solenoids for the braille cell bridge.   //
//////////////////////////////////////////////////////

void setup() {
  // Opening Serial Connection
  Serial.begin(9600); 
  // Setting up 6 output pins for solenoid actuation
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
}

void loop() {
  // Stores the state of each pin as data is read
  int state;
  // Iterator for working through pin 8 to 13
  int pin = 8;
  while (Serial.available() > 0) {
    for ( int i = 0; i < 6; i++) {
      state = Serial.read();
      if (state == '1') {
        digitalWrite(pin, HIGH);
        Serial.print("Pin ");
        Serial.print(pin);
        Serial.print(" is set high");
      } else if (state == '0') {
        digitalWrite(pin, LOW);
        Serial.print("Pin ");
        Serial.print(pin);
        Serial.print(" is set low");
      }
      pin++;
    }
  }

}

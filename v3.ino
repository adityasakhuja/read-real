int pin = 8;

void setup() {
  Serial.begin(9600);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
}

void loop() {
  char state;

  while (Serial.available()) {
    state = Serial.read();
    if (state == '1') {
      digitalWrite(pin, HIGH);
    }
    else if (state == '0') {
      digitalWrite(pin, LOW);
    }
    Serial.println(pin);
    Serial.print("State = ");
    Serial.println(state);
    if ( pin < 13) {
      pin++;
    } else {
      pin = 8;
      delay(1000);
    }
  }
}

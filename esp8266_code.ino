int led = D1;
int buzzer = D2;

void setup() {

  Serial.begin(9600);

  pinMode(led, OUTPUT);
  pinMode(buzzer, OUTPUT);

  digitalWrite(led, LOW);
  digitalWrite(buzzer, LOW);
}

void loop() {

  if (Serial.available()) {

    char data = Serial.read();

    if (data == '1') {

      digitalWrite(led, HIGH);
      digitalWrite(buzzer, HIGH);

    } else {

      digitalWrite(led, LOW);
      digitalWrite(buzzer, LOW);
    }
  }
}

#include <Servo.h>
#include "distanceLib.h"

distanceLib dlib;

Servo servo;

#define A 2
#define B 3
#define C 4
#define D 5
#define E 6
#define F 7
#define G 8
#define H 9

#define echoPin 17
#define trigPin 16

#define NUMBER_OF_STEPS_PER_TURN 500 // nemainīt!!!
//#define NUMBER_OF_STEPS_PER_MOVE 100

int NUMBER_OF_STEPS_PER_MOVE = 200; // 100 = 3.5cm;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  servo.attach(10);
  servo.write(85);
  Serial.begin(9600);
  pinMode(15, OUTPUT);
  pinMode(15, OUTPUT);
  pinMode(14, OUTPUT);
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(H, OUTPUT);
  pinMode(G, OUTPUT);
  pinMode(F, OUTPUT);
  pinMode(E, OUTPUT);
  pinMode(D, OUTPUT);
  pinMode(C, OUTPUT);
  pinMode(B, OUTPUT);
  pinMode(A, OUTPUT);

}

/*
  int dist_read() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;
  return (distance);
  }
*/

void writeL(int e, int f, int g, int h) {
  digitalWrite(E, e);
  digitalWrite(F, f);
  digitalWrite(G, g);
  digitalWrite(H, h);
}

void writeR(int a, int b, int c, int d) {
  digitalWrite(A, a);
  digitalWrite(B, b);
  digitalWrite(C, c);
  digitalWrite(D, d);
}

void onestepLF() {
  writeL(1, 0, 0, 0);
  delay(1);
  writeL(1, 1, 0, 0);
  delay(1);
  writeL(0, 1, 0, 0);
  delay(1);
  writeL(0, 1, 1, 0);
  delay(1);
  writeL(0, 0, 1, 0);
  delay(1);
  writeL(0, 0, 1, 1);
  delay(1);
  writeL(0, 0, 0, 1);
  delay(1);
  writeL(1, 0, 0, 1);
  delay(1);
}

void onestepRB() {
  writeR(1, 0, 0, 0);
  delay(1);
  writeR(1, 1, 0, 0);
  delay(1);
  writeR(0, 1, 0, 0);
  delay(1);
  writeR(0, 1, 1, 0);
  delay(1);
  writeR(0, 0, 1, 0);
  delay(1);
  writeR(0, 0, 1, 1);
  delay(1);
  writeR(0, 0, 0, 1);
  delay(1);
  writeR(1, 0, 0, 1);
  delay(1);
}

void stepperClear() {
  writeR(0, 0, 0, 0);
  writeL(0, 0, 0, 0);
}

void onestepRF() {
  writeR(1, 0, 0, 1);
  delay(1);
  writeR(0, 0, 0, 1);
  delay(1);
  writeR(0, 0, 1, 1);
  delay(1);
  writeR(0, 0, 1, 0);
  delay(1);
  writeR(0, 1, 1, 0);
  delay(1);
  writeR(0, 1, 0, 0);
  delay(1);
  writeR(1, 1, 0, 0);
  delay(1);
  writeR(1, 0, 0, 0);
  delay(1);
}

void onestepLB() {
  writeL(1, 0, 0, 1);
  delay(1);
  writeL(0, 0, 0, 1);
  delay(1);
  writeL(0, 0, 1, 1);
  delay(1);
  writeL(0, 0, 1, 0);
  delay(1);
  writeL(0, 1, 1, 0);
  delay(1);
  writeL(0, 1, 0, 0);
  delay(1);
  writeL(1, 1, 0, 0);
  delay(1);
  writeL(1, 0, 0, 0);
  delay(1);
}

void toggleBlinkR() {
  if (digitalRead(15) == HIGH) {
    digitalWrite(15, 0);
  }
  else {
    digitalWrite(15, 1);
  }
}

void toggleBlinkL() {
  if (digitalRead(13) == HIGH) {
    digitalWrite(13, 0);
  }
  else {
    digitalWrite(13, 1);
  }
}

void loop() {
  if (Serial.available() >= 1) {
    char nolasitais = Serial.read();

    if (nolasitais == 'd' || nolasitais == 'D') {
      int dist1; int dist2; int dist3; int rezultats;
      dist1 = dlib.distanceRead();
      delay(200);
      dist2 = dlib.distanceRead();
      delay(200);
      dist3 = dlib.distanceRead();
      rezultats = (dist1 + dist2 + dist3) / 3;
      Serial.print(rezultats);
    }

    if (nolasitais == 'c' || nolasitais == 'C') {
      servo.write(0);
      delay(500);
      servo.write(85);
      delay(500);
      servo.write(360);
      delay(500);
      servo.write(85);
      delay(500);
      digitalWrite(12, 1);
      delay(500);
      digitalWrite(12, 0);
      digitalWrite(13, 1);
      delay(500);
      digitalWrite(13, 0);
      digitalWrite(14, 1);
      delay(500);
      digitalWrite(14, 0);
      digitalWrite(15, 1);
      delay(500);
      digitalWrite(15, 0);
      digitalWrite(11, 1);
      delay(500);
      digitalWrite(11, 0);

    }
    if (nolasitais == 'w' || nolasitais == 'W' ) {
      digitalWrite(15, 1);
      delay(2000);
      digitalWrite(13, 1);
      delay(2000);
      digitalWrite(14, 1);
      delay(2000);
      digitalWrite(11, 1);
      delay(2000);
      digitalWrite(15, 0);
      digitalWrite(13, 0);
      digitalWrite(14, 0);
      digitalWrite(11, 0);
      digitalWrite(12, 1);
      delay(200);
      digitalWrite(12, 0);
      delay(200);
      digitalWrite(12, 1);
      delay(200);
      digitalWrite(12, 0);
      delay(200);
      digitalWrite(12, 1);
      delay(200);
      digitalWrite(12, 0);
      delay(100);
    }
    if (nolasitais == 'f' || nolasitais == 'F' ) {
      int i;
      i = 0;
      digitalWrite(12, 1);
      while (i < NUMBER_OF_STEPS_PER_MOVE) {
        onestepRF();
        onestepLF();
        i++;
      }
      stepperClear();
      digitalWrite(12, 0);
      delay(100);
    }

    if (nolasitais == 'b' || nolasitais == 'B' ) {
      int i;
      i = 0;
      digitalWrite(11, 1);
      while (i < NUMBER_OF_STEPS_PER_MOVE) {
        onestepRB();
        onestepLB();
        i++;
      }
      stepperClear();
      digitalWrite(11, 0);
      delay(100);
    }

    if (nolasitais == 'l' || nolasitais == 'L' ) {
      int i;
      i = 0;
      while (i < NUMBER_OF_STEPS_PER_TURN / 2) {
        if (i % 20 == 0) {
          toggleBlinkL();
        }
        onestepRF();
        onestepLB();
        i++;
      }
      stepperClear();
      digitalWrite(13, 0);
      delay(100);
    }

    if (nolasitais == 'r' || nolasitais == 'R' ) {
      int i;
      i = 0;
      while (i < NUMBER_OF_STEPS_PER_TURN / 2) {
        if (i % 20 == 0) {
          toggleBlinkR();
        }
        onestepRB();
        onestepLF();
        i++;
      }
      stepperClear();
      digitalWrite(15, 0);
      delay(100);
    }

    if (nolasitais == 'v' || nolasitais == 'V' ) {
      int i;
      i = 0;
      servo.write(0);
      while (i < NUMBER_OF_STEPS_PER_TURN / 4) {
        onestepRF();
        i++;
      }
      servo.write(85);
      i = 0;
      while (i < NUMBER_OF_STEPS_PER_TURN / 4) {
        onestepRB();
        i++;
      }
      servo.write(360);
      i = 0;
      while (i < NUMBER_OF_STEPS_PER_TURN / 4) {
        onestepLF();
        i++;
      }
      servo.write(85);
      i = 0;
      while (i < NUMBER_OF_STEPS_PER_TURN / 4) {
        onestepLB();
        i++;
      }
      servo.write(85);
      stepperClear();
    }

    if (nolasitais == '8') {
      servo.write(85);
      int i = 0;
      while (i < 25) {
        onestepLF();
        onestepRF();
        i++;
      }
      stepperClear();
      toggleBlinkL();
      toggleBlinkR();
      delay(5000);
      toggleBlinkL();
      toggleBlinkR();
      i = 0;
      while (i < 25) {
        onestepRB();
        onestepLB();
        i++;
      }
      stepperClear();
    }


    if (nolasitais == '6') {
      servo.write(0);
      int i = 0;
      while (i < 25) {
        onestepLF();
        onestepRB();
        i++;
      }
      stepperClear();
      toggleBlinkR();
      delay(5000);
      toggleBlinkR();
      servo.write(85);
      i = 0;
      while (i < 25) {
        onestepRF();
        onestepLB();
        i++;
      }
      stepperClear();
    }

    if (nolasitais == '4') {
      servo.write(290);
      int i = 0;
      while (i < 25) {
        onestepRF();
        onestepLB();
        i++;
      }
      stepperClear();
      toggleBlinkL();
      delay(5000);
      toggleBlinkL();
      servo.write(85);
      i = 0;
      while (i < 25) {
        onestepLF();
        onestepRB();
        i++;
      }
      stepperClear();
    }


  }
}

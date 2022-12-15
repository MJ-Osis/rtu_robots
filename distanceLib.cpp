#include "distanceLib.h"
#define echoPin 17
#define trigPin 16
long duration;
int distance;

distanceLib::distanceLib(bool displayMsg) {
  Serial.begin(9600);
  Serial.println("Library working...");
}


int distanceLib::distanceRead() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;
  return distance;

}

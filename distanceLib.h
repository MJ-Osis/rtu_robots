#ifndef t1
#define t1

#if (ARDUINO>=100)
#include "Arduino.h"
#else
#include "WProgram.h"
#endif
class distanceLib {
  public:
  distanceLib(bool displayMsg=false);
  void begin (int baudRate=9600);
  int distanceRead();
  private:
};

#endif

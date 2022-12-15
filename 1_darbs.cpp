int ledLampina = 9; //Integer - vesels skaitlis
int cipars1 = 8;
int cipars2 = 15;


/**
 * int - vesels skaitlis
 * long - vesels skaitlis - lielaks
 * byte - vesels skaitlis - 0 - 255
 * float - skaitlis ar komatu (peldosais punksts)
 * double - skaitlis ar komatu (peldosais punksts) - lielaks
 * 
 * char - simboli
 * boolean (bool) - true / false
*/

/**
 * baits (byte) - mazaka atminas dala
 * bits - vismazak vertiba datoraa (0 1)
 * 
 * 1 byte = 8 bit
 * 0000 0000 = 0
 * 1111 1111 = 255
 * 
 * int = 2byte = 16bit
 * 0000 0000 0000 0000
 * 0111 1111 1111 1111 = 32,767
 * 1111 1111 1111 1111 = 65,535
 * 
 * 
*/

char simbolsCipars = 65;
char simbolsBurts = 'G';

void setup() {
  Serial.begin(9600); // Atver komunikacijas portu starp datoru un Arduino
  pinMode(ledLampina, OUTPUT);
  
  manaFunkcija();

  funkcijaBezArgumentiem();

  Serial.println("Talak bus izsaukta int funkcijaArArgumentiem(x, y).");
  Serial.println("Si funkcija atgriez vertibu, un pati funkcija ir izsaukta caur Serial.println():");
  Serial.println(funkcijaArArgumentiem(cipars1, cipars1));

  Serial.print("Mainigais ar tipu char = 65 : ");
  Serial.println(simbolsCipars);
  Serial.print("Mainigais ar tipu char = 'G' : ");
  Serial.println(simbolsBurts);  
}

void loop() {
  digitalWrite(ledLampina, HIGH);
  delay(1000);  //milisekundes
  digitalWrite(ledLampina, LOW);
  delay(1000);
  
}

//////////////////////////////////////////////////////////////////////////
//Zemaak ir defineta funkcija kas neatgriez nekadu informaciju / vertibas
//////////////////////////////////////////////////////////////////////////

void manaFunkcija(){
  Serial.println("Jus izsaucat void manaFunkcija()");
  Serial.println();
}


/////////////////////////////////////////////////////////////////////////////
//Zemaak ir defineta funkcija kas var atgriezt argumentus, bet seit neatgriez
/////////////////////////////////////////////////////////////////////////////

int funkcijaBezArgumentiem(){ //funkcija kas var atgriezt argumentus, bet seit neatgriez
  int atbilde = cipars1 + cipars2;
  Serial.println("Jus izsaucat int funkcijaBezArgumentiem()");
  Serial.println("Si funkcija netgriez vertibas!");
  Serial.print("Atbilde ir izprinteta no pasas funkcijas: ");
  Serial.println(atbilde);
  Serial.println();
}


/////////////////////////////////////////////////////////////////////////////////////////
//Zemaak ir defineta funkcija, kas atgriez vertibas, pec funkcijas izpildes paliek cipars
// + si funkcija sanem argumentus (ciparus)
/////////////////////////////////////////////////////////////////////////////////////////

int funkcijaArArgumentiem(int x, int y){  //funkcija, kas atgriez vertibas, pec funkcijas izpildes paliek cipars
  int atbilde = x + y; //8 + 15 = 23
  return atbilde;
}
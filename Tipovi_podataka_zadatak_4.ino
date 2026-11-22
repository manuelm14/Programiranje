// C++ code
//

char oznakaKucista = 'T'; // Zauzima 1 B
bool termickaZastita = false; // Logicka vrijednost
unsigned int ulNapon_mV = 12500; // Ima raspon do 65535
unsigned int izNapon_mV = 5000; // Ima raspon do 65535
unsigned int struja_mA = 450; // ima raspon do 65535
unsigned long vrijeme_s = 86400; // Potreban je 32-bitni tip
float U_pad; 
float P_dis;
float E_toplina; 
unsigned int SRAM; 

void setup(){
  Serial.begin (9600);
  U_pad = (ulNapon_mV - izNapon_mV) / 1000;
  P_dis = U_pad * (struja_mA / 1000);
  E_toplina = P_dis * vrijeme_s;
  
  SRAM = sizeof (oznakaKucista)+
         sizeof (termickaZastita)+
         sizeof (ulNapon_mV)+
         sizeof (izNapon_mV)+
         sizeof (struja_mA)+
         sizeof (vrijeme_s)+
         sizeof (U_pad)+
         sizeof (P_dis)+
         sizeof (E_toplina)+
         sizeof (SRAM);
  
  Serial.println("Linearni stabilizator 7805");
  Serial.print("Oznaka kućišta regulaotra: ");
  Serial.println(oznakaKucista);
  Serial.print("Status termičke zaštite: ");
  Serial.println(termickaZastita);
  Serial.print("Pad napona: ");
  Serial.print(U_pad, 3);
  Serial.println(" V");
  Serial.print("Disipirana (toplinska) snaga: ");
  Serial.print(P_dis, 3);
  Serial.println(" W");
  Serial.print("Ukupna toplinska energija: ");
  Serial.print(E_toplina, 3);
  Serial.println(" J");
  Serial.print("Zauzeće radne memorije: ");
  Serial.print(SRAM);
  Serial.println(" bajtova od 2048B");
}

void loop(){
  
}

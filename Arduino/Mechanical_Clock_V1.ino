const int sensorPin = A0;  // Analog input pin that senses Vout
int sensorValue = 0;       // sensorPin default value
float Vin = 5;             // Input voltage
float Vout = 0;            // Vout default value
float Rref = 1000;          // Reference resistor's value in ohms (you can give this value in kiloohms or megaohms - the resistance of the tested resistor will be given in the same units)
float R = 1000;               // Tested resistors default value
int clk = 0;          
const int tickTHold = 110;
int ticks;
String Dout;

void setup ()
{
  Serial.begin(9600);      // Initialize serial communications at 9600 bps
}

void loop ()
{
  sensorValue = analogRead(sensorPin);  // Read Vout on analog input pin A0 (Arduino can sense from 0-1023, 1023 is 5V)
  Vout = (Vin * sensorValue) / 1023;    // Convert Vout to volts
  R = Rref * (1 / ((Vin / Vout) - 1));  // Formula to calculate tested resistor's value               
  if (R >= tickTHold){
    ticks += 1;
  }

  Dout = String(R) + ":" + String(ticks);
  Serial.println(Dout);
  delay(100);
}
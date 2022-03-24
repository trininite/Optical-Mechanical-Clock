long unsigned int clk = 0;

void setup() 
{
  Serial.begin(9600);
  delay(1000);
}

void loop() 
{
  Serial.println(clk);
  clk += 1;
  delay(1000);
}

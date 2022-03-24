
import processing.serial.*;

Serial port;
String val;

void setup() 
{ 
  size(400, 400);    //window size, (width, height)
  //String comName = Serial.list()[0];
  port = new Serial(this, "/dev/ttyACM0", 9600); 
}


void draw() 
{
    val = port.readStringUntil('\n');
    println(val);
}

void serialEvent(Serial port)
{    
  
  println(val);
}

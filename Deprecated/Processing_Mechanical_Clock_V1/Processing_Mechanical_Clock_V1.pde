import processing.serial.*;
import controlP5.*;
ControlP5 cp5;

Textlabel TickCountHeader;
Textlabel TickCount;

Textlabel CalculatedTimeHeader;
Textlabel CalculatedTime;


Serial port;
String val;
int tkclk;
int calclk;

void setup() 
{ 
  cp5 = new ControlP5(this);
  port = new Serial(this, "/dev/ttyACM0", 9600); 
  size(400,400);
  smooth();
  
  TickCountHeader = cp5.addTextlabel("TickCountHeader")    //Tick Count Stuff Start
    .setText("Tick Count:")
    .setPosition(20,50)
    .setColorValue(0xffffffff)
    .setFont(createFont("",20))
    ;

  TickCount = cp5.addTextlabel("TickCount")  
    .setText("0")
    .setPosition(135,50)
    .setColorValue(0xffffffff)
    .setFont(createFont("",20))
    ;                                              //Tick Count Stuff End
    
    
    
  CalculatedTimeHeader = cp5.addTextlabel("CalcTimeHeader") //Calculated Time Stuff Start
    .setText("Calculated Time")
    .setPosition(20,70)
    .setColorValue(0xffffffff)
    .setFont(createFont("Georgia",20))
    ;

  CalculatedTime = cp5.addTextlabel("CalcTime")
    .setText("0")
    .setPosition(170,70)
    .setColorValue(0xffffffff)
    .setFont(createFont("Georgia",20))
    ;                                           //Calculated Time Stuff

                 
              
}


void draw()
{
  background(0);
  if ( port.available() > 0) 
  {  // If data is available,
  tkclk += 1;
  val = port.readString();   // read it and store it in val
  TickCount.setText(val);
  delay(100);
  
  if (tkclk % 5 == 0)
  calclk += 1;
  CalculatedTime.setText(str(calclk));
  delay(1000);
  ;
  } 

    }
                   

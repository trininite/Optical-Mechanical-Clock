import processing.serial.*;
import controlP5.*;
ControlP5 cp5;

Textlabel countLabel;

Toggle motorToggle;
Toggle LEDToggle;

Serial port;
char val;

void setup() 
{ 
  cp5 = new ControlP5(this);
  port = new Serial(this, "/dev/ttyACM0", 9600); 
  size(400,400);
  smooth();
  
  

  motorToggle = cp5.addToggle("Motor Toggle")   // create a toggle and change the default look to a (on/off) switch look
                 .setPosition(40,40)
                 .setSize(80,20)
                 .setValue(false)
                 .setMode(ControlP5.SWITCH)
                 ;         

  LEDToggle = cp5.addToggle("LED Toggle")   // create a toggle and change the default look to a (on/off) switch look
                 .setPosition(40,80)
                 .setSize(80,20)
                 .setValue(false)
                 .setMode(ControlP5.SWITCH)
                 ;                 
                 
  countLabel = cp5.addTextlabel;
              
                 
              
  }


void draw()
{
  
}                     





	

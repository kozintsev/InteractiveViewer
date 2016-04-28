#!/usr/bin/env python
import os
import math
from OCC.BRepPrimAPI import BRepPrimAPI_MakeCylinder
from OCC.gp import gp_Ax2, gp_Pnt, gp_Dir

display.EraseAll()

#
# Make the 1st cylinder
#
cyl1 = BRepPrimAPI_MakeCylinder(50,200)
cyl1_shape = cyl1.Shape()
#
# Make the 2nd cylinder
#
cyl2 = BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(200, 200, 0), gp_Dir(0, 0, 1)), 40, 110, 210*math.pi/180)
cyl2_shape = cyl2.Shape()

display.DisplayShape(cyl2_shape)

display.View_Iso()
#
# Export result to IGES file
#
# i = OCC.IGESControl_Controller()
# i.Init()
# iges_writer = OCC.IGESControl_Writer()
# iges_writer.AddShape(cyl1_shape)
# iges_writer.AddShape(cyl2_shape)
# iges_writer.Write("./cylinder.iges")


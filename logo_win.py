from turtle import*

#dessiner le logo d'ouverture de windows

speed(2)

bgcolor('black')
penup()

goto(-50,60)
pendown()
color('#00ADEF')
begin_fill()

goto(100,100) 
goto(100,-100)
goto(-50,-60)
goto(-50,60)
end_fill()

color("black")
goto(15,100)
color("black")
width(6)
goto(15,-100)
penup()
goto(100,0)
pendown()
goto(-100,0)

#ecriture du nom de H2L

#premier trait du H
penup()
goto(-100,-150)
color('#00ADEF')
width(3)
pendown()
right(90)
forward(60)
penup()

#trait d_union des deux traits du H
backward(30)
left(90)
pendown()
forward(30)

#deuxieme traits du H
penup()
goto(-70,-150)
right(90)
pendown()
forward(60)

# premier L
penup()
goto(-40,-150)
pendown()
forward(60)
left(90)
forward(30)

#deuxieme L
penup()
goto(20,-150)
right(90)
pendown()
forward(60)
left(90)
forward(30)

#traits de soulignement du nom
penup()
goto(-100,-220)
pendown()
forward(150)

done()

import pygame as pg
pg.font.init()
w = pg.display.set_mode((268, 50))
enterfont = pg.font.Font(None, 32)
c = pg.time.Clock()
textboxrect = pg.Rect(9, 9, 250, 32)
inactivecolor = (0, 153, 51)
activecolor = (102, 255, 102)
black = (0, 0, 0)
currentcolor = inactivecolor
timer = 0
typer = True
active = False
boxtext = ''
donetext = False
while not donetext:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            donetext = True
        if event.type == pg.MOUSEBUTTONDOWN:
            if textboxrect.collidepoint(event.pos):
                active = not active
            else:
                active = False
            currentcolor = activecolor if active else inactivecolor
        if event.type == pg.KEYDOWN:
            if active:
                if event.key == pg.K_RETURN:
                    word = boxtext
                    print("You entered: " + str(boxtext) + ". ")
                    boxtext = ''
                elif event.key == pg.K_BACKSPACE:
                    boxtext = boxtext[:-1]
                else:
                    boxtext += event.unicode
    w.fill((255, 255, 255))
    surfacetext = enterfont.render(boxtext, True, currentcolor)
    width = max(250, surfacetext.get_width() + 10)
    textboxrect.w = width
    w.blit(surfacetext, (textboxrect.x + 5, textboxrect.y + 5))
    x, y = ((surfacetext.get_width() + (textboxrect.x + 5))), (textboxrect.y + 5)
    wi, h = ((surfacetext.get_width() + (textboxrect.x + 5)), ((textboxrect.y + textboxrect.h) - 5))
    if active:
        timer += c.get_time()
        if timer >= 550:
            timer = 0
            typer = not typer
        if typer:
          pg.draw.line(w, black, (x, y), (wi, h), 2)
    pg.draw.rect(w, currentcolor, textboxrect, 2)
    pg.display.flip()
    c.tick(30)
